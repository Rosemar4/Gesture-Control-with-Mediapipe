import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release and cleanup
cap.release()
cv2.destroyAllWindows()
