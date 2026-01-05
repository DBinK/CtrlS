import subprocess
import sys
from pathlib import Path
import platform

def build_with_nuitka():
    """使用 Nuitka 打包应用"""
    cmd = [
        sys.executable, "-m", "nuitka",
        "--onefile",
    ]
    
    # 根据平台添加编译器参数
    if platform.system() == "Windows":
        cmd.append("--mingw64")  # Windows 使用 MinGW64 编译器
    
    cmd.extend([
        "--windows-console-mode=force",  # Windows 特定选项
        "--include-package=keyboard",
        "--output-dir=dist",
        "--output-filename=ctrls.exe",  # Windows 上添加 .exe 扩展名
        "src/ctrls/main.py"
    ])
    
    # 确保 dist 目录存在
    Path("dist").mkdir(exist_ok=True)
    
    print("执行命令:", " ".join(cmd))
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("打包成功！")
    else:
        print("打包失败！")
        print("\n可能的解决方案:")
        print("1. 确保已安装 Microsoft C++ Build Tools 或 Visual Studio")
        print("2. 尝试使用 --mingw64 参数: python -m nuitka --onefile --mingw64 ...")
        print("3. 检查是否安装了正确的编译器工具链")

if __name__ == "__main__":
    build_with_nuitka()