from flask import Flask, request, jsonify, make_response
from datetime import datetime
from Seller import Seller
from Product import Product
from Service import Service

seller = Seller()
app = Flask(__name__)

@app.route("/seller/offerings", methods=['post'])
def add_offering():
    input_json = request.get_json()
    try:
        type = input_json["type"]
        name = input_json["name"]
        customer_name = input_json["customer_name"]
        price = input_json["price"]
        date = input_json["date"].split("-")
        print(date)
        date = datetime(int(date[0]), int(date[1]), int(date[2])) 
        if type == "Product":
            unit_price = input_json["unit_price"]
            quantity = input_json["quantity"]
            id = seller.add(Product(1, type, name, customer_name, price, date, unit_price, quantity))
        elif type == "Service":
            duration_in_days = input_json["duration_in_days"]
            is_company = input_json["is_company"]
            id = seller.add(Service(1, type, name, customer_name, price, date, duration_in_days, is_company))
        else:
            return jsonify({"message": "Invalid type"}), 400
    except:
        return jsonify({"message": "Invalid Offering"}), 400
    
    return jsonify({"Id of the added offering ": f"{id}"}), 200


@app.route('/seller/offerings/<int:offering_id>', methods=['PUT'])
def update_offering(offering_id):
    input_json = request.get_json()
    try:
        type = input_json["type"]
        name = input_json["name"]
        customer_name = input_json["customer_name"]
        price = input_json["price"]
        date = input_json["date"].split("-")

        date = datetime(int(date[0]), int(date[1]), int(date[2])) 
        if type == "Product":
            unit_price = input_json["unit_price"]
            quantity = input_json["quantity"]
            offering = Product(offering_id, type, name, customer_name, price, date, unit_price, quantity)
        elif type == "Service":
            duration_in_days = input_json["duration_in_days"]
            is_company = input_json["is_company"]
            offering = Service(offering_id, type, name, customer_name, price, date, duration_in_days, is_company)
        else:
            return jsonify({"message": "Invalid type"}), 400
    except:
        return jsonify({"message": "Invalid Offering"}), 400
    try:
        seller.update(offering)
    except:
        return jsonify({"message": "offering not found"}), 404
    
    return jsonify({"message": "success"}), 200

@app.route('/seller/offerings/<int:offering_id>', methods=['DELETE'])
def delete_offering(offering_id):
    try:
        seller.delete(offering_id)
    except Exception:
        return jsonify({"message": "offering not found"}), 404
    
    return jsonify({"message": "success"}), 200

@app.route('/seller/offerings/<int:offering_id>', methods=['GET'])
def get_offering(offering_id):
    offering = seller.get(offering_id)
    if offering == None:
        return jsonify({"message": "offering not found"}), 404
    return jsonify(offering.to_dict()), 200

@app.route('/seller/offerings/all', methods=['GET'])
def get_all_offering():
    offerings = seller.get_all()
    offerings = [off.to_dict() for off in offerings]
    return jsonify(offerings), 200

@app.route('/seller/offerings/all/<type>', methods=['GET'])
def get_all_type_offering(type):
    if type != "Product" and type != "Service":
        return jsonify({"message": "Invalid type"}), 400
    
    offerings = seller.get_all_by_type(type)
    offerings = [off.to_dict() for off in offerings]
    return jsonify(offerings), 200

if __name__ == "__main__":
    app.run()