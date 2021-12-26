# pspack-flask
pOOBs4 PS4 exploit for v9.0 + automatic gold hen
 
 ## About
 
This is just a repacked psOOBs4, as a flask package with the addition of automatic sending of GoldHEN. Some other small changes:

All credit to the team behind pOOBs4

## Setup

1. Download [Python](https://www.python.org/downloads/) and install it, ideally 3.10
2. Install flask `python3 -m pip install -r requirements.txt`

## Exploiting

1. Run app `python3 app.py`. Might need to run as root to bind to port 1337
2. In the command line the IP address to navigate to will be printed e.g `* Running on http://192.168.1.200:1337/ (Press CTRL+C to quit)`
3. Navigate to port 1337 on that IP on your PS4
4. Same as psOOBs4
5. GoldHEN should be sent once the server detects success via log messages

## Running in Docker

1. Run `docker build -t pspack-flask .`
2. Run `docker run --name pspack -d -p 1337:1337 pspack-flask`

## Help! It doesn't work on my machine

1. Try again
2. If you're not running 9.00, the exploit won't run. You'll need to modify [the template](https://github.com/mc-17/pspack-flask/blob/main/templates/index.html#L70) to match your version, or just remove the if/endif
