import cv2
import numpy as np
import os

def main():
    path = os.path.join(os.getcwd(), "robot.jpg")
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def trackbar_handler(a):
        pass

    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 1024, 768)
    cv2.createTrackbar("Hue Min","Trackbars", 0, 179, trackbar_handler)
    cv2.createTrackbar("Hue Max","Trackbars", 179, 179, trackbar_handler)
    cv2.createTrackbar("Sat Min","Trackbars", 0, 255, trackbar_handler)
    cv2.createTrackbar("Sat Max","Trackbars", 255, 255, trackbar_handler)
    cv2.createTrackbar("Val Min","Trackbars", 0, 255, trackbar_handler)
    cv2.createTrackbar("Val Max","Trackbars", 255, 255, trackbar_handler)

    while True:
        # cv2.imshow("imgHSV", imgHSV)
        h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
        h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
        s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
        s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
        v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
        v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        # initial values
        # 0 179 0 110 42 255
        lower = np.array([0, 0, 42])
        upper = np.array([179, 110, 255])
        mask = cv2.inRange(imgHSV, lower, upper)
        # 0 179 0 255 0 96
        imgResult = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", imgResult)
        cv2.imwrite(os.path.join(os.getcwd(), 'res', 'robot_mask.jpg'), mask)
        cv2.imwrite(os.path.join(os.getcwd(), 'res', 'robot_result.jpg'), imgResult)
        cv2.waitKey(1)

if __name__ == "__main__":
	main()
