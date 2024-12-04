import sys

def main():
    # 从命令行获取参数
    if len(sys.argv) != 3:
        print("错误：请提供用户名和密码作为参数！")
        return

    username = sys.argv[1]
    password = sys.argv[2]

    # 打印接收到的用户名和密码
    print(f"接收到的用户名: {username}")
    print(f"接收到的密码: {password}")

if __name__ == "__main__":
    main()
