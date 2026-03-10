
import pytest
import requests
import json

from day9.test_data_providers import read_json_data

class TestOrderAPI:
    BASE_URL = "https://simple-books-api.glitch.me/orders"
    AUTH_TOKEN = 'Bearer 05af05a54059a92cf7d5e591757e2a14cbaf81fd89530f762646ed2b4a22b1ed'

    def test_submit_delete_order(self):
        
        # Step 1 — Submit Order (POST)
        payload = {
            "bookId": 1,
            "customerName": "John"
        }

        headers = {
            "Authorization": self.AUTH_TOKEN,
            "Content-Type": "application/json"
        }

        # POST request to create order
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        order_id = response.json().get("orderId")
        
        # Step 2 — Delete Order (DELETE)
        del_res = requests.delete(f"{self.BASE_URL}/{order_id}", headers=headers)
        assert del_res.status_code == 204, f"order not delted"
