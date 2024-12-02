import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

while redis_client.llen("processed_texts") > 0:
    print(redis_client.lpop("processed_texts").decode('utf-8'))