# Python-BadApple
Python实现BadApple字符动画

运行该程序需要的第三方库有：PIL、numpy，可以通过 pip 安装。其中 getImage.py 用于从视频中获取帧图像，采样间隔可调整，借助了终端命令 ffmpeg，可以使用 Homebrew 直接安装。

若下载完整的包，将 play.py 中 getTxt(img_dir_path, txt_dir_path) 注释掉直接运行 play.py 即可。

注意，终端大小至少需要300x75，如果无法满足该大小，调整 image2txt.py 中的 charWidth 值为终端每行支持的字符数，不注释 play.py 中的 getTxt(img_dir_path, txt_dir_path) ，运行 play.py 稍等片刻即可。当然 charWidth 值越小转化效果越差。但 charWidth 过大终端会出现屏幕闪烁现象。
