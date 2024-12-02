from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for text in ["This is a great day!", "Terrible experience.", "I love programming!"]:
    print (f"Sending: {text}")
    producer.send ("text-topic", text.encode('utf-8'))

producer.close()