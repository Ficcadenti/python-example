'''
Created on 14 ago 2020

@author: raffa
'''
import pika


if __name__ == '__main__':
    pass


print('Collegamento a RabbitMQ...')
params=pika.ConnectionParameters(host='localhost')
connection=pika.BlockingConnection(params)
canale=connection.channel()
canale.queue_declare(queue='worker_queue')
print('...eseguito')

def callback(ch,method,properties,body):
    print("Ricevuto %s",body)
    
canale.basic_consume(queue='worker_queue',on_message_callback=callback)
canale.start_consuming()