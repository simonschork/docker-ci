from flask import Flask, jsonify


app = Flask(__name__)


weine = [
    {"id": 1, "name": "Spritzi", "rating": 4},
    {"id": 2, "name": "Blubber", "rating": 3},
]


@app.route("/weincheckerapp/api/v1.0/weine", methods=["GET"])
def get_weine():
    return jsonify({"weine": weine})


if __name__ == "__main__":
    app.run(debug=True)
