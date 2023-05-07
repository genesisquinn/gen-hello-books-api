from flask import jsonify 

def test_get_empty_all_books(client):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []



def test_get_one_planet(client, two_saved_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"title": "Frankenstein", "description": "Horror",  "id":1}

def test_get_non_existent_planet(client, two_saved_books):
    response = client.get("/books/100")
    response_body = response.get_json()

    assert response.status_code == 404

def test_invalid_planet_route(client, two_saved_books):
    response = client.get("/books/ADA")
    response_body = response.get_json()

    assert response.status_code == 400

def test_get_all_planets(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()
    print(response_body)

    assert response.status_code == 200
    assert response_body == [{"title": "Frankenstein", "description": "Horror","id": 1}, 
                            {"title": "The Force", "description": "Thriller", "id": 2}]

def test_post_one_planet(client):
    response =client.post ("/books", json= {"title": "The Shining", 
                                            "description": "Horror"})
    
    response_body = response.get_data(as_text=True) 
    assert response.status_code == 201
    assert response_body == (f"Book The Shining successfully created")