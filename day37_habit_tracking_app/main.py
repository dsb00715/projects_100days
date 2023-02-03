from requests import *
from datetime import datetime

USERNAME = "dsb00715"
TOKEN = "fhdkjhfkldjskfj"
GRAPH_ID = "d1"

endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

""" 
# Step1: Setting up a user account
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)
"""

"""
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Work on TProject",
    "unit": "min",
    "type": "int",
    "color": "sora",
    "timezone": "Europe/Berlin",
}
# Step2: Setting up a graph
# response = post(url=graph_endpoint, json=graph_parameters, headers=graph_headers)
# print(response.text)
"""

today = datetime.now()
date = today.strftime("%Y%m%d")
pixel_parameters = {
    "date": date,
    "quantity": input("How many minutes did you work today?"),
}
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Step3: Post a pixel
post_response = post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(post_response.text)


"""
pixel_update_endpoint = f"{pixel_endpoint}/{date}"
pixel_update_parameters = {
    "quantity": "10",
}


# Step4: Update a pixel
# response_put = put(
#     url=pixel_update_endpoint, json=pixel_update_parameters, headers=headers
# )
# print(response_put.text)
"""

"""
# Step5: Delete a pixel 
# response_delete = delete(url=pixel_update_endpoint, headers=headers)
# print(response_delete.text)
"""
