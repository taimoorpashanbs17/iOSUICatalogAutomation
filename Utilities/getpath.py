import os
import platform


def get_file_path(directory_name: str, file_name: str) -> str:
    """
    Helper method to get the file path regardless of OS, so that user don't have to add absolute path again and again.
    :param directory_name: Name of the directory, where we have to access the file.
    :param file_name: Name of the file, which needs to be accessed.
    :return: Absolute File path of file, which needs to be accessed.
    """

    os_name = platform.system()
    current_path = os.getcwd()
    file_path = None
    parent_directory = os.path.dirname(current_path)
    if os_name == "Windows":
        file_path = os.path.abspath(parent_directory +
                                    "//" + directory_name + "//" + file_name)
    elif os_name == "Linux" or "Darwin":
        file_path = os.path.abspath(parent_directory +
                                    "/" + directory_name + "/" + file_name)
    return file_path
