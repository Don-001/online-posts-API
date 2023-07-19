import pytest
from .. import schemas


def test_create_user(client):
    response = client.post("/users", json={"email":"wazuup@gmail.com", "password": "iamapassword1"})
    
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "wazuup@gmail.com"
    assert response.status_code == 201
    
    
def test_login_user(client, test_user):
    response = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    
    assert response.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [('wrongemail@gmail.com', '007', 403),
    ('jamesbond@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, '007', 422),
    ('jamesbond@gmail.com', None, 422)])
def test_incorrect_login(client, test_user, email, password, status_code):
    response = client.post("/login", data={"username" : email, "password" : password})
    
    assert response.status_code == status_code