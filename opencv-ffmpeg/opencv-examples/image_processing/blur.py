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

    ''' 
        many image processing operations involve 'convolution', where a small matrix is applied to all pixels 
        in a frame and acts as a filter. For an excellent example, look here: http://setosa.io/ev/image-kernels/
        try to experiment with the kernel size and see what kind of output you get. 
        
        a 3x3 kernel looks like this 
          _____
         |1 1 1|   
         |1 1 1|  
         |1 1 1|  
          -----
        to perform a simple blur, you would multiple every element in the 3x3 kernel by 1/9 and set
        the center pixel (the anchor) to that value
    '''
    # the data type can be anything you want, but a 32 bit float allows for more precision
    kernel = np.ones((3, 3), dtype=np.float32)/9

    for frame in reader:
        ''' here we use the cv2.filter2D method to do the convolution. the -1 parameter specifies that the depth of the 
            destination array is the same as the source (HxWx3)
        '''
        blurred = cv2.filter2D(frame, -1, kernel)
        writer.write_frame(blurred)

    writer.close()
    reader.close()


