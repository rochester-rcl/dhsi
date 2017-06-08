from io_parser import IOParser

# video io
from videoreader import VideoReader
from videowriter import VideoWriter

# OpenCV
import cv2

# numpy
import numpy as np

if __name__ == '__main__':
    parser = IOParser()
    reader = VideoReader(parser.input_file)
    writer = VideoWriter(parser.output_file, reader.fps, (reader.width, reader.height))

    # initialize an array WxHx1 to act as a placeholder for the other 2 channels
    black_channel = np.zeros((reader.height, reader.width), dtype=np.uint8) #unsigned 8-bit integers

    for frame in reader:
        # by default OpenCV arranges its matrices in BGR colorspace
        b, g, r = cv2.split(frame)
        output_red = cv2.merge([black_channel, black_channel, r])
        writer.write_frame(output_red)




