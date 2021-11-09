import cv2
from datetime import datetime

def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        windowName_2 = "Sample Feed from Camera 2"
        windowName_3 = "Sample Feed from Camera 3"
        # cv2.namedWindow(windowName)

        # capture1 = cv2.VideoCapture(0)  # laptop's camera
        capture1 = cv2.VideoCapture("http://192.168.230.36:8080/video")
        capture2 = cv2.VideoCapture("http://192.168.230.220:8080/video")   # sample code for mobile camera video capture using IP camera
        capture3 = cv2.VideoCapture("http://192.168.230.74:8080/video")

        # define size for recorded video frame for video 1
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        # define size for recorded video frame for video 2
        width2 = int(capture1.get(3))
        height2 = int(capture1.get(4))
        size2 = (width2, height2)

        # define size for recorded video frame for video 3
        width3 = int(capture1.get(3))
        height3 = int(capture1.get(4))
        size3 = (width3, height3)

        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

        # frame of size is being created and stored in .avi file
        optputFile2 = cv2.VideoWriter(
            'Stream2Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size2)

        # frame of size is being created and stored in .avi file
        optputFile3 = cv2.VideoWriter(
            'Stream3Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size2)

        # check if feed exists or not for camera 1 and camera 2 and camera 3
        if capture1.isOpened() and capture2.isOpened():
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()
        else:
            ret1 = False
            ret2 = False
            ret3 = False

        while ret1 and ret2:
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()

            cv2.putText(frame1,str(datetime.now()), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, .5,(255,255,255),2,cv2.LINE_AA)
            frameshow1 = cv2.resize(frame1, (640, 360), interpolation = cv2.INTER_AREA)
            cv2.imshow(windowName, frameshow1)

            cv2.putText(frame2,str(datetime.now()), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, .5,(255,255,255),2,cv2.LINE_AA)
            frameshow2 = cv2.resize(frame2, (640, 360), interpolation = cv2.INTER_AREA)
            cv2.imshow(windowName_2, frameshow2)

            cv2.putText(frame3,str(datetime.now()), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, .5,(255,255,255),2,cv2.LINE_AA)
            frameshow3 = cv2.resize(frame3, (640, 360), interpolation = cv2.INTER_AREA)
            cv2.imshow(windowName_3, frameshow3)

            # saves the frame from camera 1, 2 and 3
            optputFile1.write(frame1)
            optputFile2.write(frame2)
            optputFile2.write(frame3)

            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        optputFile1.release()
        capture2.release()
        optputFile2.release()
        capture3.release()
        optputFile3.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        windowName2 = "Live Stream Camera 2"
        windowName2 = "Live Stream Camera 3"
        # cv2.namedWindow(windowName1)

        # capture1 = cv2.VideoCapture(0)
        capture1 = cv2.VideoCapture("http://192.168.230.36:8080/video")
        capture2 = cv2.VideoCapture("http://192.168.230.220:8080/video")
        capture2 = cv2.VideoCapture("http://192.168.230.74:8080/video")

        if capture1.isOpened() and capture2.isOpened() and capture3.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()
        else:
            ret1 = False
            ret2 = False
            ret3 = False

        while ret1 and ret2 and ret3:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)
            ret2, frame2 = capture2.read()
            cv2.imshow(windowName2, frame2)
            ret3, frame3 = capture2.read()
            cv2.imshow(windowName3, frame3)

            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")

main()
