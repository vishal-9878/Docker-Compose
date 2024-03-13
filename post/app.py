from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {"id": 1, "user_id": 1, "content": "Hello, world!"},
    {"id": 2, "user_id": 2, "content": "Hi, Alice!"},
]

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    posts.append({"id": len(posts) + 1, "user_id": data["user_id"], "content": data["content"]})
    return jsonify({"message": "Post created"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)