import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='productorenpython')

channel.basic_publish(exchange='', routing_key='productorenpython', body='¡Hola consumidor en JavaScript!')
print(" [x] Sent 'Hello JavaScript!'")

connection.close()
