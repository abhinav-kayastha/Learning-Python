from flask import Flask, request

app = Flask(__name__)


@app.route('/sum')
def sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    sum = number1+number2
    return str(sum)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
