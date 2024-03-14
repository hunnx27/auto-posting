import redis

# Redis 연결
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushall()