import shutil
import subprocess
import sys
from pathlib import Path

from genPyiReWhl import re_zip

# vcvars_bat = r"D:\VS2019\VC\Auxiliary\Build\vcvars64.bat"
vcvars_bat = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"

# 虚拟环境路径配置
venv_dir = Path(".venv")
project_dir = Path(__file__).resolve().parent.parent
python_exe = venv_dir / "Scripts" / "python.exe"

print(f"项目路径: {project_dir}")
print(f"虚拟环境 Python 路径: {python_exe}")
cache_dir = project_dir / ".py-build-cmake_cache"
if cache_dir.exists():
    print(r"删除旧生成目录 ..\.py-build-cmake_cache")
    shutil.rmtree(cache_dir)

# 注意 cmd /c + 路径引号
build_cmd = f'"{python_exe}" -m build --no-isolation --wheel'
cmdline = f'cmd /c ""{vcvars_bat}" && {build_cmd}"'
print(f"执行命令: {cmdline}")

with subprocess.Popen(cmdline,
                      cwd=project_dir,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.STDOUT,
                      text=True,
                      shell=True) as proc:
    for line in proc.stdout:
        print(line, end='')

    proc.wait()
    if proc.returncode == 0:
        print("构建成功")
        re_zip()
    else:
        print("构建失败，退出码:", proc.returncode)
        sys.exit(proc.returncode)
