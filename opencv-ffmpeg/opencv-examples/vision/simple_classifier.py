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
        Although we don't have a large dataset to work with for classifying features in an image, 
        we can attempt to detect a known image in our video.
        
        We use the SIFT (Scale-Invariant Feature Transform) to find keypoints in the image (i.e. what makes the image
        "interesting" or distinctive) that can be found whether or not the image has been transformed (rotated, scaled, etc...)
        
        SIFT also comes up with descriptors for these keypoints, which describe certain aspects that make them unique, 
        such as scale and orientation. 
        
        Once we collect all of our keypoints with descriptors, we put store them in a data structure that allows us to do 
        nearest neighbor searches. In this case we'll use FLANN (Fast Library for Approximate Nearest Features).
        
        Finally, we'll set a minimum value for nearest-neighbor matches. If we're above it, we'll say we've detected something
        and draw a box around it.
    
    '''

    MIN_MATCHES = 10
    src_img = cv2.imread('/home/shared/opencv-examples/files/halls_region.png', 0)
    sift = cv2.xfeatures2d.SIFT_create()

    keypoints_src, descriptors_src = sift.detectAndCompute(src_img, None)

    index_params = {'algorithm': 0, 'trees': 5}
    search_params = {'checks': 50}

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    for frame in reader:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # we could also draw keypoints
        # kp_img = None
        detected_text = 'Not Halls'
        keypoints_query, descriptors_query = sift.detectAndCompute(gray, None)
        # need to make sure we actually have descriptors, if not it will return None

        if type(descriptors_query) is np.ndarray:
            matches = flann.knnMatch(descriptors_src, descriptors_query, k=2)
            good_matches = []
            for match, neighbor in matches:
                if match.distance < 0.7 * neighbor.distance:
                    good_matches.append(match)

            if len(good_matches) > MIN_MATCHES:
                good_points = [keypoints_query[gm.queryIdx] for gm in good_matches]
                detected_text = "Halls"
                # kp_img = cv2.drawKeypoints(frame, good_points, color=(0,255,0))

        # text is 10px from the left and 50px from the bottom. Scale is 1, color is white, and line thickness is 3
        cv2.putText(frame, detected_text, (10, reader.height - 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3,
                    cv2.LINE_AA)
        writer.write_frame(frame)
    '''
     if kp_img is not None:
         writer.write_frame(kp_img)
     else:
         writer.write_frame(frame)
    '''

    writer.close()
    reader.close()
