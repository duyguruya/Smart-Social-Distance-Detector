# Akıllı Sosyal Mesafe Dedektörü

Bu proje, YOLOv8 derin öğrenme modeli ile bir görüntüdeki kişileri tespit eder ve aralarındaki sosyal mesafeyi analiz eder. Sosyal mesafe ihlalleri görselleştirilerek özellikle kalabalık ortamlarda farkındalık sağlamayı amaçlar.

## Özellikler

- Görsel (resim) üzerinden analiz
- YOLOv8 ile insan tespiti
- Öklidyen mesafe hesaplama
- Mesafe ihlalini kırmızı kutularla vurgulama
- İşlenmiş görüntüyü kaydetme (sonuc.jpg)

## Kullanılan Teknolojiler

- Python 3.x
- OpenCV
- Ultralytics YOLOv8

## Proje Yapısı

Smart-Social-Distance-Detector/
├── ana.py
├── gerçek zamanlı.py
├── yolov8n.pt
├── utils.py
├── kalabalık.jpg
├── sonuc.jpg
├── gereksinimler.txt
└── README.md 

## Kurulum

1. Depoyu klonlayın:

```bash
git clone https://github.com/duyguruya/Smart-Social-Distance-Detector.git
cd Smart-Social-Distance-Detector

2.Gerekli kütüphaneleri yükleyin:

bash
pip install opencv-python ultralytics

Kullanım
Aşağıdaki komut ile çalıştırabilirsiniz:

bash
python main.py
Varsayılan olarak crowded.jpg görüntüsünü işler, mesafe ihlallerini işaretler ve sonucu result.jpg olarak kaydeder.

Parametreler (main.py içinde)
Parametre	Açıklama	Varsayılan Değer
image_path	İşlenecek görselin yolu	crowded.jpg
model_path	YOLOv8 model dosyası	yolov8n.pt
min_distance	Mesafe eşiği (piksel cinsinden)	75

#Geliştirme Planları :

Gerçek zamanlı kamera desteği (realtime.py)
Mesafe ihlali istatistikleri
Web arayüzü ile analiz görüntüleme

#İletişim 
Projeyle ilgili görüş, öneri veya sorularınız için:

GitHub: github.com/duyguruya
E-posta: duyguruyacig1403@gmail.com
LinkedIn: linkedin.com/in/duygu-rüya-çığ-5b7a09322
# SmartSocialDistanceDetector
# SmartSocialDistanceDetector
# Akıllı-Sosyal-Mesafe-Algılayıcısı
