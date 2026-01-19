#!/usr/bin/env python3
"""
FaceFusion Kurulum Test Script'i
Bu script tüm bağımlılıkları kontrol eder
"""

import sys
print("Python Versiyonu:", sys.version)
print("\n" + "="*60)
print("PAKET KONTROLÜ BAŞLIYOR")
print("="*60 + "\n")

# 1. Temel Python Paketleri
packages = [
    ('gradio', 'Gradio (Web UI)'),
    ('cv2', 'OpenCV (Görüntü işleme)'),
    ('numpy', 'NumPy (Matematik)'),
    ('onnxruntime', 'ONNX Runtime (AI modelleri)'),
]

missing_packages = []

for package_name, description in packages:
    try:
        __import__(package_name)
        print(f"✅ {description:30} - KURULU")
    except ImportError:
        print(f"❌ {description:30} - EKSİK!")
        missing_packages.append(package_name)

print("\n" + "="*60)

# 2. FaceFusion Modülleri
print("\nFACEFUSION MODÜL KONTROLÜ")
print("="*60 + "\n")

try:
    import os
    os.environ['OMP_NUM_THREADS'] = '1'

    facefusion_modules = [
        'facefusion.state_manager',
        'facefusion.face_detector',
        'facefusion.face_landmarker',
        'facefusion.face_recognizer',
        'facefusion.face_analyser',
        'facefusion.processors.modules.face_swapper.core',
    ]

    for module in facefusion_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except Exception as e:
            print(f"❌ {module} - HATA: {str(e)}")

except Exception as e:
    print(f"❌ FaceFusion import hatası: {str(e)}")

print("\n" + "="*60)
print("SONUÇ")
print("="*60 + "\n")

if missing_packages:
    print("❌ EKSİK PAKETLER VAR!\n")
    print("Şu komutu çalıştır:")
    print(f"pip install {' '.join(missing_packages)}")
    print("\nveya:")
    print("pip install -r requirements.txt")
else:
    print("✅ TÜM TEMEL PAKETLER KURULU!")
    print("\nŞimdi modelleri test et:")
    print("python face_swap_app.py")

print("\n" + "="*60)

# 3. Klasör Kontrolü
print("\nKLASÖR YAPISI KONTROLÜ")
print("="*60 + "\n")

import os
important_paths = [
    'facefusion/',
    'requirements.txt',
    'face_swap_app.py',
    '.assets/models/' if os.path.exists('.assets/models/') else None,
]

for path in important_paths:
    if path and os.path.exists(path):
        print(f"✅ {path}")
    else:
        print(f"❌ {path} - BULUNAMADI!")

print("\n" + "="*60)
