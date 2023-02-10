from Utilities.getpath import get_file_path
import os


_directory_name = 'TextFilesData'


def create_text_file(file_name: str):
    """
        Creating new text file.
    :param file_name: Name of text file, which needs to be created.
    """

    file_path = get_file_path(_directory_name, file_name)
    open(file_path, "x")


def write_text_file(file_name: str, data: str):
    """
        Writing text file, here it will check if text file already exists, it will delete it,
        else just write it down the data, which was asked.
    :param file_name: Name of the text file, where data needs to be inserted.
    :param data: Data which needs to be entered in text file.
    """

    file_path = get_file_path(_directory_name, file_name)
    check_file = os.path.isfile(file_path)
    if check_file is True:
        os.remove(file_path)
    open(file_path, "x")
    file_name = open(file_path, "w")
    file_name.write(data)


def read_text_file(file_name: str) -> str:
    """
        Read the contents of text file and return the value at the end.
    :param file_name: Name of the file, from where value needs to be retrieved.
    :return: Contents of text file in string format.
    """

    file_path = get_file_path(_directory_name, file_name)
    with open(file_path) as f:
        lines = f.read()
    return lines
