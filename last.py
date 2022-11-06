import os
import moviepy.editor as mp
from moviepy.editor import *
def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)

aud = []
dir_path = os.path.dirname(os.path.realpath(__file__))+ "/audio/"
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
            aud.append("audio/" + path)

concatenate_audio_moviepy(aud, "audio/concatenated.mp3")

dir = os.path.dirname(os.path.realpath(__file__))+ "/morph/"
allfiles = os.listdir(dir)
files = ["morph/"+fname for fname in allfiles if fname.endswith('.mp4')]
print(files)

def concatenate_video(video_clip_paths, output_path, method="compose"):
    """Concatenates several video files into one video file
    and save it to `output_path`. Note that extension (mp4, etc.) must be added to `output_path`
    `method` can be either 'compose' or 'reduce':
        `reduce`: Reduce the quality of the video to the lowest quality on the list of `video_clip_paths`.
        `compose`: type help(concatenate_videoclips) for the info"""
    clips = [VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path)

concatenate_video(files, "morph/concatenated.mp4")

audio = mp.AudioFileClip("audio/concatenated.mp3")
video1 = mp.VideoFileClip("morph/concatenated.mp4")
final = video1.set_audio(audio)
final.write_videofile("result/output.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')