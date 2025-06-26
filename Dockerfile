# Hafif ve resmi Python 3.9 Alpine tabanlı imajı kullanıyoruz
FROM python:3.9-alpine

# Çalışma dizinimizi /app olarak belirliyoruz
WORKDIR /app

# Gereksinim dosyamızı konteyner içine kopyalıyoruz
COPY app/requirements.txt .

# Bağımlılıkları yüklüyoruz (cache'lememek için --no-cache-dir)
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını konteyner içine kopyalıyoruz
COPY app/ .

# Uygulamayı başlatıyoruz
CMD ["python", "app.py"]
