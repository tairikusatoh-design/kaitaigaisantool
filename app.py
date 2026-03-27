from flask import Flask, render_template, request, jsonify
from logic import calculate_estimate, get_reasons

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    
    result = calculate_estimate(data)
    reasons = get_reasons(data)

    return jsonify({
        "price_min": result["min"],
        "price_max": result["max"],
        "price_detail": result["detail"],
        "reasons": reasons
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)