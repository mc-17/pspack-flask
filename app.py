import argparse
from datetime import datetime
import os
import time
from distutils.version import LooseVersion
from flask import Flask, render_template, request
import fnmatch
import io
import requests
from urllib.parse import unquote_plus
import zipfile


from sender import send
app = Flask(__name__)


def get_latest_release(output_dir: str = ""):
    try:
        if output_dir and not os.path.isdir(output_dir):
            os.makedirs(output_dir, mode=0o755)

        file_version = os.path.join(output_dir, "VERSION")

        releases_url = "https://api.github.com/repos/GoldHEN/GoldHEN/releases"
        releases = sorted(requests.get(releases_url).json(),
                          key=lambda rls: LooseVersion(rls.get("tag_name", 0)),
                          reverse=True)

        if not releases:
            raise ValueError("Error retrieving GoldHEN releases!")

        latest_release = releases[0].get("zipball_url", None)
        version = releases[0].get("tag_name", None)

        if not latest_release or not version:
            raise ValueError("Error getting release URL - unexpected release format!")

        if os.path.isfile(file_version):
            with open(file_version) as fp:
                have_version = LooseVersion(fp.read())
                if have_version >= version:
                    print(f"Version on disk ({have_version}) equal to or newer to latest ({version}")
                    return

        with io.BytesIO(requests.get(latest_release).content) as zip_data:
            with zipfile.ZipFile(zip_data) as zf:
                for zip_entry in zf.filelist:
                    if fnmatch.fnmatch(zip_entry.filename, "*goldhen_*_900.bin"):
                        print(f"Found 9.0.0 GoldHEN: {zip_entry.filename}")
                        with zf.open(zip_entry) as hen_read:
                            with open(os.path.join(output_dir, "goldhen.bin"), "wb+") as hen_write:
                                hen_write.write(hen_read.read())
                                print(f"Downloaded!")

                                with open(file_version, "w+") as fp:
                                    fp.write(version)

                                break
    except requests.exceptions.ConnectionError:
        print("Failed to download GoldHEN!")


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
    print(msg)

    if "done" in msg:
        # success message, send HEN
        print(f"Sending golden hen to {request.remote_addr}")
        send(request.remote_addr, 9020, "payload/goldhen.bin")

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
    args = argparse.ArgumentParser()
    args.add_argument("--host", required=False, type=str, default='0.0.0.0')
    args.add_argument("--port", required=False, type=int, default=1337)
    args.add_argument("--offline", default=False, action="store_true", help="Do not attempt to update GoldHEN")
    args.add_argument("--update", default=False, action="store_true", help="Force update GoldHEN")
    args = args.parse_args()

    fileInfo = os.stat("payload/goldhen.bin")

    if not args.offline:
        if (time.time() - fileInfo.st_mtime) > (60 * 60 * 24 * 14) or args.update:
            get_latest_release("payload")
        else:
            print("GoldHEN not 14 days old, not updating")

    app.run(host=args.host, port=args.port)
