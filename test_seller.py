import unittest
from datetime import date
from Product import Product
from Seller import Seller
from Service import Service

class SellerTests(unittest.TestCase):
    def setUp(self):
        self.seller = Seller()
        self.product = Product(1, "Product", "Product 1", "John Doe", 10.99, date.today(), 1.09, 10)
        self.service = Service(2, "Service", "Service 1", "Jane Smith", 99.99, date.today(), 7, True)
        self.seller.add(self.product)
        self.seller.add(self.service)

    def tearDown(self):
        self.seller = None
        self.product = None
        self.service = None

    def test_add(self):
        offering = Product(3, "Product", "Product 2", "Alice Johnson", 19.99, date.today(), 9.99, 5)
        self.seller.add(offering)
        self.assertEqual(len(self.seller.get_all()), 3)

    def test_get(self):
        result = self.seller.get(self.product.get_id())
        self.assertEqual(result, self.product)

    def test_get_returns_none_when_id_not_found(self):
        result = self.seller.get(999)
        self.assertIsNone(result)

    def test_get_all(self):
        result = self.seller.get_all()
        self.assertEqual(len(result), 2)

    def test_get_all_by_type(self):
        result = self.seller.get_all_by_type("Product")
        self.assertEqual(len(result), 1)

    def test_update(self):
        offering = Product(self.product.get_id(), "Product", "Updated Product", "John Doe", 15.99, date.today(), 8.99, 7)
        self.seller.update(offering)
        offering_id = offering.get_id()
        result = self.seller.get(offering_id)
        self.assertEqual(result.get_name(), "Updated Product")
        self.assertEqual(result.get_price(), 15.99)

    def test_update_raises_exception_when_id_not_found(self):
        offering = Product(999, "Product", "Invalid Product", "John Doe", 9.99, date.today(), 5.99, 10)
        with self.assertRaises(Exception):
            self.seller.update(offering)

    def test_delete(self):
        product_id = self.product.get_id()
        self.seller.delete(product_id)
        result = self.seller.get(product_id)
        self.assertIsNone(result)
        self.assertEqual(len(self.seller.get_all()), 1)

    def test_delete_raises_exception_when_id_not_found(self):
        with self.assertRaises(Exception):
            self.seller.delete(999)

    def test_to_dict(self):
        
        product = Product(
            id=1,
            type="Product",
            name="Test Product",
            customer_name="John Doe",
            price=19.99,
            date=date.today().__str__(),
            unit_price=9.99,
            quantity=5
        )

        
        result = product.to_dict()

        
        expected = {
            "id": 1,
            "type": "Product",
            "name": "Test Product",
            "customer_name": "John Doe",
            "price": 19.99,
            "date": date.today().__str__(),
            "unit_price": 9.99,
            "quantity": 5
        }
        self.assertEqual(result, expected)

    def test_add_returns_valid_id(self):
        # Create a Product instance
        product = Product(
            id=1,
            type="Product",
            name="Test Product",
            customer_name="John Doe",
            price=19.99,
            date=date.today().__str__(),
            unit_price=9.99,
            quantity=5
        )

        returned_id = self.seller.add(product)
        # returned id cannot be equal to 1 because there is already an object with this id
        assert returned_id != 1

if __name__ == '__main__':
    unittest.main()
