import subprocess
import sys


def install():
    package_name = "PySide6QCustomPlot2"

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package_name, "-y"])
    subprocess.check_call([sys.executable,
                           "-m",
                           "pip",
                           "install",
                           r"..\dist\PySide6QCustomPlot2-2.1.1-cp311-cp311-win_amd64.whl"
                           ])


if __name__ == '__main__':
    install()
