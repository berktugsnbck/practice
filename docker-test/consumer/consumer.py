import pika
  
def on_message_recieved(ch, method, properties, body):
    print(f"recieved que: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the message")

connection_parameters = pika.ConnectionParameters(host='192.168.1.100', port=5672)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='countbox')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='countbox',  on_message_callback=on_message_recieved)

print("starting consuming")

channel.start_consuming()
