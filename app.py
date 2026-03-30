import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from logic import calculate_estimate, get_reasons

app = Flask(__name__)
app.secret_key = "change-this-secret-key-123"

PAID_PASSWORD = "db6658" 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/paid", methods=["GET", "POST"])
def paid():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == PAID_PASSWORD:
            session["paid_ok"] = True
            return redirect(url_for("paid"))
        else:
            return render_template("paid_login.html", error="パスワードが違います")

    if not session.get("paid_ok"):
        return render_template("paid_login.html", error=None)

    return render_template("paid.html")


@app.route("/paid-logout")
def paid_logout():
    session.pop("paid_ok", None)
    return redirect(url_for("paid"))


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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
