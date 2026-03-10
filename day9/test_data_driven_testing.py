
import pytest
import requests
import json

from day9.test_data_providers import read_json_data
from day9.test_data_providers import read_csv_data

BASE_URL = "https://simple-books-api.glitch.me/orders"
AUTH_TOKEN = 'Bearer 05af05a54059a92cf7d5e591757e2a14cbaf81fd89530f762646ed2b4a22b1ed'

def submit_delete_order(bookId, customerName):
        
    # Step 1 — Submit Order (POST)
    payload = {
         "bookId": int(bookId)  ,
         "customerName": customerName
    }

    headers = {
         "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    # POST request to create order
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    order_id = response.json().get("orderId")
        
    # Step 2 — Delete Order (DELETE)
    del_res = requests.delete(f"{BASE_URL}/{order_id}", headers=headers)
    assert del_res.status_code == 204, f"order not delted"


@pytest.mark.parametrize('order_data', read_json_data("./testData/orders_json_data.json"))
def test_with_json_data(self, order_data):
    order_data = order_data[0]
    submit_delete_order(order_data["BookID"], order_data["CustomerName"])         

@pytest.mark.parametrize('book_id,customer_name', read_csv_data("./testData/orders_csv_data.csv"))
def test_with_csv_data(book_id, customer_name):
    submit_delete_order(book_id, customer_name)