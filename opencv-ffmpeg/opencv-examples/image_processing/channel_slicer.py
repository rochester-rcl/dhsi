import sys
sys.path.append('../')

from video_io.io_parser import IOParser

# video io
from io import videoreader
from io import videowriter

# OpenCV
import cv2

# numpy
import numpy as np

if __name__ == '__main__':
    parser = io_parser.IOParser()
    reader = videoreader.VideoReader(parser.input_file)
    writer = videowriter.VideoWriter(parser.output_file)

    # initialize an array WxHx1 to act as a placeholder for the other 2 channels
    black_channel = np.zeros((reader.height, reader.width), dytpe=np.uint8) #unsigned 8-bit integers

    for frame in reader:
        # by default OpenCV arranges its matrices in BGR colorspace
        b, g, r = cv2.split(frame)
        output_red = cv2.merge(black_channel, black_channel, r)
        writer.write(output_red)




