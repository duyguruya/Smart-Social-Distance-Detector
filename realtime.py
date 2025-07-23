import cv2
import math
from ultralytics import YOLO

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def main(model_path="yolov8n.pt", min_distance=75):
    # YOLO modelini yükle
    model = YOLO(model_path)

    # Kamerayı başlat
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Kişileri tespit et
        results = model(frame)[0]
        boxes = results.boxes.xyxy.cpu().numpy()
        class_ids = results.boxes.cls.cpu().numpy()

        people_boxes = [box for box, cls in zip(boxes, class_ids) if int(cls) == 0]

        centers = []
        for box in people_boxes:
            x1, y1, x2, y2 = box
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            centers.append((cx, cy))

        # Kutuları çiz (ilk başta yeşil)
        for box in people_boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Mesafeyi kontrol et ve ihlalleri kırmızı yap
        for i in range(len(centers)):
            for j in range(i + 1, len(centers)):
                distance = euclidean_distance(centers[i], centers[j])
                if distance < min_distance:
                    for idx in [i, j]:
                        x1, y1, x2, y2 = map(int, people_boxes[idx])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.circle(frame, centers[idx], 5, (0, 0, 255), -1)

        # Görüntüyü göster
        cv2.imshow("Gerçek Zamanlı Sosyal Mesafe Kontrolü", frame)

        # 'q' tuşuna basılırsa çık
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
