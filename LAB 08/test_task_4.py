# Test cases for ShoppingCart
import unittest
from task_4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.5)

        # Add same item again (should sum price)
        self.cart.add_item("apple", 2.0)
        self.assertEqual(self.cart.items["apple"], 3.5)

        # Add another item
        self.cart.add_item("banana", 0.99)
        self.assertIn("banana", self.cart.items)
        self.assertEqual(self.cart.items["banana"], 0.99)

    def test_add_item_invalid(self):
        with self.assertRaises(ValueError):
            self.cart.add_item(123, 1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item("orange", -2)
        with self.assertRaises(ValueError):
            self.cart.add_item("orange", "free")

    def test_remove_item(self):
        self.cart.add_item("milk", 2.5)
        self.cart.add_item("bread", 1.0)
        self.cart.remove_item("milk")
        self.assertNotIn("milk", self.cart.items)
        self.assertIn("bread", self.cart.items)

    def test_remove_item_not_found(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("not_in_cart")

    def test_total_cost(self):
        self.assertEqual(self.cart.total_cost(), 0)
        self.cart.add_item("eggs", 2.0)
        self.cart.add_item("cheese", 3.5)
        self.assertEqual(self.cart.total_cost(), 5.5)
        self.cart.add_item("eggs", 1.0)  # eggs total: 3.0
        self.assertEqual(self.cart.total_cost(), 6.5)
        self.cart.remove_item("cheese")
        self.assertEqual(self.cart.total_cost(), 3.0)

if __name__ == "__main__":
    unittest.main()
