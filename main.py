import cv2
import trackpy as tp

# Create a VideoCapture object to read from the video file
cap = cv2.VideoCapture("C:/Users/Owner/Downloads/Kennedy.mp4")

# Set the video resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the region of interest (ROI) where the barbell will be tracked
roi = (500, 0, 500, 700)

# Define the parameters for locate()
minmass = 500
maxsize = 500

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    # crop the frame with the region of interest
    frame = frame[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
    radius = 100
    # Use trackpy to locate the barbell in the frame
    f = tp.locate(frame, minmass=minmass, maxsize=maxsize, invert=False,
                  preprocess=False, diameter = 25)

    # Iterate through the particles and draw a circle around the barbell
    for index, particle in f.iterrows():
        x, y = particle.x+roi[0], particle.y+roi[1]
        cv2.circle(frame, (x, y), radius, (0, 255, 0), 1)

    # Display the frame
    cv2.imshow("Tracking", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
