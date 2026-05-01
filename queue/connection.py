import pika

def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

def get_channel():
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue='notifications')
    channel.queue_declare(queue='retry_queue')

    return channel, connection
