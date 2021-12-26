import os

from flask import Flask, render_template, request
from urllib.parse import unquote_plus
from sender import send
app = Flask(__name__)


@app.route('/')
def index():
    ua = request.headers.get("User-Agent", None)
    try:
        if ua:
            ua_part = ua[ua.index("PlayStation 4/") + len("PlayStation 4/"):]
            ua_part = ua_part[:ua_part.index(")")]
    except ValueError:
        print("Not PS4")
        ua_part = ua

    return render_template("index.html", version=ua_part)


@app.route("/log/<msg>")
def log(msg):
    msg = unquote_plus(msg)
    if "done" in msg or "already" in msg:
        # success message, send HEN
        print(f"Sending golden hen to {request.remote_addr}")
        send(request.remote_addr, 9020, "payload/goldhen_2.0b2_900.bin")

    print(msg)
    return "OK"


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
