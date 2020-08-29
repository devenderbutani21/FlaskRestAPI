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


@app.route('/myData', methods=['GET'])
def myData():
    result = {
        "1": {
            "category": "Pizza",
            "items": "25",
            "img_url": "https://cdn.pixabay.com/photo/2017/12/05/20/10/pizza-3000285_1280.png",
            "img_height": "160",
            "img_width": "160",
            "menu": {
                "1": {
                    "name": "Pepperoni",
                    "price_in_dollar": "7.0",
                    "rating": "4",
                    "portion_size": "200g",
                    "img_url": "",
                },
                "2": {
                    "name": "Mushroom",
                    "price_in_dollar": "10.0",
                    "rating": "3",
                    "portion_size": "200g",
                    "img_url": "",
                },
                "3": {
                    "name": "Mexican Street Corn",
                    "price_in_dollar": "12.0",
                    "rating": "4",
                    "portion_size": "200g",
                    "img_url": "",
                },
                "4": {
                    "name": "Buffalo Chicken",
                    "price_in_dollar": "14.0",
                    "rating": "4",
                    "portion_size": "200g",
                    "img_url": "",
                },
            },
        },
        "2": {
            "category": "Salads",
            "items": "40",
            "img_url": "https://cdn.pixabay.com/photo/2016/12/05/10/07/dish-1883501_1280.png",
            "img_height": "160",
            "img_width": "160",
            "menu": {
                "1": {
                    "name": "Summer Asian Slaw",
                    "price_in_dollar": "8.0",
                    "rating": "4",
                    "portion_size": "250g",
                    "img_url": "",
                },
                "2": {
                    "name": "Broccoli",
                    "price_in_dollar": "10.0",
                    "rating": "3",
                    "portion_size": "300g",
                    "img_url": "",
                },
                "3": {
                    "name": "Shredded Brussels Sprout",
                    "price_in_dollar": "12.0",
                    "rating": "4",
                    "portion_size": "300g",
                    "img_url": "",
                },
                "4": {
                    "name": "Pasta Salad",
                    "price_in_dollar": "7.0",
                    "rating": "3",
                    "portion_size": "250g",
                    "img_url": "",
                },
            },
        },
        "3": {
            "category": "Desserts",
            "items": "30",
            "img_url": "https://cdn.pixabay.com/photo/2016/04/04/09/09/dessert-1306397_1280.png",
            "img_height": "160",
            "img_width": "160",
            "menu": {
                "1": {
                    "name": "Fried Ice Cream",
                    "price_in_dollar": "10.0",
                    "rating": "4",
                    "portion_size": "100g",
                    "img_url": "",
                },
                "2": {
                    "name": "Samoa Dessert Lasagna",
                    "price_in_dollar": "8.0",
                    "rating": "3",
                    "portion_size": "100g",
                    "img_url": "",
                },
                "3": {
                    "name": "Oreo Truffles",
                    "price_in_dollar": "12.0",
                    "rating": "4",
                    "portion_size": "100g",
                    "img_url": "",
                },
                "4": {
                    "name": "Chocolate Pudding",
                    "price_in_dollar": "7.0",
                    "rating": "3",
                    "portion_size": "100g",
                    "img_url": "",
                },
            },
        },
        "4": {
            "category": "Pasta",
            "items": "44",
            "img_url": "https://cdn.pixabay.com/photo/2017/03/31/03/37/food-2190301_1280.png",
            "img_height": "140",
            "img_width": "140",
            "menu": {
                "1": {
                    "name": "Pesto",
                    "price_in_dollar": "8.0",
                    "rating": "4",
                    "portion_size": "250g",
                    "img_url": "",
                },
                "2": {
                    "name": "Lemon Linguine with Roasted Tomatoes",
                    "price_in_dollar": "10.0",
                    "rating": "3",
                    "portion_size": "300g",
                    "img_url": "",
                },
                "3": {
                    "name": "Fettuccine Alfredo",
                    "price_in_dollar": "12.0",
                    "rating": "4",
                    "portion_size": "250g",
                    "img_url": "",
                },
                "4": {
                    "name": "Spaghetti Bolognese",
                    "price_in_dollar": "10.0",
                    "rating": "3",
                    "portion_size": "250g",
                    "img_url": "",
                },
            },
        },
        "5": {
            "category": "Beverages",
            "items": "30",
            "img_url": "https://cdn.pixabay.com/photo/2018/05/12/19/56/coffee-cup-3394435_1280.png",
            "img_height": "140",
            "img_width": "140",
            "menu": {
                "1": {
                    "name": "Hot Chocolate Frost",
                    "price_in_dollar": "2.0",
                    "rating": "4",
                    "portion_size": "50g",
                    "img_url": "",
                },
                "2": {
                    "name": "Peppermint Mocha flavor",
                    "price_in_dollar": "3.0",
                    "rating": "3",
                    "portion_size": "50g",
                    "img_url": "",
                },
                "3": {
                    "name": "Caramel Brulee Latte",
                    "price_in_dollar": "4.0",
                    "rating": "4",
                    "portion_size": "50g",
                    "img_url": "",
                },
                "4": {
                    "name": "Winter Wonderland",
                    "price_in_dollar": "3.5",
                    "rating": "3",
                    "portion_size": "50g",
                    "img_url": "",
                },
            },
        },
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
