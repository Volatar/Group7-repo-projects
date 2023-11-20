from flask import Flask, request
from flask_restful import Api, Resource, abort

# Create app and api
app = Flask(__name__)
api = Api(app)

# Ice cream menu dictionary
iceCream = {1: "Vanilla", 2: "Chocolate", 3: "Strawberry", 4: "Cotton Candy", 5: "Mint Chocolate Chip"}


# Validate whether ice cream already exists
def abort_if_id_exists(ice_cream_id):
    if ice_cream_id in iceCream:
        abort(409, message="ID already exists")


# Validate whether ice cream does not exist
def abort_if_id_does_not_exists(ice_cream_id):
    if ice_cream_id not in iceCream:
        abort(404, message="ID is invalid")


# Api resource for ice cream menu
class IceCream(Resource):

    def get(self, ice_cream_id):
        abort_if_id_does_not_exists(ice_cream_id)
        return {ice_cream_id: iceCream[ice_cream_id]}, 200

    def post(self, ice_cream_id):
        abort_if_id_exists(ice_cream_id)
        iceCream[ice_cream_id] = request.form['name']
        return {ice_cream_id: iceCream[ice_cream_id]}, 201

    def put(self, ice_cream_id):
        abort_if_id_does_not_exists(ice_cream_id)
        iceCream[ice_cream_id] = request.form['name']
        return {ice_cream_id: iceCream[ice_cream_id]}, 201

    def delete(self, ice_cream_id):
        abort_if_id_does_not_exists(ice_cream_id)
        del iceCream[ice_cream_id]
        return {'message': 'Item is deleted from the menu'}, 200


# Add resource to api
api.add_resource(IceCream, "/iceCream/<int:ice_cream_id>")

# Run main
if __name__ == "__main__":
    app.run(debug=True)
