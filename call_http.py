import requests
import re

# Make a GET request to the URL
url = "http://10.11.0.1/mobile/login?dst=&target=mobile"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.text

    # Print or use the HTML content as needed
    # print(html_content)
    
    search_string = r"hexMD5("

    # Split the HTML content by lines
    html_lines = html_content.split('\n')

    # Find the line containing the search string using regular expressions
    matching_line = None
    for line in html_lines:
        if re.search(re.escape(search_string), line):
            matching_line = line.strip()
            break

    # Print the matching line
    if matching_line:
        print("Matching line:")
        print(matching_line)
    else:
        print("The specified string was not found in the HTML content.")

else:
    print("Failed to retrieve HTML. Status code:", response.status_code)
