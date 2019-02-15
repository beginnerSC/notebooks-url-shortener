from flask import Flask, redirect, request

app = Flask(__name__)

PRODUCTION_BASE_URL = 'https://notebooks.ai/join?code={code}'
STAGING_BASE_URL = 'http://staging.notebooks.ai/join?code={code}'
DEV_BASE_URL = 'http://localhost:5000/join?code={code}'

@app.route('/')
def index():
    return 'Visit https://notebooks.ai', 404


@app.route('/i/<code>')
def invitation(code):
    base_url = PRODUCTION_BASE_URL
    if 'staging' in request.args:
        base_url = STAGING_BASE_URL
    elif 'dev' in request.args:
        base_url = DEV_BASE_URL
    return redirect(base_url.format(code=code))


if __name__ == '__main__':
    app.debug = True
    app.run()
