import cv2
import time

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

bbox = cv2.selectROI("Select Object", frame, False)

cv2.destroyWindow("Select Object")

tracker = cv2.TrackerCSRT_create()

tracker.init(frame, bbox)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    start = time.time()

    success, bbox = tracker.update(frame)

    if success:

        x, y, w, h = [int(i) for i in bbox]

        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      (0,255,0),
                      3)

        cv2.putText(frame,
                    "Tracking",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2)

    else:

        cv2.putText(frame,
                    "Object Lost",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2)

    fps = 1/(time.time()-start)

    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,0,0),
                2)

    cv2.imshow("Object Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()