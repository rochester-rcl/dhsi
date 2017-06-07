# OpenCV
import cv2

# utils
import sys
import os

# easy io parser
from io_parser import IOParser

# video io
from videoreader import VideoReader


class VideoWriter(object):
    # just an example of how we can map containers to preset codecs
    FOURCC_MAP = {
        '.mp4': 'X264',
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
    parser = IOParser()
    reader = VideoReader(parser.input_file)
    writer = VideoWriter(parser.output_file, reader.fps, (reader.width, reader.height))

    for frame in reader:
        writer.write_frame(frame)
    writer.close()
    reader.close()
