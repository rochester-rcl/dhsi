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
        OpenCV 3 offers a high-level tracking API that features several tracking algorithms you can experiment with.
        For now we'll use the Kernelized Correlation Filters tracker (KCF), which uses a Bag of Features (like Bag of Words)
        approach to define positive and negative 'patches' to differentiate between the foreground and background. This 
        is used to set up the Appearance Model of our tracker (how our tracked region looks) as well as the Motion Model 
        a predictive estimation of where the object will be based on its velocity and location in previous frames.
        
    '''
    # initialize the tracker
    tracker = cv2.Tracker_create('KCF')

    # bounding boxes are represented as x, y, w, h
    bounding_box = (400, 230, 30, 40)

    # read in first frame of video using our generator
    frame1 = reader.__next__()
    tracker.init(frame1, bounding_box)

    for frame in reader:
        ret, bounding_box = tracker.update(frame)
        if ret:
            '''
                to draw a rectangle, we have to specify 2 points one vertex representing the top left of the rectangle,
                and one representing the bottom right (opposite) vertex
                
            '''
            # x, y
            point1 = (int(bounding_box[0]), int(bounding_box[1]))
            # x + w, y + h
            point2 = (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3]))
            cv2.rectangle(frame, point1, point2, (0, 255, 0))

        writer.write_frame(frame)
    writer.close()
    reader.close()

