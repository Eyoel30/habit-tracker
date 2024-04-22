import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "iloveeyoeltomuch"
TOKEN = "sfhqew840q3f90ew32990"
GRAPH_ID = "eyoelsgraph12"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# when using post you are sending a data through the API and the data should be in a json format,
# so the parameter is json=value not params=value
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_endpoint_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=10, day=10)
update_day = today.strftime("%Y%m%d")

pixela_endpoint_update = f"{pixela_endpoint_endpoint}/{update_day}"


graph_parameter = {
    "id": GRAPH_ID,
    "name": "running exercise",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.32"
}
put_update = {
    "quantity": "20.1"
}

# when you want to access the data you need to authenticate you token so inorder to hide the token in the url entry in
# the browser from other person you need to hide it by using the header **kwag so your token is not going to be
# available for anybody to access

# response = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)
# print(response.text)

# response = requests.post(pixela_endpoint_endpoint, json=post_data, headers=headers)
# print(response.text)

response = requests.put(pixela_endpoint_update, json=put_update, headers=headers)
print(response.text)
