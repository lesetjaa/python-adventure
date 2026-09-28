import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "lesetja"
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph1"


def format_date(date: datetime):
    return date.strftime("%Y%m%d")


user_params = {
    "token": TOKEN,  # my own token
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Step 1 - create a user account

# response = requests.post(url=pixela_endpoint, json=user_params) # we are sending json data
# print(response.text)


# Step 2 - create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Read Pages",
    "unit": "pixel",
    "type": "int",
    "color": "sora",
}

req_header = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=req_headers)
# print(graph_response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
todays_date = format_date(datetime.today())

pixel_config = {
    "date": todays_date,
    "quantity": "1",
}

# pixel_response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=req_header)
# print(pixel_response.text)

date_to_update = format_date(datetime.today() - timedelta(days=1))  # yesterday
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

update_pixel_config = {
    "quantity": "9"
}

# update_response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=req_header)
# print(update_response.text)

date_to_delete = format_date(datetime(2026, 9, 15))
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

# delete_response = requests.delete(url=delete_pixel_endpoint, headers=req_header)
# print(delete_response.text)
