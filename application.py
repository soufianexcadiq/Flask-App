import os
from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html", message="CI/CD Flask App Working!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    application.run(host="0.0.0.0", port=port)
