from fastapi.testclient import TestClient
from fastapi_basics.learning_fastapi import app

# Create a "client" that can send requests to the app
client = TestClient(app)

#Test the home page
def test_read_main():
    #The Robot sends a GET request
    response = client.get("/")

    #Assert: Check if status code is success
    assert response.status_code == 200

    #Assert: Check if the message is what we expect
    assert response.json() == {
        "message": "Hello from my new server!",
        "tip": "To test the API and add shoes, go to: http://127.0.0.1:8000/docs"
    }

#Test searching for a shoe that doesn't exist
def test_get_non_existent_shoe():
    # Try to get shoe ID 999
    response = client.get("/shoes/999")
    # Check if we get our custom error message
    assert response.json() == {"error": "Shoe not found in the factory"}


def test_shoe_lifecycle():
    #First :Test creating a new shoe (POST Testing)
    # Define the new shoe data
    new_shoe_data = {
        "id": 10,
        "name": "Adidas Yeezy",
        "size": 42,
        "color": "Grey"
    }
    #Send the POST request with the JSON data
    response = client.post("/shoes/", json=new_shoe_data)

    assert response.status_code == 200
    assert response.json()["message"] == "Shoe added successfully!"
    assert response.json()["shoe"]["name"] == "Adidas Yeezy"

    #Try to GET the shoe we just created (GET Testing)
    get_response = client.get("/shoes/10")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Adidas Yeezy"

    #Second: Test updating a shoe (PUT TESTING)

    update_data = {
        "id": 10,
        "name": "Adidas Yeezy",
        "size": 42,
        "color": "Red"
    }
    #send the put request to update shoe (ID 10)
    response = client.put("/shoes/10", json=update_data)

    #check
    assert response.status_code == 200
    assert response.json()["message"] == "Shoe 10 has been updated."

    #verify the shoe again to see the new color
    get_res = client.get("/shoes/10")
    assert get_res.json()["color"]== "Red"

    #Test deleting a sohe (DELETE TESTING)
    response = client.delete("/shoes/10")

    assert response.status_code == 200
    assert "has been deleted" in response.json()["message"]

    #try to get the shoe
    final_check = client.get("/shoes/10")
    assert "error" in final_check.json()


