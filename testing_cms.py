import unittest
from unittest.mock import MagicMock
from entity.Courier import Courier
from dao.CourierServiceDB import CourierServiceDb

class TestCourierServiceDb(unittest.TestCase):

    def setUp(self):
        # Set up test environment
        self.courier = Courier(
            courier_id="123",
            sender_name="John Doe",
            sender_address="123 Main St",
            receiver_name="Jane Smith",
            receiver_address="456 Elm St",
            weight=5,
            status="Pending",
            tracking_number="TRACK123",
            delivery_date="2024-05-20",
            packages=1
        )

    def test_insert_order(self):
        # Test insert_order method
        courier_service = CourierServiceDb()
        courier_service.connection = MagicMock()  # Mocking the database connection
        result = courier_service.insert_order(self.courier)
        self.assertTrue(result)

    def test_update_courier_status(self):
        # Test update_courier_status method
        courier_service = CourierServiceDb()
        courier_service.connection = MagicMock()  # Mocking the database connection
        tracking_number = "TRACK123"
        new_status = "In Transit"
        result = courier_service.update_courier_status(tracking_number, new_status)
        self.assertTrue(result)

    def test_retrieve_delivery_history(self):
        # Test retrieve_delivery_history method
        courier_service = CourierServiceDb()
        courier_service.connection = MagicMock()  # Mocking the database connection
        tracking_number = "TRACK123"
        result = courier_service.retrieve_delivery_history(tracking_number)
        self.assertIsNotNone(result)

    def test_generate_shipment_status_report(self):
        # Test generate_shipment_status_report method
        courier_service = CourierServiceDb()
        courier_service.connection = MagicMock()  # Mocking the database connection
        result = courier_service.generate_shipment_status_report()
        self.assertIsNotNone(result)

    def test_generate_revenue_report(self):
        # Test generate_revenue_report method
        courier_service = CourierServiceDb()
        courier_service.connection = MagicMock()  # Mocking the database connection
        result = courier_service.generate_revenue_report()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
