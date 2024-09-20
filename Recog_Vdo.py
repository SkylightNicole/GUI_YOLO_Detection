from ultralytics import YOLO
import cv2
import easyocr
import threading

last_detection = None
text_detection = None
frame_to_process = None
lock = threading.Lock()
text_lock = threading.Lock()
stop_thread = False
run = 0
frame = None
text = None

def get_current_frame():
    global frame
    if frame is not None:
        return frame.copy()
    return None
def get_current_text():
    global text
    if text is not None:
        return text.copy()
    return None

def detect_plate():
    """For Plate Detection with Multithread"""
    model = YOLO("best.pt")
    global last_detection , frame_to_process , stop_thread
    frame = None
    while not stop_thread:
        with lock:
            if frame_to_process is not None:
                frame = frame_to_process.copy()
                frame_to_process = None
            else:
                continue
        if frame is not None:
            detections = model(frame)[0]
            detections_ = []
            for detection in detections.boxes.data.tolist():
                x1,y1,x2,y2,score,class_id = detection
                detections_.append([x1,y1,x2,y2,score,class_id])

            if len(detections_) > 0:
                x1, y1, x2, y2, score, class_id = detections_[0]
                last_detection = (int(x1), int(y1), int(x2), int(y2))

def detect_text():
    """For Text Reading from Cropped Frame with Multithread"""
    global text_detection , stop_thread , text
    crop_frame = None
    reader = easyocr.Reader(["en"],gpu=True)
    while not stop_thread:
        with text_lock:
            if text_detection is not None:
                crop_frame = text_detection.copy()
                text_detection = None
        if crop_frame is not None and crop_frame.size > 0:
            text = reader.readtext(crop_frame,detail=0)


def detect_video():
    """To Actually Process the Video In Realtime"""
    global frame_to_process , text_detection , frame , last_detection
    while not stop_thread:
        with lock:
            if frame is not None:
                frame_to_process = frame.copy()
        with lock:
            if last_detection is not None and frame is not None:
                x1, y1, x2, y2 = last_detection
                reading = frame[y1:y2,x1:x2].copy()
                with text_lock:
                    text_detection = reading
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


def resize_frame(frame, width=None, height=None):
    '''Resize the frame to a new width or height while maintaining aspect ratio.'''
    if frame is not None:
        (h, w) = frame.shape[:2]
        
        if width is None and height is None:
            return frame

        if width is not None:
            ratio = width / float(w)
            dim = (width, int(h * ratio))
        else:
            ratio = height / float(h)
            dim = (int(w * ratio), height)

        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        return resized

def recognized():
    global stop_thread , run , frame
    stop_thread = False
    video = cv2.VideoCapture("D:\\DarkSky\\GUI_YOLO_Detection-main\\GUI_YOLO_Detection-main\\Picture\\Car_70.mp4")
    if not video.isOpened():
        print("Error: Could not open video.")
        exit()
    
    detection_thread = threading.Thread(target=detect_plate, daemon=True)
    text_detection_thread = threading.Thread(target=detect_text,daemon=True)
    detection_thread.start()
    text_detection_thread.start()

    while video.isOpened():
        check, frame = video.read()
        frame = resize_frame(frame,width=640)
        if run < 1:
            run = run + 1
            video_detection = threading.Thread(target=detect_video,daemon=True)
            video_detection.start()
        if not check:
            print("Reached the end of the video or error occurred.")
            run = 0
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    stop_thread = True
    detection_thread.join()
    text_detection_thread.join()
    video_detection.join()
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognized()