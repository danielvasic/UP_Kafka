from kafka import KafkaConsumer, KafkaAdminClient
import redis
from textblob import TextBlob

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

consumer = KafkaConsumer(
    "text-topic",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id="text-group"
)

for text in consumer:
    sentiment = TextBlob(text.value.decode('utf-8')).sentiment.polarity
    sentiment_type = "pozitivan" if sentiment > 0 else "negativan"
    redis_client.rpush(
        "processed_texts", 
        f"Text {text.value.decode('utf-8')}, sentiment {sentiment_type}"
    )
    print(f"Text {text.value.decode('utf-8')}, sentiment {sentiment_type}")

consumer.close()