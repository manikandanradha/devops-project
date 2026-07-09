import os
import redis
import time
msg = os.environ.get('APP_MESSAGE', 'Default Message')
print(f"APP_MESSAGE: {msg}")
r = redis.Redis(host='my-redis', port=6379)
print("Python app connected to redis!...")
r.set('message', 'Hello from Python to redis!!')
val = r.get('message')
print(f"redis: {val.decode('utf-8')}")