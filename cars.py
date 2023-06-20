import time
import numpy as np
import cv2
from ultralytics import YOLO
from keras.models import load_model
import tensorflow as tf



print("started")
model = YOLO('yolov8n.pt')
print("loaded Yolo")




cap = cv2.VideoCapture(
    r"C:\Users\Msk basha\Documents\D drive\Projects\Cars Project\30 Minutes of Cars Driving By in 2009_3.mp4")
distance_model = load_model(
    r"Model__ 31-3-2023 _ trained on 3000 8000 1000 y_out.h5")
print("loaded Distance model")



frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count = 0
bt = time.time()
lis = []
prev = 0
for i in range(1000):
    count += 1
    # Read a frame from the video stream
    ret, frame = cap.read()
    if count % 3 != 0:
        continue
    images = []
    coordinates = []
    coordinates_in_pixels = []
    for i in model.predict(frame, verbose=False)[0].boxes.data:
        l = np.array(list((map(int, i))))
        if l[-1] == 2:
            # frame = cv2.rectangle(frame, [l[0], l[1]], [l[2], l[3]], 2)
            img = np.array(tf.image.resize(
                frame[l[1]:l[3], l[0]:l[2]], (80, 120)), dtype='uint8')
            k = np.array(l[:-2]/np.array([1280, 720, 1280, 720]))
            images.append(img)
            coordinates.append(k)
            coordinates_in_pixels.append(l)
    dist = distance_model.predict([np.array(images),
                                   np.array(coordinates)], verbose=False)
    # img = np.zeros((500, 500, 3), np.uint8)
    # for i in range(len(coordinates)):
    #     val = dist[i]-44
    #     cv2.circle(img, (int(val[0])*10+30, int(val[1])
    #                * 10+30), 1, (0, 0, 255), -1)

    def edit_string(string):
        return str(string)[:4]
    for k in range(len(coordinates)):
        l = coordinates_in_pixels[k]
        # print(dist[i])
        # val = list(map(int, dist[k]-44))
        # val = list(map(edit_string, val))
        val = 1000/dist[k][0]-4
        cv2.putText(frame, str(val)[:4]+' m', (l[0], l[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 1)

    cv2.imshow(" ", frame)
    # # If there was an error reading the frame, break out of the loop
    if not ret:
        break
    # Display the frame

    # Wait for a key press and check if the 'q' key was pressed
    if cv2.waitKey(1) == ord('q'):
        break
print(' Time spent ', time.time()-bt)
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
