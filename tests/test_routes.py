# tests/test_routes.py

def test_list_products_by_name(self):
    """It should List products by name"""
    self._create_products(5)
    response = self.client.get(BASE_URL, query_string='name=Product')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertTrue(all(product["name"] == 'Product' for product in data))

def test_list_products_by_category(self):
    """It should List products by category"""
    self._create_products(5)
    response = self.client.get(BASE_URL, query_string='category=TOYS')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertTrue(all(product["category"] == 'TOYS' for product in data))

def test_list_products_by_availability(self):
    """It should List products by availability"""
    self._create_products(5)
    response = self.client.get(BASE_URL, query_string='available=true')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.get_json()
    self.assertTrue(all(product["available"] for product in data))
