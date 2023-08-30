from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from db.DataDB import select_table
import json
import smtplib
import rsa
from tool_fuction import load_keys


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def retrieve_password(received_data, socket, address, database):
    from_addr = "fluppyfr@163.com"
    smtp_server = "smtp.163.com"
    password = "VXQBWCZGYBRDEGEC"
    content = received_data['content']
    user_id = content['user_id']
    ret = select_table(database, "user", user_id=user_id)
    # to_addr = user_email
    to_addr = ret[0][3]
    rsa_pwd = ret[0][2]
    pubkey, privkey = load_keys()
    user_pwd = rsa.decrypt(rsa_pwd, privkey).decode()

    body = f"""
    尊敬的用户，
    
    您的登录密码已找回。以下是您的登录信息：
    
    用户名：{user_id}
    密码：{user_pwd}
    
    请妥善保管您的登录信息，不要与他人分享。如果您有任何疑问或需要帮助，请随时联系我们的客服团队。
    
    感谢您的使用！
    
    最好的祝愿，
    您的平台团队
    """

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = _format_addr('IMsoftware <%s>' % from_addr)
    msg['To'] = _format_addr('杂鱼用户 <%s>' % to_addr)
    msg['Subject'] = Header('您似乎忘记了密码……', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print(f"向{to_addr}发送了邮件")
    # data = {
    #     "type": "retrieve_password",
    #     "back_data": "0000",
    #     "content": None
    # }
    # json_data = json.dumps(data).encode('utf-8')
    # socket.sendall(json_data)
