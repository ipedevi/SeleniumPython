import os


class Config:
    url = "about:blank"
    default_browser = "chrome"
    command_executor = 'http://127.0.0.1:4444/wd/hub'
    project_root = "."
    results_dir = "./results"
    implicit_wait = 10
    SEPARATOR = os.path.sep

    def __init__(self):
        print("Standard configuration")
