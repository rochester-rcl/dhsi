from io_parser import IOParser

# video io
from videoreader import VideoReader
from videowriter import VideoWriter

# OpenCV
import cv2

# numpy
import numpy as np

# math
import math

if __name__ == '__main__':
    parser = IOParser()
    reader = VideoReader(parser.input_file)
    writer = VideoWriter(parser.output_file, reader.fps, (reader.width, reader.height))

    # initialize an array WxHx1 to act as a placeholder for the other 2 channels
    black_channel = np.zeros((reader.height, reader.width), dtype=np.uint8)  # unsigned 8-bit integer
    slice_size = math.ceil(reader.width / 4)

    for frame in reader:
        # by default OpenCV arranges its matrices in BGR colorspace
        b, g, r = cv2.split(frame)
        output_red = cv2.merge([black_channel, black_channel, r])
        output_green = cv2.merge([black_channel, g, black_channel])
        output_blue = cv2.merge([b, black_channel, black_channel])

        # using numpy array indexing, we can swap sections of the original frame with our processed ones
        # frame[:(keep the height dimension the same), slice_start:slice_end]
        frame[:, slice_size:slice_size*2] = output_red[:, slice_size:slice_size*2]
        frame[:, slice_size*2:slice_size*3] = output_green[:, slice_size*2:slice_size*3]
        frame[:, slice_size*3:slice_size*4] = output_blue[:, slice_size*3:slice_size*4]
        writer.write_frame(frame)

    writer.close()
    reader.close()




