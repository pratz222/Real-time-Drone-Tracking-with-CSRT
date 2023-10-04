import cv2

cap = cv2.VideoCapture(0) 

tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()

if not ret:
    print("Error: No Input found")
    exit()

# Select a region to track
bbox = cv2.selectROI("Object Tracking", frame, False)
tracker.init(frame, bbox)

while True:
    
    ret, frame = cap.read()

    if not ret:
        break


    ret, bbox = tracker.update(frame)

    if ret:
       
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    else:
        pass


    cv2.imshow("Object Tracking", frame)

    # Press 'e' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
