from moviepy.editor import *


class Video:
    def video_clip(self, videopath, start, end, rename, ext):

        clip = VideoFileClip(videopath).subclip(start, end)

        video = CompositeVideoClip([clip])

        new_video = rename + '.' + ext

        video.write_videofile(new_video)

        return new_video


video = Video()

res = video.video_clip("video2.mp4", 10, 400, "clip/className1", "mp4")


print(res)
