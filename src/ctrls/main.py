import argparse
import time
from datetime import datetime

import keyboard


# ==========================================
# 核心业务逻辑层
# ==========================================
def run_autosave_service(interval: int):
    """
    运行带有倒计时显示的自动保存服务。
    """
    print("----------------- 自动保存工具已启动 -----------------")
    print(f"设定间隔: {interval} 秒")
    print("停止方法: Ctrl + C, 或关闭此终端窗口")
    print("----------------------------------------------------")
    print("⚠️  注意: 请务必【最小化】此终端窗口，或切换到其他软件")
    print("如果焦点在终端窗口上, Ctrl+S 会暂停程序 (终端默认行为)")
    print("----------------------------------------------------")
    print("若日志卡住不刷新了, 点击终端任意位置 (移动焦点到终端), \n按任意键即可恢复, 然后切换到别的软件 (移动焦点到终端外)")
    print("----------------------------------------------------")

    space_str = " " * 20
    
    try:
        while True:
            # 1. 倒计时循环
            # 从 interval 倒数到 1
            for remaining in range(interval, 0, -1):
                # \r : 回到当前行的开头
                # end="": 不要输出换行符
                # flush=True: 强制立即显示（防止输出被缓存）
                # 字符串末尾留几个空格，是为了覆盖掉上一轮可能留下的长字符
                print(f"\r{space_str}", end="", flush=True)
                print(f"\r⏳ 距离下次保存还有: {remaining} 秒  ", end="", flush=True)
                time.sleep(1)

            # 2. 倒计时结束，执行保存
            print("\r⏳ 正在发送保存命令... " + space_str, end="", flush=True)
            keyboard.press_and_release('ctrl+s')
            print("\r✅ 保存命令已发送!   " + space_str, end="", flush=True)

            
            # 3. 更新同一行显示“已保存”状态
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"\r✅ [{timestamp}] 触发保存成功! " + space_str, end="", flush=True)
            
            # 4. 稍微停顿一下(0.5秒)，让用户能看清"保存成功"这几个字
            # 否则瞬间就变回倒计时了
            time.sleep(0.5)
                
    except KeyboardInterrupt:
        # 捕获 Ctrl+C 后，先换一行再打印退出信息，否则会跟倒计时挤在一起
        print("\n\n程序已退出。")

# ==========================================
# 命令行接口层
# ==========================================
def parse_cli_args():
    parser = argparse.ArgumentParser(
        prog='CtrlS',
        description="带倒计时的自动保存工具 - 在后台定时发送Ctrl+S命令进行保存",
        epilog="示例: ctrls -t 30 (每30秒自动保存一次)"
    )
    
    parser.add_argument(
        '-t', '--time', 
        type=int, 
        default=60,
        help="保存间隔时间（秒），默认 60"
    )
    
    return parser.parse_args()

# ==========================================
# 入口
# ==========================================
def main():
    args = parse_cli_args()
    run_autosave_service(args.time)


if __name__ == "__main__":
    main()