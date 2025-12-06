from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/getAction", methods=["POST"])
def get_action():
    data = request.json
    move = data.get("move", "unknown")
    # Simple AI logic
    if move == "punch":
        action = random.choice(["block", "dodge", "counter"])
    else:
        action = "idle"
    return jsonify({"action": action})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
