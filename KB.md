创建虚拟环境
1. 打开 VSCode：
启动 Visual Studio Code。
2. 打开终端：
您可以通过菜单栏选择 Terminal -> New Terminal，或者使用快捷键 Ctrl + 打开终端。
3. **创建虚拟环境**： 在终端中，使用以下命令创建虚拟环境（假设您使用的是 Python 3）： bash
python -m venv venv
   这将创建一个名为 `venv` 的虚拟环境文件夹。

4. **激活虚拟环境**：
   - **在 Windows 上**：
     ```bash
     venv\Scripts\activate
     ```
   - **在 macOS 或 Linux 上**：
     ```bash
     source venv/bin/activate
     ```

   激活后，您会看到终端提示符前面出现 `(venv)`，表示虚拟环境已激活。

### 安装依赖项

在虚拟环境激活后，您可以安装所需的依赖项，例如 WhisperJax 和 PyTorch：


pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Looking in indexes: https://download.pytorch.org/whl/cu118



### 配置 VSCode 使用虚拟环境

1. **选择 Python 解释器**：
   按下 `Ctrl + Shift + P` 打开命令面板，输入并选择 `Python: Select Interpreter`。然后选择您刚刚创建的虚拟环境的 Python 解释器。

2. **运行代码**：
   现在，您可以在 VSCode 中运行您的 Python 代码，确保它使用的是虚拟环境中的依赖项。

### 退出虚拟环境

完成工作后，您可以通过以下命令退出虚拟环境：



这样，您就成功在 VSCode 中创建并使用了虚拟环境。
