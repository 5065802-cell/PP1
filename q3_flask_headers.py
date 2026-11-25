from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def headers():
    ua = request.headers.get("User-Agent")
    host = request.headers.get("Host")
    accept = request.headers.get("Accept")
    return f"<h2>Request Headers</h2><p><b>User-Agent:</b> {ua}</p><p><b>Host:</b> {host}</p><p><b>Accept:</b> {accept}</p>"

if __name__ == "__main__":
    app.run(debug=True)
