##  Flask + Redis Docker Compose Projesi  
_Basit bir Flask uygulaması + Redis servisi ile Docker Compose örgi_

## Proje Açıklaması (Türkçe)

Bu proje, Flask kullanılarak hazırlais basit bir web uygulamasını ve Redis veritabanını Docker Compose ile ayaga kaldırır. Amaç, çoklu servislerin Docker üzerinden yönetimini vesimini göstermek.

## Kullanılan Teknolojiler

- **Python (Flask)** Web uygulaması
- **Redis** Sayı verisini saklayan bellek içi veritabanı
- **Docker & Docker Compose** Konteynerleştirme ve servis yönetimi

## Klasör Yapısı

flask-redis-app/
--app/
----app.py
----requirements.txt
--Dockerfile
--docker-compose.yml
--.gitignore
--README.md
