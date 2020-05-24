from flask import Flask

# Instantiate the app
app = Flask(__name__)


@app.route("/")
def get_weine():
    return {"weine": ["Sauvignon Blang", "Chardonnay", "Dornfelder", "Grauburgunder"]}


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
