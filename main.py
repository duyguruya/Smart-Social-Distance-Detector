import cv2
import math
from ultralytics import YOLO

def euclidean_distance(point1, point2):
    """İki nokta arasındaki mesafeyi hesaplar."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_social_distance(image_path, model_path="yolov8n.pt", min_distance=75):
    # YOLO modelini yükleyelim
    model = YOLO(model_path)

    # Resmi oku
    img = cv2.imread(image_path)
    if img is None:
        print("Resim yüklenemedi, dosya yolunu kontrol et.")
        return

    # Tespit yap
    results = model(img)[0]
    boxes = results.boxes.xyxy.cpu().numpy()  # Kutu koordinatları
    class_ids = results.boxes.cls.cpu().numpy()  # Sınıf ID'leri

    # Sadece insanları alalım (class_id = 0)
    people_boxes = [box for box, cls in zip(boxes, class_ids) if int(cls) == 0]

    # Her kişinin kutusunun orta noktasını hesapla
    centers = []
    for box in people_boxes:
        x1, y1, x2, y2 = box
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        centers.append((center_x, center_y))

    # Başlangıçta tüm insanları yeşil kutu ile çiz
    for box in people_boxes:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Mesafe çok yakın olanları kırmızıya çevir
    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            mesafe = euclidean_distance(centers[i], centers[j])
            if mesafe < min_distance:
                # İki kişinin kutusunu kırmızı yap
                for idx in [i, j]:
                    x1, y1, x2, y2 = map(int, people_boxes[idx])
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    # Orta noktaya da kırmızı nokta koy
                    cv2.circle(img, centers[idx], 5, (0, 0, 255), -1)

    # Sonucu göster ve kaydet
    cv2.imshow("Sosyal Mesafe Kontrolü", img)
    cv2.imwrite("sonuc.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    check_social_distance("crowded.jpg")



