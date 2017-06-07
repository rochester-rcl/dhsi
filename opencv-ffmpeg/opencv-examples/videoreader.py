# OpenCV
import cv2

# utils
import sys
import os

# argparse
import argparse


class VideoReader(object):
    def __init__(self, input_file):
        self._video_cap = VideoReader.open_video(input_file)
        self.frames = int(self._video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_frame < self.frames:
            new_frame = self.current_frame + 1
            self._video_cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
            ret, frame = self._video_cap.read()
            if ret is True:
                self.current_frame = new_frame
                return frame
            else:
                print('There was an error processing frame {}'.format(new_frame))
                StopIteration()
        else:
            StopIteration()

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
    parser = argparse.ArgumentParser(
        description="Test that the reader works")
    parser.add_argument('-i', '--input_file', help="input video file", required="true",
                        type=str)

    args = vars(parser.parse_args())
    input_file = args['input_file']
    reader = VideoReader(input_file)

    for frame in reader:
        # do something with frame
        print(frame.shape)
