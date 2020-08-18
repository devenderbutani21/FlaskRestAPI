from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while (n > 0):
        digit = n % 10
        sum += digit ** order
        n //= 10

    if (sum == copy_n):
        print(f"{copy_n} is an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Other Numbers": [1, 23, 32, 43, 34]
        }
    else:
        print(f"{copy_n} is not an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Other Numbers": [1, 23, 32, 43, 34]
        }

    return jsonify(result)


@app.route('/myData')
def myData():
    result = {
        "firstName": "Delta",
        "lastName": "Alpha",
        "age": 27,
        "address": {
            "streetAddress": "Plot-8, Raja Nagar",
            "city": "New Delhi",
            "state": "Delhi",
            "postalCode": "110059"
        }
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
