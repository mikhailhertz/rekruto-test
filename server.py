from flask import Flask, request as r

app = Flask(__name__)

@app.route('/', methods=["GET"])
def do():
    n = r.args.get("name")
    m = r.args.get("message")
    n = "" if n is None else " " + n + "! "
    m = "" if m is None else " " + m + "!"
    return f'''<!DOCTYPE html><html><head><script>document.title = "Hello{n}{m}";</script></head><body>{n}{m}</body></html>'''

if __name__ == '__main__':
    app.run(debug=True)
