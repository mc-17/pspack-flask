import os

from flask import Flask, render_template, request
from urllib.parse import unquote_plus
from sender import send
app = Flask(__name__)


def check_payload_path(path: str):
    path = os.path.join("payload", os.path.basename(path))
    return os.path.isfile(path)


@app.route('/')
def index():
    ua = request.headers.get("User-Agent", None)
    ua_part = ua
    try:
        if ua:
            ua_part = ua[ua.index("PlayStation 4/") + len("PlayStation 4/"):]
            ua_part = ua_part[:ua_part.index(")")]
    except ValueError:
        print("Not PS4")

    return render_template("index.html", version=ua_part, payloads=sorted(os.listdir("payload"),
                                                                          key=lambda name: "gold" not in name))


queue = {}


@app.route("/expect/<payload>")
def expect(payload):
    payload = unquote_plus(payload)
    if check_payload_path(f"payload/{payload}"):
        print("Queuing payload request")
        queue[request.remote_addr] = os.path.join("payload", payload)
    else:
        print("Bad payload request!")
    return ""


@app.route("/log/<msg>")
def log(msg):
    msg = unquote_plus(msg)
    print(msg)

    if "done" in msg:
        payload = queue.get(request.remote_addr, "payload/goldhen_2.0b_900.bin")
        print(f"Sending {payload} to {request.remote_addr}...")
        send(request.remote_addr, 9020, payload)
        print(f"Done!")

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
