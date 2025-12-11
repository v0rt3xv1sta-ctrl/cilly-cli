import os

print("Welcome To Cilly CLI")
while True:
    try:
        cwd = os.getcwd()
        cmd = input(f"{cwd} >> ")

        if cmd == "exit":
            break

        elif cmd.startswith("cd "):
            os.chdir(cmd[3:])

        else:
            os.system(cmd)

    except:
        print("Hi you might have gotten the wrong command.")

    