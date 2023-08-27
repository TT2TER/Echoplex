import os


def get_file_extension(filepath):
    _, file_extension = os.path.splitext(filepath)
    return file_extension.lower()
