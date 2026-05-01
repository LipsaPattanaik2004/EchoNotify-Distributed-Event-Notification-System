# EchoNotify — Distributed Event Notification System

EchoNotify is a scalable, event-driven notification system built using Flask and RabbitMQ. It demonstrates asynchronous message processing, queue-based architecture, retry handling, and persistent storage — simulating real-world notification systems used in platforms like Uber and Swiggy.

---

## Overview

EchoNotify is designed to handle notification delivery in a distributed and fault-tolerant manner. Instead of processing requests synchronously, the system uses a producer-consumer model where events are pushed to a message queue and processed asynchronously by workers.

This ensures better scalability, reliability, and decoupling between system components.

---

## Architecture

The system follows an event-driven architecture:

1. Client sends a notification request via REST API
2. API (Producer) pushes the event to RabbitMQ queue
3. Consumer (Worker) processes the notification asynchronously
4. On failure, the message is pushed to a retry queue
5. Notification status is stored in the database

---

## Features

* Asynchronous event processing using message queues
* Producer-consumer architecture for decoupled services
* Retry mechanism for failed notifications
* REST API for triggering notifications
* Persistent storage using SQLite
* Scalable and fault-tolerant design

---

## Tech Stack

* Backend: Python (Flask)
* Messaging Queue: RabbitMQ
* Database: SQLite (SQLAlchemy ORM)
* Messaging Library: Pika
* DevOps: Docker (optional for RabbitMQ setup)

---

## Project Structure

```
echonotify/
│
├── api/
│   └── app.py
│
├── producer/
│   └── producer.py
│
├── consumer/
│   └── consumer.py
│
├── queue/
│   └── connection.py
│
├── retry/
│   └── retry_handler.py
│
├── database/
│   └── models.py
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Installation & Setup

### Step 1: Clone Repository

```
git clone https://github.com/your-username/echonotify.git
cd echonotify
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

### Step 1: Start RabbitMQ (Docker)

```
docker-compose up
```

RabbitMQ UI:
http://localhost:15672
Username: guest
Password: guest

---

### Step 2: Start API Server

```
python api/app.py
```

---

### Step 3: Start Consumer Worker

```
python consumer/consumer.py
```

---

## API Usage

### Endpoint

POST /notify

### Sample Request

```
{
  "user_id": "101",
  "message": "Your order has been shipped"
}
```

### Sample Response

```
{
  "status": "Notification queued successfully",
  "data": {
    "user_id": "101",
    "message": "Your order has been shipped"
  }
}
```

---

## Retry Mechanism

If a notification fails during processing:

* It is automatically pushed to a retry queue
* The system ensures no message is lost
* Enables fault-tolerant message delivery

---

## Database Schema

The system stores notifications with:

* user_id
* message
* status (SENT / FAILED)

---

## Future Enhancements

* Integrate Redis for caching and rate limiting
* Add email/SMS notification services
* Implement Kafka for high-throughput systems
* Add monitoring and logging dashboards
* Deploy on AWS using Docker containers

---

## Why This Project Matters

This project demonstrates:

* Distributed system design
* Event-driven architecture
* Asynchronous processing
* Fault tolerance with retry logic
* Real-world backend engineering concepts

---

## Author

Lipsa Pattanaik
ITER, SOA University

---

## License

This project is intended for educational and portfolio purposes.
