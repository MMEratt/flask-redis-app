from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis bağlantısı için ayarlar
redis_host = os.getenv("REDIS_HOST", "redis")    # Environment variable’dan al, yoksa "redis" kullan
redis_port = int(os.getenv("REDIS_PORT", 6379))  # Aynı şekilde port

# Redis client objesi
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('hits')  # 'hits' anahtarı Redis'de sayacı artırır
    return f"Merhaba! Bu sayfaya {count} kere geldiniz."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
