import whisper
import torch
import os
import subprocess

def extract_audio_from_video(video_file, audio_file):
    # 使用 ffmpeg 提取音频
    command = [
        'ffmpeg',
        '-i', video_file,
        '-q:a', '0',
        '-map', 'a',
        audio_file
    ]
    subprocess.run(command, check=True)

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
    
    audio_file = None  # 初始化音频文件变量

    # 如果输入文件是视频文件，提取音频
    if input_file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
        audio_file = "extracted_audio.wav"  # 提取的音频文件名
        extract_audio_from_video(input_file_abs, audio_file)
        input_file_abs = audio_file  # 更新为提取的音频文件
    
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

    # 删除提取的音频文件（如果存在）
    if audio_file and os.path.exists(audio_file):
        os.remove(audio_file)
        print(f"已删除临时音频文件: {audio_file}")

if __name__ == "__main__":
    input_file = r"D:\My.Dev\WhisperJax2Txt\AV\fly.mp4"  # 输入文件路径，可以是音频或视频文件
    output_file = "output.txt"  # 输出文本文件路径
    convert_audio_to_text(input_file, output_file)
