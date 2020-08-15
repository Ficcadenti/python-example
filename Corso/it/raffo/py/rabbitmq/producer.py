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

print(type(params))
print(params)
print(connection)
print(canale)

print('...eseguito')

i:int = 0
while True:
    message=str(i)
    i+=1
    canale.basic_publish(exchange='',routing_key='worker_queue', body=message)
    print('Inviato messaggio %s',message)
    if i>100_000:
        break

connection.close()

