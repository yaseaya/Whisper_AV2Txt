import whisper
import torch
import os

def convert_audio_to_text(input_file, output_file):
    # 检查 GPU 是否可用
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"使用设备: {device}")

    # 加载 Whisper 模型
    model = whisper.load_model("large-v3").to(device)
    
    print("正在转录音频...")
    
    # 获取绝对路径并处理可能的编码问题
    input_file_abs = os.path.abspath(input_file)
    input_file_abs = input_file_abs.encode('utf-8').decode('utf-8')
    
    # 转换音频文件
    try:
        result = model.transcribe(input_file_abs)
    except RuntimeError as e:
        print(f"转录时出错: {str(e)}")
        print(f"请检查文件路径是否正确: {input_file_abs}")
        return
    
    # 将转录文本写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result["text"])
    
    print(f"转录完成。结果已保存到 {output_file}")

if __name__ == "__main__":
    input_file = r"D:\My.Dev\WhisperJax2Txt\AV\huawei.mp3"  # 使用原始字符串
    output_file = "output.txt"  # 输出文本文件路径
    convert_audio_to_text(input_file, output_file)
