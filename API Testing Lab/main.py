from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

iceCream = {1: "Vanilla", 2: "Chocolate", 3: "Strawberry", 4: "Cotton Candy", 5: "Mint Chocolate Chip"}


class IceCream(Resource):
    def get(self, ice_cream_id):
        return {ice_cream_id: iceCream[ice_cream_id]}

    def put(self, ice_cream_id):
        iceCream[ice_cream_id] = request.form['name']
        return {ice_cream_id: iceCream[ice_cream_id]}


api.add_resource(IceCream, "/iceCream/<int:ice_cream_id>")

if __name__ == "__main__":
    app.run(debug=True)
