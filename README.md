# gophish-reset_admin
在Gophish v0.11.0 及以上版本，忘记admin密码可用。
1，进入 Gophish 目录（含 gophish.db）。
2，在同一目录下新建文件 reset_admin.py
3，运行脚本（需要安装 bcrypt，通常自带）：
  python reset_admin.py
如果提示缺少 bcrypt，先装它（通常很快）：
pip install bcrypt -i https://pypi.tuna.tsinghua.edu.cn/simple
4，重启 Gophish，用刚设置的新密码登录即可。
