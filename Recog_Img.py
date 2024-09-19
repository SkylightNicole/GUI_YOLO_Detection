from ultralytics import YOLO
import cv2
import easyocr
import threading
model = YOLO("best.pt")
path = ".\\Picture\\Pic.jpg"
reader = easyocr.Reader(["en"],gpu=True)

def Img_Reg():
    img = cv2.imread(path)

    detect = model(img)[0]
    for detects in detect.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id = detects
    x1 , y1 , x2 , y2 = map(int,[x1,y1,x2,y2])
    crop_img = img[y1:y2,x1:x2].copy()
    text = reader.readtext(crop_img,detail=0)
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return img , text

if __name__ == "__main__":
    Img_Reg()