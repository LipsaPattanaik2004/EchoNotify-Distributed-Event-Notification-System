import json
from queue.connection import get_channel

def send_to_retry(data):
    channel, connection = get_channel()

    channel.basic_publish(
        exchange='',
        routing_key='retry_queue',
        body=json.dumps(data)
    )

    print(f"[Retry] Sent to retry queue: {data}")

    connection.close()
