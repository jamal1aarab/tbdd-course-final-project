# tests/test_models.py

def test_read_a_product(self):
    """It should Read a product"""
    product = ProductFactory()
    product.create()
    self.assertIsNotNone(product.id)
    
    # Fetch it back
    found_product = Product.find(product.id)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)

def test_find_product_by_name(self):
    """It should Find products by name"""
    products = [ProductFactory(name="Apple") for _ in range(3)]
    for product in products:
        product.create()
    
    found_products = Product.find_by_name("Apple")
    self.assertEqual(len(found_products), 3)
    for product in found_products:
        self.assertEqual(product.name, "Apple")

def test_find_product_by_category(self):
    """It should Find products by category"""
    products = [ProductFactory(category=Category.TOYS) for _ in range(3)]
    for product in products:
        product.create()
    
    found_products = Product.find_by_category(Category.TOYS)
    self.assertEqual(len(found_products), 3)
    for product in found_products:
        self.assertEqual(product.category, Category.TOYS)

def test_find_product_by_availability(self):
    """It should Find products by availability"""
    products = [ProductFactory(available=True) for _ in range(3)]
    for product in products:
        product.create()
    
    found_products = Product.find_by_availability(True)
    self.assertEqual(len(found_products), 3)
    for product in found_products:
        self.assertTrue(product.available)
