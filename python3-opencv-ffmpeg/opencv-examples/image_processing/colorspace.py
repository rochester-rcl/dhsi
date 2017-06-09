from io_parser import IOParser

# video io
from videoreader import VideoReader
from videowriter import VideoWriter

# OpenCV
import cv2

if __name__ == '__main__':
    parser = IOParser()
    reader = VideoReader(parser.input_file)
    writer = VideoWriter(parser.output_file, reader.fps, (reader.width, reader.height), color=False)

    '''
        OpenCV allows for you to easily switch between colorspaces using the cvtColor method
        Note - no video players will be able to play a single channel grayscale video so each channel, R,G,B are 
        given the same intensity values to represent grayscale.
    '''

    for frame in reader:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        '''
        if we didn't specify that our VideoWriter is grayscale, we would have to convert back to BGR to output a 
        playable version.
        '''
        # to_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        writer.write_frame(gray)

    writer.close()
    reader.close()
