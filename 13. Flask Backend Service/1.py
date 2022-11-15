from flask import Flask, request

app = Flask(__name__)


@app.route('/isPrime')
def isPrime():
    args = request.args
    primeFlag = True
    num = int(args.get('number'))
    if num == 1:
        primeFlag = False
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                primeFlag = False

    response = {
        'number': num,
        'isPrime': str(primeFlag)
    }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
