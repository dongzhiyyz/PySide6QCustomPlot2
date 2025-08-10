import csv
import hashlib
import os
import sys
import ctypes
import builtins
import time
from textwrap import dedent

import PySide6
import zipfile
import shutil
from pathlib import Path



def gen_pyi(out_dir: Path):
    dll_paths = [
        r"..\.venv\Lib\site-packages\PySide6",  # PySide6的DLL路径
        r"..\.venv\Lib\site-packages\shiboken6",  # shiboken6的DLL路径
    ]

    critical_dlls = [
        "Qt6Core.dll",
        "Qt6Gui.dll",
        "Qt6Widgets.dll",
        'Qt6PrintSupport.dll',
        'pyside6.abi3.dll',
        "shiboken6.abi3.dll",
    ]

    for dll_name in critical_dlls:
        for dll_path in dll_paths:
            dll_full_path = os.path.join(dll_path, dll_name)
            if os.path.exists(dll_full_path):
                try:
                    ctypes.CDLL(dll_full_path)
                    print(f"预加载DLL成功: {dll_full_path}")
                    break
                except OSError as e:
                    print(f"预加载DLL失败 {dll_full_path}: {e}")

    builtins.PySide6 = PySide6  # 注入到全局环境中

    try:
        from shibokensupport.signature.lib import pyi_generator
        sys.argv = [
            "pyi_generator",
            "--outpath", f"{out_dir}/PySide6QCustomPlot2",
            "../.py-build-cmake_cache/cp311-cp311-win_amd64/PySide6QCustomPlot2.pyd"
        ]
        pyi_generator.main()

        # 原来的内容
        old_line = {
            "class QCustomPlot(PySide6.QtWidgets.QWidget):"                  :
                """
                class QCustomPlot(PySide6.QtWidgets.QWidget):
                    xAxis: QCPAxis
                    yAxis: QCPAxis
                    xAxis2: QCPAxis
                    yAxis2: QCPAxis
                    legend: QCPLegend
                """,
            "class QCPItemText(PySide6QCustomPlot2.QCPAbstractItem):"        :
                """
                class QCPItemText(PySide6QCustomPlot2.QCPAbstractItem):
                    position_item: QCPItemPosition
                    topLeft: QCPItemAnchor
                    top: QCPItemAnchor
                    topRight: QCPItemAnchor
                    right: QCPItemAnchor
                    bottomRight: QCPItemAnchor
                    bottom: QCPItemAnchor
                    bottomLeft: QCPItemAnchor
                    left: QCPItemAnchor
                """,
            "class QCPItemTracer(PySide6QCustomPlot2.QCPAbstractItem):"      :
                """
                class QCPItemTracer(PySide6QCustomPlot2.QCPAbstractItem):
                    position_item: QCPItemPosition
                """,
            "class QCPRange(Shiboken.Object):"                               :
                """
                class QCPRange(Shiboken.Object):
                    lower: float
                    upper: float
                """,
            "class KeyValues(Shiboken.Object):"                              :
                """
                class KeyValues(Shiboken.Object):
                    keys: List[float]
                    values: List[float]
                """,
            "class QCPItemStraightLine(PySide6QCustomPlot2.QCPAbstractItem):":
                """
                class QCPItemStraightLine(PySide6QCustomPlot2.QCPAbstractItem):
                    point1: QCPItemPosition
                    point2: QCPItemPosition
                """
        }

        # 新的内容
        time.sleep(0.01)
        print("pyi生成完成!\n")

        # 读取并替换
        original_whl = f'{out_dir}/PySide6QCustomPlot2/PySide6QCustomPlot2.pyi'
        with open(original_whl, 'r', encoding='gbk') as f:
            content = f.read()

        for key, value in old_line.items():
            content = content.replace(key, dedent(value).strip())

        # 写入文件
        with open(original_whl, 'w') as f:
            f.write(content)

        print("修改QCustomPlot完成!")

        return True

    except ImportError as e:
        print(f"导入错误: {e}")
        return False

    except Exception as e:
        print(f"执行错误: {e}")
        return False


def re_zip():
    # === 配置 ===
    src_lower = "pyside6qcustomplot2"  # 原始小写包名
    dst_upper = "PySide6QCustomPlot2"  # 替换为的大写包名
    base_dir = Path(__file__).resolve().parent
    temp_dir = base_dir.parent / "dist/temp_whl_unpack"
    out_dir = base_dir.parent / "dist"

    # === Step 0: 自动查找唯一 .whl 文件 ===
    whls = list(out_dir.glob("*.whl"))
    if len(whls) < 1:
        print("当前目录下必须有且只有一个 .whl 文件")
        return

    original_whl = whls[-1]
    print(f"找到 whl 文件: {original_whl.name}")

    # === Step 1: 解压 .whl 到临时目录 ===
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    with zipfile.ZipFile(original_whl, 'r') as zipf:
        zipf.extractall(temp_dir)

    if not gen_pyi(temp_dir):
        return

    # === Step 2: 改路径名中的小写包名为大写 ===
    def rename_all_occurrences(root: Path, old: str, new: str):
        for dirpath, dirnames, filenames in os.walk(root, topdown=False):
            for filename in filenames:
                old_path = Path(dirpath) / filename
                if old in filename:
                    new_filename = filename.replace(old, new)
                    old_path.rename(Path(dirpath) / new_filename)
            for dirname in dirnames:
                if old in dirname:
                    old_dir = Path(dirpath) / dirname
                    new_dirname = dirname.replace(old, new)
                    old_dir.rename(Path(dirpath) / new_dirname)

        for child in root.iterdir():
            if child.is_dir() and old in child.name:
                child.rename(child.parent / child.name.replace(old, new))

    rename_all_occurrences(temp_dir, src_lower, dst_upper)
    print("路径重命名完成")

    # === Step 3: 替换 .dist-info 文件中的内容 ===
    dist_info_dir = next(temp_dir.glob(f"{dst_upper}-*.dist-info"))
    for fpath in dist_info_dir.iterdir():
        if fpath.is_file():
            try:
                text = fpath.read_text(encoding="utf-8")
                new_text = text.replace(src_lower, dst_upper)
                if new_text != text:
                    fpath.write_text(new_text, encoding="utf-8")
                    print(f"替换包名内容: {fpath.name}")
            except UnicodeDecodeError:
                print(f"跳过非文本文件: {fpath.name}")
    print(".dist-info 内容替换完成")

    # === Step 4: 重建 RECORD 文件 ===
    record_path = dist_info_dir / "RECORD"

    def hash_file(path: Path):
        h = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return "sha256=" + h.digest().hex(), str(path.stat().st_size)

    new_records = []
    for path in temp_dir.rglob("*"):
        if path.is_dir():
            continue
        rel_path = path.relative_to(temp_dir).as_posix()
        if rel_path == f"{dist_info_dir.name}/RECORD":
            new_records.append([rel_path, "", ""])
        else:
            digest, size = hash_file(path)
            new_records.append([rel_path, digest, size])

    with open(record_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(new_records)
    print("RECORD 重建完成")

    # === Step 5: 重新打包 .whl ===
    output_whl = out_dir / original_whl.name.replace(src_lower, dst_upper)
    if output_whl.exists():
        output_whl.unlink()

    with zipfile.ZipFile(output_whl, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for path in temp_dir.rglob("*"):
            if path.is_file():
                rel_path = path.relative_to(temp_dir).as_posix()
                zipf.write(path, rel_path)
    print(f"打包完成: {output_whl.name}")


if __name__ == '__main__':
    re_zip()
    # from install import install
    # install()
