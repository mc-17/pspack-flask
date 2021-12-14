# pspack-flask
pOOBs4 PS4 exploit for v9.0 + automatic gold hen
 
 ## About
 
This is just a repacked psOOBs4, as a flask package with the addition of automatic sending of GoldHEN. Some other small changes:

- Some magic numbers have been renamed (never looked at a PS4 bug before, and wanted to know wtf was going on)
- Some additional logging via HTTP requests (not massively useful as can't do a lot in critical section, but useful for kicking off goldenhen send)

## Setup:

1. Install requirements `python3 -m pip install -r requirements.txt`
2. Run app `python3 app.py --host=0.0.0.0 --port=1337`
3. Navigate to port 1337 on your host IP on your PS4
4. Same as psOOBs4
5. GoldHEN should be sent once the server detects success via log messages


## Help! It doesn't work on my machine

1. Try again
2. If you're not running 9.00, the exploit won't run. You'll need to modify [the template](https://github.com/mc-17/pspack-flask/blob/main/templates/index.html#L70) to match your version, or just remove the if/endif
