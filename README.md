# pspack-flask
pOOBs4 PS4 exploit for v9.0 + automatic gold hen
 
 ## About
 
This is just a repacked psOOBs4, as a flask package with the addition of automatic sending of GoldHEN. Some other small changes:

- Some magic numbers have been renamed (never looked at a PS4 bug before, and wanted to know wtf was going on)
- Some additional logging via HTTP requests (not massively useful as can't do a lot in critical section, but useful for kicking off goldenhen send)

## Setup:

1. Activate venv `venv/bin/python3 app.py --host=0.0.0.0 --port=1337`
2. Navigate to port 1337 on your host IP on your PS4
3. Same as psOOBs4
4. GoldenHEN should be sent once the server detects success via log messages

