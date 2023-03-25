
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


#这些错误提示都是Python中缺少相关模块的错误。您需要使用命令行或终端进入电脑，运行以下命令来安装缺失的模块：
#1. 安装moviepy模块：`pip install moviepy`
#2. 安装pandas模块：`pip install pandas`
#3. 安装openpyxl模块：`pip install openpyxl`
#安装完后，测试代码应该可以正常执行了。
