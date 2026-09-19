from flask import Flask, render_template, jsonify, request
from countdown_timer import format_time, validate_custom_time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/time", methods=["POST"])
def set_time():
    data = request.get_json(silent=True) or {}

    try:
        minutes = int(data.get("minutes", 0))
        seconds = int(data.get("seconds", 0))
    except (TypeError, ValueError):
        return jsonify({"success": False, "message": "Enter valid numbers."}), 400

    if not validate_custom_time(minutes, seconds):
        return jsonify({
            "success": False,
            "message": "Seconds must be 0–59 and total time must be greater than 0."
        }), 400

    total = minutes * 60 + seconds

    return jsonify({
        "success": True,
        "total_seconds": total,
        "formatted": format_time(total)
    })


if __name__ == "__main__":
    app.run(debug=True)
