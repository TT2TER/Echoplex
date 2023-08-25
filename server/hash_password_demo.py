import hashlib
import os


def hash_password(password, salt=None, iterations=100000):
    if salt is None:
        salt = os.urandom(16)  # 生成随机盐

    # 将盐和密码组合后进行迭代哈希
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return salt, hashed_password


def verify_password(input_password, salt, stored_hashed_password, iterations=100000):
    hashed_input_password = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, iterations)
    return hashed_input_password == stored_hashed_password


# 示例用法
user_password = "securepassword"
salt, hashed_password = hash_password(user_password)
print("Salt:", salt)
print("Hashed Password:", hashed_password)

# 验证密码
input_password = "securepassword"
password_match = verify_password(input_password, salt, hashed_password)
print("Passwords match:", password_match)
