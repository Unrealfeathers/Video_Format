import os
import secrets
import ffmpeg


def main():
    cwd = os.getcwd()
    files = os.listdir(cwd)

    for file in files:
        if file == "main.py" or file == ".idea":
            continue

        if file.endswith(('.avi', '.flv', '.rm', '.wmv', '.rmvb', '.mpg')):
            try:
                name = secrets.token_hex(16)
                new_file = name + ".mp4"
                ffmpeg.input(file).output(new_file).run()
            except Exception:
                name = secrets.token_hex(16)
                new_file = name + ".mp4"
                ffmpeg.input(file).output(new_file).run()
            continue

        # 判断文件名是否为32位16进制数
        if len(file.split(".")[0]) != 16 or all(c in '0123456789abcdef' for c in file.split(".")[0]):
            print("No 16 hex")
            try:
                name = secrets.token_hex(16)
                os.renames(cwd + "\\" + file, name + "." + file.split(".")[-1])
            except Exception:
                name = secrets.token_hex(16)
                os.renames(cwd + "\\" + file, name + "." + file.split(".")[-1])


if __name__ == "__main__":
    main()
