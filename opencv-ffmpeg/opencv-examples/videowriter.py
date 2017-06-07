# OpenCV
import cv2

# utils
import sys
import os

# argparse
import argparse

from videoreader import VideoReader


class VideoWriter(object):
    # just an example of how we can map containers to preset codecs
    FOURCC_MAP = {
        '.mp4': 'DIVX',
        '.mkv': 'X264',
        '.mov': 'H264',
    }

    def __init__(self, output_path, fps, resolution):
        self.output_path = VideoWriter.resolve_path(output_path)
        self.codec = VideoWriter.map_fourcc(output_path)
        self.resolution = resolution
        self.fps = fps
        self._writer = cv2.VideoWriter(self.output_path, self.codec, self.fps, self.resolution)

    def write_frame(self, frame):
        self._writer.write(frame)

    def close(self):
        self._writer.release()

    @staticmethod
    def map_fourcc(file_path):
        try:
            pathname, ext = os.path.splitext(file_path)
            return cv2.VideoWriter_fourcc(*VideoWriter.FOURCC_MAP[ext])
        except KeyError:
            print("No codecs found for extension {}. Quitting".format(ext))
            sys.exit()

    @staticmethod
    def resolve_path(file_path):
        return os.path.abspath(file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test that the reader works")
    parser.add_argument('-i', '--input_file', help="input video file path", required="true", type=str)
    parser.add_argument('-o', '--output_file', help="output video file path", required="true", type=str)

    args = vars(parser.parse_args())
    input_file = args['input_file']
    output_path = args['output_file']

    reader = VideoReader(input_file)
    writer = VideoWriter(output_path, 24.0, (320, 240))

    for frame in reader:
        writer.write_frame(frame)
    writer.close()
    reader.close()
