# socat TCP-LISTEN:6000,fork,reuseaddr EXEC:"python main.py",pty,stderr

flag = "hackerman{Sup3r_S3cr3t_Flag}"

def freeflagmenu():
    print("==================Free Flag Menu==================")
    print()
    print("1. Show Flag")
    print("2. Exit")
    print()
    print("===================================================")
    print()
    choice = input("Enter your choice: ")
    if choice == "1":
        print(flag)
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
    exit()

if __name__ == '__main__':
    freeflagmenu()