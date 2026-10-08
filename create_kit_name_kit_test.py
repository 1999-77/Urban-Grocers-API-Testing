import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = {
        "name": name
    }
    return current_kit_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_data)
    assert response.status_code == 201
    assert response.json()["authToken"] != ""
    return response.json()["authToken"]

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )
    assert response.status_code == 400

# prueba 1 se permite 1 character
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# prueba 2 se permiten 511 characters
def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body("A" * 511)
    positive_assert(kit_body)

# prueba 3 no se permiten 0 characters
def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# prueba 4 no se permiten 512 characters
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("A" * 512)
    negative_assert_code_400(kit_body)

# prueba 5 se permiten caracteres especiales
def test_create_kit_special_symbols_in_name_get_success_response():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

# prueba 6 se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# prueba 7 se permiten números
def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# prueba 8 falta el parámetro name
def test_create_kit_no_name_get_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

# prueba 9 tipo de parámetro incorrect
def test_create_kit_number_type_name_get_error_response():
    kit_body = {
        "name": 123
    }
    negative_assert_code_400(kit_body)



