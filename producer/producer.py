import json
from queue.connection import get_channel

def send_notification(data):
    channel, connection = get_channel()

    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=json.dumps(data)
    )

    print(f"[Producer] Sent: {data}")

    connection.close()
