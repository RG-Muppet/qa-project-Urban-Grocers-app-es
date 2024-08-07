import sender_stand_request
import data


# función que cambiará el contenido del cuerpo de solicitud
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_user(data.user_body)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert user_response.json()["authToken"] != ""
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


#	El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


#	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_create_user_511_letters_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_user_special_caracter_in_name_get_success_response():
    positive_assert("№%@")


#	Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_kit_3_letter_2_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")


#	Se permiten números: kit_body = { "name": "123" }
def test_create_kit_3_number_in_name_get_success_response():
    positive_assert("123")


def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400


def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


#	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


#	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


#	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_user_empty_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)


#El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_user_no_first_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)
