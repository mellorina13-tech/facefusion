# 🎬 Ana FaceFusion Kullanım Rehberi - Video Desteği

## 🚀 Başlatma

### **Windows:**
```cmd
baslat_full.bat
```
(veya dosyaya çift tıkla)

### **Linux/Mac:**
```bash
./baslat_full.sh
```

### **Manuel Başlatma:**
```bash
python facefusion.py run
```

---

## 📺 Web Arayüzü

Uygulama başladığında tarayıcında açılır:
```
http://localhost:7860
```

---

## 🎯 Video Yüz Değiştirme - Adım Adım

### **1️⃣ SOURCE (Kaynak) Bölümü**

**Kaynak Resmi Yükle:**
- "Source" sekmesine git
- Kullanmak istediğin yüzü içeren resmi yükle
- Birden fazla resim yükleyebilirsin (daha iyi sonuç)

**İpuçları:**
- Net ve açık yüz fotoğrafı kullan
- Frontal (ön) açıdan çekilmiş olmalı
- Yeterli aydınlatma önemli

---

### **2️⃣ TARGET (Hedef) Bölümü**

**Video Dosyası Yükle:**
- "Target" sekmesine git
- Yüzün değiştirileceği videoyu yükle
- Desteklenen formatlar: MP4, AVI, MOV, MKV vs.

---

### **3️⃣ PROCESSORS (İşlemciler) Bölümü**

**Face Swapper Seç:**
- "Processors" bölümünde
- ✅ "Face Swapper" işaretle
- Diğer işlemciler (opsiyonel):
  - Face Enhancer (yüz iyileştirme)
  - Frame Enhancer (video kalitesi artırma)

---

### **4️⃣ AYARLAR**

**Face Swapper Model:**
- `inswapper_128` (hızlı, önerilen)
- `simswap_256` (daha kaliteli)
- `ghost_256` (deneysel)

**Execution:**
- Thread Count: 4-8 arası (bilgisayarına göre)
- Execution Provider: CPU veya GPU

---

### **5️⃣ OUTPUT (Çıktı) Bölümü**

**Çıktı Ayarları:**
- Output Path: Kaydetmek istediğin dosya yolu
- Video Encoder: `libx264` (önerilen)
- Video Quality: `90` (yüksek kalite)
- Video FPS: Orijinal video ile aynı

---

### **6️⃣ İŞLEME BAŞLA**

**"Start" Butonuna Tıkla:**
- İşlem başlar
- İlerleme çubuğu gösterir
- Terminal'de detaylı log görürsün

**Süre:**
- 10 saniye video = ~2-5 dakika (CPU)
- GPU ile çok daha hızlı

---

## 🎨 GELİŞMİŞ ÖZELLİKLER

### **Face Mask (Yüz Maskesi)**

Yüzün hangi bölgelerini değiştireceğini ayarla:

**Face Mask Types:**
- ✅ **Box** - Kare alan
- ✅ **Occlusion** - Engelleri algılar
- ✅ **Region** - Özel bölgeler

**Face Mask Blur:**
- 0.0 - 1.0 arası
- 0.3 önerilir (doğal geçiş)

**Face Mask Padding:**
- Top, Right, Bottom, Left
- Her kenar için ayrı ayar

---

### **Face Selector (Yüz Seçici)**

Videoda birden fazla yüz varsa:

**Face Selector Mode:**
- `reference` - Referans yüze en yakını
- `one` - En büyük yüz
- `many` - Tüm yüzler

**Face Selector Order:**
- `left-right` - Soldan sağa
- `large-small` - Büyükten küçüğe
- `best-worst` - En iyi skorlu

---

### **Trim Frame (Kırpma)**

Videonun sadece bir kısmını işle:

**Trim Frame Start:**
- Başlangıç frame numarası
- Örn: 0 (baştan başla)

**Trim Frame End:**
- Bitiş frame numarası
- Örn: 300 (5 saniye @ 60fps)

---

## 📊 PERFORMANS İPUÇLARI

### **Hız Artırma:**

1. **Thread Count Artır:**
   - Execution Thread Count: 8 veya 16
   - CPU çekirdek sayına göre ayarla

2. **Video Çözünürlüğü Azalt:**
   - Output Video Resolution: 720p veya 1080p
   - 4K çok yavaş

3. **Basit Model Kullan:**
   - `inswapper_128` en hızlı
   - `simswap_256` daha yavaş ama kaliteli

4. **GPU Kullan (Varsa):**
   - Execution Provider: CUDA
   - 10-20x daha hızlı

---

### **Kalite Artırma:**

1. **Face Enhancer Ekle:**
   - Processors'da ✅ Face Enhancer işaretle
   - Yüz detaylarını iyileştirir

2. **Frame Enhancer Ekle:**
   - Processors'da ✅ Frame Enhancer işaretle
   - Video kalitesini artırır

3. **Yüksek Kalite Model:**
   - `simswap_256` kullan
   - Daha yavaş ama çok daha iyi

4. **Video Quality Artır:**
   - Output Video Quality: 95-100

---

## 🎥 WEBCAM CANLI YÜZ DEĞİŞTİRME

### **Başlatma:**

```bash
python facefusion.py run --ui-layouts webcam
```

veya web arayüzünde **"Webcam"** sekmesine git.

**Özellikler:**
- ✅ Gerçek zamanlı yüz değiştirme
- ✅ Webcam'den canlı görüntü
- ✅ Kayıt yapabilme
- ✅ Eğlenceli ve hızlı

---

## 📋 ÖRNEK KULLANIM SENARYOLARI

### **Senaryo 1: Kısa Video Klibi**

```
Source: kendi_yuzum.jpg
Target: 10_saniye_video.mp4
Processor: Face Swapper
Model: inswapper_128
Output: sonuc.mp4

Süre: ~3 dakika
```

---

### **Senaryo 2: Yüksek Kalite Müzik Videosu**

```
Source: 3_farkli_acidan_yuz.jpg (x3)
Target: muzik_klibi.mp4 (3 dakika)
Processors:
  - Face Swapper
  - Face Enhancer
  - Frame Enhancer
Model: simswap_256
Quality: 95
Output: yuksek_kalite_sonuc.mp4

Süre: ~30-45 dakika (CPU)
```

---

### **Senaryo 3: Film Sahnesi**

```
Source: aktör_yuzu.jpg
Target: film_sahnesi.mp4 (1 dakika)
Processor: Face Swapper
Model: inswapper_128
Face Selector: reference
Mask Blur: 0.4 (doğal)
Output: degistirilmis_sahne.mp4

Süre: ~10-15 dakika
```

---

## ⚙️ KOMUT SATIRI KULLANIMI

Arayüz kullanmadan, direkt komutla:

### **Temel Video Swap:**

```bash
python facefusion.py headless-run \
  --source kaynak.jpg \
  --target video.mp4 \
  --output sonuc.mp4 \
  --processors face_swapper
```

### **Gelişmiş Ayarlarla:**

```bash
python facefusion.py headless-run \
  --source kaynak.jpg \
  --target video.mp4 \
  --output sonuc.mp4 \
  --processors face_swapper face_enhancer \
  --face-swapper-model simswap_256 \
  --execution-thread-count 8 \
  --output-video-quality 90
```

---

## 🐛 SORUN GİDERME

### **"Out of memory" Hatası:**

```
1. Video Memory Strategy: strict
2. Thread Count azalt: 2 veya 4
3. Video çözünürlüğü azalt
```

### **Çok Yavaş İşliyor:**

```
1. Basit model kullan: inswapper_128
2. Enhancer'ları kapat
3. Thread count artır
4. Video'yu kırp (trim frame)
```

### **Sonuç Doğal Görünmüyor:**

```
1. Face Mask Blur artır: 0.4-0.5
2. Face Enhancer ekle
3. Farklı model dene: simswap_256
4. Benzer açıdan kaynak resim kullan
```

### **Yüz Algılanmıyor:**

```
1. Face Detector Score azalt: 0.3
2. Daha net kaynak resmi kullan
3. Frontal açıdan resim çek
4. Yeterli ışık olsun
```

---

## 📚 KOMUTLAR LİSTESİ

### **Ana Komutlar:**

```bash
# Web arayüzü başlat
python facefusion.py run

# Webcam modu
python facefusion.py run --ui-layouts webcam

# Komut satırı işleme
python facefusion.py headless-run

# Toplu işlem
python facefusion.py batch-run

# Benchmark test
python facefusion.py benchmark
```

### **Yardım:**

```bash
# Tüm komutları gör
python facefusion.py --help

# Belirli komut yardımı
python facefusion.py run --help
python facefusion.py headless-run --help
```

---

## 🎓 DAHA FAZLA BİLGİ

**Resmi Dokümantasyon:**
- https://docs.facefusion.io

**GitHub:**
- https://github.com/facefusion/facefusion

**Video Tutorials:**
- YouTube'da "FaceFusion tutorial" ara

---

## ⚠️ ÖNEMLİ NOTLAR

1. **Yasa Dışı Kullanım Yasak:**
   - Başkalarını kandırmak için kullanma
   - İzinsiz başkalarının yüzünü kullanma
   - Deepfake farkındalığı önemli

2. **İlk Kullanım:**
   - Modeller indirilecek (2-5 dakika)
   - İnternet bağlantısı gerekli
   - ~300-500MB yer kaplar

3. **Performans:**
   - CPU ile yavaş (normal)
   - GPU varsa çok hızlı
   - Sabırlı ol

4. **Kalite:**
   - İyi kaynak resmi = iyi sonuç
   - Benzer açı ve ışık şart
   - Denemeler yap

---

## 🎉 BAŞARILI KULLANIM!

**Artık hazırsın!** Hem resim hem video ile yüz değiştirme yapabilirsin.

```bash
# Hemen başla:
baslat_full.bat  # Windows
./baslat_full.sh # Linux/Mac

# veya
python facefusion.py run
```

**İyi eğlenceler!** 🚀
