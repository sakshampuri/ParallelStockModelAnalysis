import os


def get_file_path():
    return os.getcwd()


if __name__ == "__main__":
    print(get_file_path())