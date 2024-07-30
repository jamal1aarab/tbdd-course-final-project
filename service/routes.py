# service/routes.py

@app.route("/products", methods=["GET"])
def list_products():
    """Returns all of the Products"""
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")
    
    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(Category[category.upper()])
    elif available:
        products = Product.find_by_availability(available.lower() == 'true')
    else:
        products = Product.all()
    
    results = [product.serialize() for product in products]
    return jsonify(results), status.HTTP_200_OK
