from datetime import datetime
from flask import jsonify, abort
from flask_restful import Resource, reqparse
from susej.model.product import Product
from susej.commands_dml import commands as database


class ProductService(Resource):
    def get(self):
        try:
            products = database.select_table(Product) or abort(404, "Product not found")
            return jsonify(
                {
                    "status": "1",
                    "mensage": "Sucess",
                    "products": [product.to_dict() for product in products]
                }
            )
        except Exception as error:
            return jsonify(
                {
                    "status": "0",
                    "mensage": "Error",
                    "description": f"{error}"
                }
            )

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("name", type=str)
            parser.add_argument("price", type=str)
            parser.add_argument("store_owner", type=str)
            args = parser.parse_args()

            product = Product(**args, creation_date=datetime.now())
            database.insert_table(product)

            return product.to_dict()
        except Exception as error:
            return jsonify(
                {
                    "status": "0",
                    "mensage": "Error",
                    "description": f"{error}"
                }
            )

    def delete(self):
        try:
            database.delete_table(all=True, table=Product)
            return jsonify(
                {
                    "status": "1",
                    "mensage": "Sucess"
                }
            )
        except Exception as error:
            return jsonify(
                {
                    "status": "0",
                    "mensage": "Error",
                    "description": f"{error}"
                }
            )
