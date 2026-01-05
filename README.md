# CtrlS - 自动保存工具

一个简单实用的自动保存工具，能够在后台定时发送 `Ctrl+S` 快捷键命令，帮助您自动保存当前工作内容，防止因意外情况导致的工作丢失。

## 功能特性

- **定时自动保存**：可自定义保存间隔时间，定时发送 `Ctrl+S` 保存命令
- **倒计时显示**：实时显示距离下次保存的倒计时
- **状态反馈**：保存成功后显示时间戳，便于确认操作执行
- **用户友好**：提供清晰的使用提示和停止方法

## 安装

### 方法一：直接使用编译好的可执行文件

从 [GitHub releases](https://github.com/DBinK/CtrlS/releases) 下载可执行文件

然后就可以从命令行中运行了, 例如：

```pwsh
./ctrls.exe -t 60
```

### 方法二：使用 uv tool (推荐)

若没有安装 uv , 可使用这个脚本安装

<details>
<summary>点击展开安装命令</summary>

```bash
curl -LsSf https://gitee.com/wangnov/uv-custom/releases/download/latest/uv-installer-custom.sh | sh  # 适用于 Linux
```

```pwsh
powershell -ExecutionPolicy Bypass -c "irm https://gitee.com/wangnov/uv-custom/releases/download/latest/uv-installer-custom.ps1 | iex"  # 适用于 Windows
```

</details>

使用 uv tool 方式 (推荐使用): 

```bash
uv tool install git+https://github.com/DBinK/CtrlS.git
```

### 方法三：使用 pipx

使用 pipx 方式:

```bash
pipx install git+https://github.com/DBinK/CtrlS.git
```

## 使用方法

### 作为命令行工具运行

```bash
# 使用默认间隔时间（60秒）
ctrls

# 指定保存间隔时间（例如：45秒）
ctrls -t 45
```

参数说明：
- `-t` 或 `--time`：设置保存间隔时间（单位：秒），默认值为60

## 构建可执行文件

项目提供了构建脚本，可以使用 Nuitka 将项目打包为可执行文件：

```bash
# 确保已安装 Nuitka
pip install nuitka

# 运行构建脚本
python build.py
```

构建成功后，可执行文件将位于 `dist` 目录下。

## 注意事项

⚠️ **重要提示**：
1. 请在使用时将终端窗口**最小化**，或切换到其他软件界面，否则 `Ctrl+S` 可能会影响终端
2. 如果焦点在终端窗口上，`Ctrl+S` 会暂停程序（按 `Ctrl+Q` 恢复）
3. 如需停止程序，可按 `Ctrl+C` 或直接关闭终端窗口

## 工作原理

项目使用 `keyboard` 库模拟 `Ctrl+S` 快捷键，通过定时器机制在后台周期性地执行保存操作。主循环包含一个倒计时功能，可以让用户了解下次保存的时间。

## 依赖库

- [keyboard](https://github.com/boppreh/keyboard)：用于模拟键盘事件
- [nuitka](https://nuitka.net/)：用于将 Python 代码编译为可执行文件

## 适用场景

- 长时间编辑文档、代码时防止意外丢失
- 需要定时保存工作状态的场景
- 避免忘记手动保存的习惯
 