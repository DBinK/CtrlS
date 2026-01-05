import subprocess
import sys
from pathlib import Path

def build_with_nuitka():
    """使用 Nuitka 打包应用"""
    cmd = [
        sys.executable, "-m", "nuitka",
        "--onefile",
        "--include-package=keyboard",
        "--output-dir=dist",
        "--output-filename=ctrls",
        "src/ctrls/main.py"
    ]
    
    # 确保 dist 目录存在
    Path("dist").mkdir(exist_ok=True)
    
    print("执行命令:", " ".join(cmd))
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("打包成功！")
    else:
        print("打包失败！")

if __name__ == "__main__":
    build_with_nuitka()