import tkinter as tk
from tkinter import messagebox
import subprocess  # 用于调用外部 Python 文件

# 创建主窗口
root = tk.Tk()
root.title("主菜单")
root.geometry("700x800")

# 用于放置子窗口内容的主框架
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# 清除框架内容
def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# 子窗口 - 表定义
def open_table_definition_window():
    clear_frame()

    # 子窗口布局
    tk.Label(main_frame, text="入力文件名:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    file_name_entry = tk.Entry(main_frame)
    file_name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(main_frame, text="表名:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    table_name_entry = tk.Entry(main_frame)
    table_name_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(main_frame, text="出力文件名:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    output_file_name_entry = tk.Entry(main_frame)
    output_file_name_entry.grid(row=2, column=1, padx=10, pady=10)

    # 调用外部 Python 文件
    def call_external_script():
        input_file = file_name_entry.get()
        table_name = table_name_entry.get()
        output_file = output_file_name_entry.get()

        if not input_file or not table_name or not output_file:
            messagebox.showwarning("警告", "所有字段都必须填写！")
            return

        # 调用另一个 Python 文件，传递参数
        try:
            subprocess.run(["python", "table_definition.py", input_file, table_name, output_file])
            messagebox.showinfo("完成", "表定义已生成！")
        except Exception as e:
            messagebox.showerror("错误", f"执行出错: {e}")

    tk.Button(main_frame, text="生成", command=call_external_script).grid(row=3, column=0, columnspan=2, pady=20)

# 子窗口 - 表插入
def open_table_insert_window():
    clear_frame()

    # 插入按钮
    def call_insert_script():
        try:
            subprocess.run(["python", "table_insert.py"])
            messagebox.showinfo("完成", "表数据已插入！")
        except Exception as e:
            messagebox.showerror("错误", f"执行出错: {e}")

    tk.Label(main_frame, text="表插入操作", font=("Arial", 14)).pack(pady=20)
    tk.Button(main_frame, text="插入", command=call_insert_script).pack(pady=50)

# 子窗口 - データ作成
def open_data_generate_window():
    clear_frame()

    # 子窗口布局
    tk.Label(main_frame, text="入力文件名:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    input_file_name_entry = tk.Entry(main_frame)
    input_file_name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(main_frame, text="出力文件名:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    output_file_name_entry = tk.Entry(main_frame)
    output_file_name_entry.grid(row=1, column=1, padx=10, pady=10)

    # 调用外部 Python 文件
    def call_external_script():
        input_file = "./input/"+input_file_name_entry.get()
        output_file = "./input/"+output_file_name_entry.get()

        if not input_file:
            messagebox.showwarning("警告", "所有字段都必须填写！")
            return

        # 调用另一个 Python 文件，传递参数
        try:
            subprocess.run(["python", "GenerateDataMultiSheet.py", input_file,output_file])
            messagebox.showinfo("完成", "表定义已生成！")
        except Exception as e:
            messagebox.showerror("错误", f"执行出错: {e}")

    tk.Button(main_frame, text="生成", command=call_external_script).grid(row=3, column=0, columnspan=2, pady=20)

# 菜单
menu_bar = tk.Menu(root)
db_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="データベース作成", menu=db_menu)

# 子菜单
db_menu.add_command(label="テーブル定義", command=open_table_definition_window)
db_menu.add_command(label="テーブルINSERT", command=open_table_insert_window)
db_menu.add_command(label="データの作成", command=open_data_generate_window)

# 设置菜单到主窗口
root.config(menu=menu_bar)

# 运行主窗口
root.mainloop()
