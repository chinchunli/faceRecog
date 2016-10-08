from pykafka import KafkaClient

Pi_ID = "FF001"
client = KafkaClient(hosts="118.163.149.163:9092")
topic = client.topics['idiraspberrypi']
producer = topic.get_producer()

producer.produce(['Kaixo Nextel from pykafka!'])