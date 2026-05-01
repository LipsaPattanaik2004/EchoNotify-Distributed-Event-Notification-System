from flask import Flask, request, jsonify
from producer.producer import send_notification

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json

    required_fields = ["user_id", "message"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    send_notification(data)

    return jsonify({
        "status": "Notification queued successfully",
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
