import pytest
import json

@pytest.fixture(autouse=True)
def load_json_fixture(request):
    with open("./complex.json", "r") as file:
        request.cls.json_response =  json.load(file)

class TestParseComplexJsonResponse:
    def test_user_details_vlaidation(self):
        assert  self.json_response["status"] == "success", "Wrong status"
        userDetails = self.json_response["data"]["userDetails"]
        assert userDetails["id"] == 12345, "Wrong user id"
        assert userDetails["name"] == "John Doe", "Wrong user name"
        assert userDetails["email"] == "john.doe@example.com", "Wrong user email"
        
        phoneNum = userDetails["phoneNumbers"][0]
        assert phoneNum["type"] == "home", "Wrong phone type"
        assert phoneNum["number"] == "123-456-7890", "Wrong phone number"

        geoDetails =  userDetails["address"]["geo"]
        assert geoDetails["latitude"] == 39.7817, "Wrong latitude"
        assert geoDetails["longitude"] == -89.6501, "Wrong longitude"

        userPreferences = userDetails["address"]["prefrences"]
        assert userPreferences["notifications"] is True, "Notifications should be enabled"
        assert userPreferences["theme"] == "dark", "Wrong theme preference"


    def test_recent_orders_validation(self):
        recent_orders = self.json_response['data']["userDetails"]["address"]['recentOrders']

        # verify total number of orders
        assert len(recent_orders) == 2, "Expected only 2 orders"

        # Validate First order details
        first_order = recent_orders[0]
        assert first_order['orderId'] == 101, "Order Mismatch"
        assert first_order['totalAmount'] == 1226.49, "Total Amount Mismatch"

        items = recent_orders[0]['items']
        assert items[1]['name'] == "Mouse", "Item name mismatch"

        # Validate second order details
        second_order = recent_orders[1]
        assert len(second_order['items']) == 1, "Items count mismatch"

        second_order_items = second_order['items'][0]
        assert second_order_items['name'] == "Smartphone", "Item name mismatch"
        assert second_order_items['price'] == 799.99, "Price mismatch"

    def test_preferences_and_metadata_validation(self):

        # Validate Preferences --> Languages
        preferences = self.json_response['data']['userDetails']["address"]['prefrences']
        languages = preferences['languages']

        assert len(languages) == 3
        assert languages[0] == "English"
        assert languages[1] == "Spanish"
        assert languages[2] == "French"

        # Validate Metadata
        metadata = self.json_response['data']['userDetails']['meta']

        assert metadata['requestId'] == "abc123xyz"
        assert metadata['responseTimeMs'] == 250, "Response Time mismatch"