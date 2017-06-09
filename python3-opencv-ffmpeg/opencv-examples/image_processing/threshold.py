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
        Thresholding, or "binarization" operations are important for simplifying images in order to do analysis on them -
        for instance in OCR 
    '''

    for frame in reader:
        # we need to pass a grayscale matrix to the threshold function
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # if a pixel value is above 200, make it white - otherwise make it black
        ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        writer.write_frame(thresh)

    writer.close()
    reader.close()