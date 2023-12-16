import unittest
from flask import jsonify
from app.app import create_app, prepare_db


class TestProductController(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        prepare_db(self.app)
        self.client = self.app.test_client()

    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

        data = jsonify(response.get_json())
        self.assertIsInstance(data, list)

    def test_save_product(self):
        data = {
            'code': 'ABC123',
            'name': 'Example Product',
            'description': 'This is an example product.',
            'price': 19.99,
            'quantity': 10,
            'inventoryStatus': 'In stock',
            'category': 'Electronics',
            'image': 'https://example.com/image.jpg',
            'rating': 4.5
        }

        response = self.client.post('/products', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_one_product(self):
        product_id = 1
        response = self.client.get(f'/products/{product_id}')
        self.assertEqual(response.status_code, 200)

        data = jsonify(response.get_json())
        self.assertIsInstance(data, dict)

    def test_edit_product(self):
        product_id = 1
        data = {
            'name': 'Updated Product Name',
            'description': 'Updated product description'
        }

        response = self.client.patch(f'/products/{product_id}', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        product_id = 1
        response = self.client.delete(f'/products/{product_id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
