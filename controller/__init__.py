import os
import ffmpeg

OUTPUT_FOLDER = "./outputs"

if not os.path.exists(OUTPUT_FOLDER) :
    os.makedirs(OUTPUT_FOLDER)

def convert_video(input_video_path, output_format) :
    output_video_path = os.path.join(OUTPUT_FOLDER, os.path.splitext(os.path.split(os.path.abspath(input_video_path))[-1])[0] + '.' + output_format)
    stream = ffmpeg.input(input_video_path)
    stream = ffmpeg.output(stream, output_video_path)
    ffmpeg.run(stream)
    return output_video_path