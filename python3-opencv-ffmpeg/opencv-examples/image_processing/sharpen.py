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

    ''' See 'blur.py' for an explanation of kernels. Below is an example of how you can create a custom kernel.
        You can play around with the numbers and see what you get.
    '''

    sharpen_kernel = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ), dtype=np.float32)

    for frame in reader:
        sharpened = cv2.filter2D(frame, -1, sharpen_kernel)
        writer.write_frame(sharpened)

    writer.close()
    reader.close()