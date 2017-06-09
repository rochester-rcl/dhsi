from io_parser import IOParser

# video io
from videoreader import VideoReader
from videowriter import VideoWriter

# OpenCV
import cv2

import numpy as np

if __name__ == '__main__':
    parser = IOParser()
    reader = VideoReader(parser.input_file)
    writer = VideoWriter(parser.output_file, reader.fps, (reader.width, reader.height))

    '''
        Because the Python bindings for OpenCV use numpy matrices to store pixel data we can use a lot of convenient 
        numpy methods such as array indexing
    '''

    MAX = 100
    MIN = 80

    def clip_intensity(intensity):
        if intensity > MAX:
            return MAX

        if intensity < MIN:
            return MIN

        return intensity

    for frame in reader:
        ''' 
            for instance, we can set a whole channel to a specific value. i.e. all blue values become 50
            frame[:, :, 0] = 50
            
            Or we can do something more sophisticated like apply a function to all intensity values in a channel using
            np.vectorize 
        '''
        # note - this is horribly inefficient
        clip = np.vectorize(clip_intensity)
        blue_intensity = frame[:, :, 0]
        green_intensity = frame[:, :, 1]
        red_intensity = frame[:, :, 2]
        frame[:, :, 0] = clip(blue_intensity)
        frame[:, :, 1] = clip(green_intensity)
        frame[:, :, 2] = clip(red_intensity)
        writer.write_frame(frame)

    writer.close()
    reader.close()
