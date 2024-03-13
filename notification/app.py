from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = [
    {"id": 1, "user_id": 1, "content": "You have a new friend request"},
    {"id": 2, "user_id": 2, "content": "Bob commented on your post"},
]

@app.route("/notifications", methods=["GET"])
def get_notifications():
    return jsonify(notifications)

@app.route("/notifications", methods=["POST"])
def create_notification():
    data = request.get_json()
    notifications.append({"id": len(notifications) + 1, "user_id": data["user_id"], "content": data["content"]})
    return jsonify({"message": "Notification created"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)