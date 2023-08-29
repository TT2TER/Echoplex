import os


savepath = "files/token/token.txt"
# 如果savepath不存在，创建savepath
os.makedirs(os.path.dirname(savepath), exist_ok=True)