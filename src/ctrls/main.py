import keyboard
import time

# 这是一个死循环脚本，用于持续运行
# 如果打包时使用了无窗口模式(-w)，需要在任务管理器中结束进程来停止

def run_loop(interval):
    while True:
        # 等待指定秒数
        time.sleep(interval)
        
        # 发送组合键
        keyboard.send('ctrl+s')
        
        # 可选：为了调试，可以把日志写到文件，因为打包后看不到控制台
        # with open("log.txt", "a") as f:
        #     f.write(f"Saved at {time.ctime()}\n")

if __name__ == "__main__":
    # 间隔时间 60 秒
    INTERVAL = 3
    
    # 防止多重运行（简单的逻辑）
    print(f"自动保存脚本运行中... 每 {INTERVAL} 秒触发一次 Ctrl+S")
    
    run_loop(INTERVAL)