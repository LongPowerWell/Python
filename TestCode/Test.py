
import os
import glob
from moviepy.editor import AudioFileClip
import pandas as pd

# 指定目录路径
path = r'E:\newnew8848\新媒体工作室\BaiduNetdiskDownload'

# 查找所有音频文件
audio_files = glob.glob(os.path.join(path, '*.mp3'))

# 遍历所有音频文件，获取名称、大小和长度信息
audio_info = []
for file in audio_files:
    name = os.path.basename(file)
    size = os.path.getsize(file)
    with AudioFileClip(file) as audio:
        duration = audio.duration
    audio_info.append((name, size, duration))

# 将结果保存到Excel文件中
df = pd.DataFrame(audio_info, columns=['Name', 'Size', 'Duration'])
df.to_excel('audio_info.xlsx', index=False)
