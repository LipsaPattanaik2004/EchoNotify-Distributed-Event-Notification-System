import json
from queue.connection import get_channel
from retry.retry_handler import send_to_retry
from database.models import SessionLocal, Notification

def process_notification(ch, method, properties, body):
    data = json.loads(body)

    session = SessionLocal()

    try:
        print(f"[Consumer] Processing: {data}")

        # Simulate failure randomly (for retry demo)
        import random
        if random.choice([True, False]):
            raise Exception("Simulated failure")

        notification = Notification(
            user_id=data["user_id"],
            message=data["message"],
            status="SENT"
        )

        session.add(notification)
        session.commit()

        print("[Consumer] Notification processed successfully")

    except Exception as e:
        print(f"[Consumer] Error: {e}")
        send_to_retry(data)

    finally:
        session.close()

def start_consumer():
    channel, connection = get_channel()

    channel.basic_consume(
        queue='notifications',
        on_message_callback=process_notification,
        auto_ack=True
    )

    print("[Consumer] Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    start_consumer()
