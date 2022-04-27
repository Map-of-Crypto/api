from flask import Flask, jsonify, request

app = Flask(__name__)

from merchants import merchants
from products import products

# Get Data Routes
@app.route('/merchants')
def getmerchants():
    # return jsonify(merchants)
    return jsonify({'merchants': merchants})


@app.route('/merchants/<string:merchant_id>')
def getmerchant(merchant_id):
    merchantsFound = [
        merchant for merchant in merchants if merchant['id'] == merchant_id.lower()]
    if (len(merchantsFound) > 0):
        return jsonify({'merchant': merchantsFound[0]})
    return jsonify({'message': 'merchant Not found'})

# Create Data Routes
@app.route('/merchants', methods=['POST'])
def addmerchant():
    new_merchant = {
        'id': request.json['id'],
        'name': request.json['name'],
        'lattitude': request.json['lattitude'],
        'longitude': request.json['longitude'],
    }
    merchants.append(new_merchant)
    return jsonify({'merchants': merchants})

# Update Data Route
@app.route('/merchants/<string:merchant_id>', methods=['PUT'])
def editmerchant(merchant_name):
    merchantsFound = [merchant for merchant in merchants if merchant['name'] == merchant_id]
    if (len(merchantsFound) > 0):
        merchantsFound[0]['id'] = request.json['id']
        merchantsFound[0]['name'] = request.json['name']
        merchantsFound[0]['lattitude'] = request.json['lattitude']
        merchantsFound[0]['longitude'] = request.json['longitude']
        return jsonify({
            'message': 'merchant Updated',
            'merchant': merchantsFound[0]
        })
    return jsonify({'message': 'merchant Not found'})

# DELETE Data Route
@app.route('/merchants/<string:merchant_name>', methods=['DELETE'])
def deletemerchant(merchant_name):
    merchantsFound = [merchant for merchant in merchants if merchant['name'] == merchant_name]
    if len(merchantsFound) > 0:
        merchants.remove(merchantsFound[0])
        return jsonify({
            'message': 'merchant Deleted',
            'merchants': merchants
        })


### product



@app.route('/products')
def getproducts():
    # return jsonify(products)
    return jsonify({'products': products})


@app.route('/products/<string:product_id>')
def getproduct(product_id):
    productsFound = [
        product for product in products if product['id'] == product_id.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'product Not found'})

# Create Data Routes
@app.route('/products', methods=['POST'])
def addproduct():
    new_product = {
        'id': request.json['id'],
        'merchant': request.json['merchant'],
        'name': request.json['name'],
        'description': request.json['description'],
        'price': request.json['price'],
        'currency': request.json['currency'],
        'shippingCosts': request.json['shippingCosts'],
    }
    products.append(new_product)
    return jsonify({'products': products})

# Update Data Route
@app.route('/products/<string:product_id>', methods=['PUT'])
def editproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_id]
    if (len(productsFound) > 0):
        productsFound[0]['id'] = request.json['id']
        productsFound[0]['merchant'] = request.json['merchant']
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['description'] = request.json['description']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['currency'] = request.json['currency']
        productsFound[0]['store'] = request.json['store']
        productsFound[0]['shippingCosts'] = request.json['shippingCosts']

        return jsonify({
            'message': 'product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'product Not found'})

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteproduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'product Deleted',
            'products': products
        })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))