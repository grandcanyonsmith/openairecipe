import requests
import json


# client_id = "MvBPV3sEIoYkaYOO7ahud9" # Your client ID
# client_secret = "usu07u9dwMzbF5MPth0VAiZdbYzBGj" # Your client secret
# personal_access_token = "352269-431a5429-3b59-4ff1-a4ad-24f1304642df" # Your personal access token

# def authenticate_figma_app(client_id, client_secret):
#     """
#     Authenticate a Figma app
#     :param client_id: Your client ID
#     :param client_secret: Your client secret
#     :return: A JSON object containing the access token
#     """
#     url = "https://www.figma.com/api/oauth/token"
#     data = {
#         "client_id": client_id,
#         "client_secret": client_secret,
#         "grant_type": "client_credentials"
#     }
#     response = requests.post(url, data=data)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file(file_key, access_token):
#     """
#     Get a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the file
#     """
#     url = "https://api.figma.com/v1/files/" + file_key
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_nodes(file_key, access_token):
#     """
#     Get the nodes of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the nodes
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/nodes"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_images(file_key, access_token):
#     """
#     Get the images of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the images
#     """
#     url = "https://api.figma.com/v1/images/" + file_key
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_comments(file_key, access_token):
#     """
#     Get the comments of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the comments
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/comments"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_versions(file_key, access_token):
#     """
#     Get the versions of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the versions
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/versions"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_teams(file_key, access_token):
#     """
#     Get the teams of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the teams
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/teams"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_project(file_key, access_token):
#     """
#     Get the project of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the project
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/project"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_comments(file_key, access_token):
#     """
#     Get the comments of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the comments
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/comments"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)

# def get_figma_file_comments(file_key, access_token):
#     """
#     Get the comments of a Figma file
#     :param file_key: The key of the file
#     :param access_token: The access token
#     :return: A JSON object containing the comments
#     """
#     url = "https://api.figma.com/v1/files/" + file_key + "/comments"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return json.loads(response.text)
import requests, json


uri = "https://www.figma.com/api/oauth/token"
headers = {
    "Content-Type": "application/json"
}
body = {
    "client_id": "MvBPV3sEIoYkaYOO7ahud9",
    "client_secret": "usu07u9dwMzbF5MPth0VAiZdbYzBGj",
    "code": "code&",
    "redirect_uri": "https://sterlingenterprises.io",
    "grant_type": "authorization_code"
}

response = requests.post(uri, headers=headers, data=json.dumps(body))

print(response.json())