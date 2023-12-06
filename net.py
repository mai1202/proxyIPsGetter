from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def serve_ips():
    return send_file('./ips.txt')


if __name__ == '__main__':
    app.run()
