import os
import re
import shutil
from copy import deepcopy

files = os.listdir()


def load_videos(files):
    patterns = re.compile(r"^.*(\.mkv)|(\.mp4)|(\.avi)|(\.mov)$")
    videos = [file for file in files if re.findall(patterns, file)]
    videos_copy = deepcopy(videos)
    for video in videos_copy:
        if re.search('OP|ED|PV', video):
            videos.remove(video)
    return videos


def load_subtitles(files):
    patterns = re.compile(r"^.*(\.ssa)|(\.ass)|(\.srt)|(\.smi)$")
    subtitles = [file for file in files if re.findall(patterns, file)]
    return subtitles


def converter():
    videos = load_videos(files)
    videos = sorted(videos)
    subtitles = load_subtitles(files)
    subtitles = sorted(subtitles)

    for i in range(len(videos)):
        # print(videos[i])
        # print(subtitles[i])
        # print('')
        video = videos[i]
        episode = video.rsplit('.', 1)[0]
        subtitle = subtitles[i]
        subtitle_ext = subtitle.rsplit('.', 1)[1]
        new_subtitle = episode + '.' + subtitle_ext
        # print(subtitle)
        # print(new_subtitle)
        shutil.copyfile(subtitle, new_subtitle)


if __name__ == '__main__':
    converter()
