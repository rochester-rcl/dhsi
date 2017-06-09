# OpenCV
import cv2

# utils
import sys
import os

# io parser

from io_parser import IOParser


class VideoReader(object):
    def __init__(self, input_file):
        self._video_cap = VideoReader.open_video(input_file)
        self.frames = int(self._video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0
        self.width = int(self._video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self._video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self._video_cap.get(cv2.CAP_PROP_FPS)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.current_frame < self.frames:
                new_frame = self.current_frame + 1
                self._video_cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
                ret, frame = self._video_cap.read()
                if ret is True:
                    self.current_frame = new_frame
                    return frame
                else:
                    print('Processed {} frames'.format(new_frame))
                    self.close()
                    raise StopIteration
            else:
                self.close()
                raise StopIteration
        except cv2.error as error:
            print(error)
            self.close()
            raise StopIteration

    def close(self):
        self._video_cap.release()

    @staticmethod
    def open_video(video_path):
        try:
            video_cap = cv2.VideoCapture(VideoReader.resolve_path(video_path))
            return video_cap
        except cv2.error as error:
            print(error)
            sys.exit()

    @staticmethod
    def resolve_path(file_path):
        return os.path.abspath(file_path)


if __name__ == '__main__':
    parser = IOParser()
    reader = VideoReader(parser.input_file)

    for frame in reader:
        # do something with frame
        print(frame.shape)
