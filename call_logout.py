import requests

url = "http://10.11.0.1/mobile/logout"

# Define the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Send the POST request
response = requests.post(url, headers=headers)

# Print the response for debugging
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)