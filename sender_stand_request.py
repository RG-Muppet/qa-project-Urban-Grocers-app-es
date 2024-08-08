import configuration
import requests
import data


#Creación de usuario y token
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers_user)


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


#creación de kit
def post_new_client_kit(kit_body, authToken):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + authToken
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)




