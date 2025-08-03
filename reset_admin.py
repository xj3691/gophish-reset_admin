# reset_admin.py
import bcrypt, sqlite3, sys

new_password = input("请输入新密码: ").strip()
if not new_password:
    print("密码不能为空")
    sys.exit(1)

hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
conn = sqlite3.connect("gophish.db")
conn.execute("UPDATE users SET hash=? WHERE username='admin'", (hashed,))
conn.commit()
conn.close()
print("密码已重置，请用 admin / 新密码 登录")