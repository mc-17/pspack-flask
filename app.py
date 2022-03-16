import os
import glob

from flask import Flask, render_template, request
from urllib.parse import unquote_plus
from sender import send
app = Flask(__name__)


@app.route('/')
def index():
    ua = request.headers.get("User-Agent", None)
    ua_part = None
    if ua:
        if "PlayStation 4/" in ua:
            ua_part = ua[ua.index("PlayStation 4/") + len("PlayStation 4/"):]
        elif "Playstation 4/" in ua:
            ua_part = ua[ua.index("Playstation 4/") + len("Playstation 4/"):]

        if ")" in ua_part:
            ua_part = ua_part[:ua_part.index(")")]
        else:
            ua_part = None

    if not ua_part:
        print("Not PS4")
        ua_part = ua

    return render_template("index.html", version=ua_part)


@app.route("/log/<msg>")
def log(msg):
    msg = unquote_plus(msg)
    if "done" in msg or "already" in msg:
        # success message, send HEN
        print(f"Sending golden hen to {request.remote_addr}")

        # find last file in folder
        files_path = sorted(glob.glob("GoldHEN/*.bin"))
        last_file = files_path[-1]
        send(request.remote_addr, 9020, last_file)

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
