from moviepy.editor import *

clip = VideoFileClip("myvideo.mp4").subclip(20, 45)

# clip = clip.volumex(0.8)
#
# txt_clip = TextClip("My holidays 2019", fontsize=70, color='white')
#
# txt_clip = txt_clip.set_position('center').set_duration(10)

video = CompositeVideoClip([clip])

video.write_videofile("my_new1.mp4")

