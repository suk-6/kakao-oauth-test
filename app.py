from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/redirect")
def redirect():
    code = request.args.get("code")
    res = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&redirect_uri\=http://localhost:5001&client_id=1435f38002c0dc20f7552d34a9c5f87b&code={code}"
    )
    return res.json()


if __name__ == "__main__":
    app.run(port=5001)
