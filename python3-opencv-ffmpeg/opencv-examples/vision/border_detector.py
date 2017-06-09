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
        We can use either thresholding or edge detection to simplify our frames and use cv2.findContours 
        to find all of the contours in our image. We can then sort them by size and do some additional processing to
        try to find specific polygons or shapes within the frame.
        
    '''
    for frame in reader:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        mod_img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # grab the 3 largest contour areas
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[0:2]

        for contour in sorted_contours:
            epsilon = 0.1*cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) == 4:
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
                break
        writer.write_frame(frame)

    writer.close()
    reader.close()


