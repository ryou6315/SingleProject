import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("300x200")

# 模拟的用户数据
USER_DATA = {
    "admin": "123456",
    "user": "password"
}

# 登录功能
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_DATA and USER_DATA[username] == password:
        messagebox.showinfo("登录成功", f"欢迎，{username}！")
    else:
        messagebox.showerror("登录失败", "用户名或密码错误！")

# 清空输入框
def clear_inputs():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# 创建标签和输入框
tk.Label(root, text="用户名:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="密码:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# 创建按钮
login_button = tk.Button(root, text="登录", command=login)
login_button.grid(row=2, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="清空", command=clear_inputs)
clear_button.grid(row=2, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()
