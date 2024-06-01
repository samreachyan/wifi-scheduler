import requests

# Example username and password
username = "student"
new_password = "0439af55190043dc0ff9deacaa5c7961"  # Ensure this is properly assigned

url = "http://10.11.0.1/mobile/login"

# Print the variables to ensure they are not None
print(f"Username: {username}")
print(f"Password: {new_password}")

# Define the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Define the payload (form data)
payload = {
    'username': username,  # replace with the actual username value
    'password': new_password,  # replace with the actual password value
    'dst': ''
}

# Send the POST request
response = requests.post(url, data=payload, headers=headers)

# Print the response for debugging
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)