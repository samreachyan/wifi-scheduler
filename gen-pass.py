import hashlib
import re
import requests

username = 'student'
password = 'mekong'


# get the pattern
def extract_pattern(input_string):
    
    # Regular expression to match the octal sequences
    pattern = re.compile(r"'(\\[0-3]?[0-7]{1,2})' \+ document\.login\.password\.value \+ '((?:\\[0-3]?[0-7]{1,2})+)'")

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    if match:
        # Extract the matched groups
        octal1 = match.group(1)
        octal2 = match.group(2)
        
        # Print the results
        print("First octal part:", octal1)
        print("Second octal part:", octal2)

        prefix = fr"{octal1}"
        suffix = fr"{octal2}"

        decoded_prefix = prefix.encode().decode('unicode_escape')
        print("Decoded:", decoded_prefix)  # Prints: ?
        decoded_suffix = suffix.encode().decode('unicode_escape')
        print("Decoded:", decoded_suffix)  # Prints: ?

        my_pass = generate_password(decoded_prefix + password + decoded_suffix)
        print(my_pass)
        return my_pass

    else:
        print("No match found")


    

# Generate Hashed Password
def generate_password(combined_string):
    # Combine the components into a single byte string
    # combined_string = prefix + password + suffix

    # Convert the combined string into a byte array, interpreting it as Latin-1 encoded text
    byte_string = combined_string.encode('latin1')

    # Compute the MD5 hash
    md5_hash = hashlib.md5(byte_string).hexdigest()
    return md5_hash


# Extract hash string
def extract_substring(s):
    print(s)
    print("==========")
    start_idx = s.find('(') + 1  # Find the index of '(' and add 1 to exclude '('
    end_idx = s.find(')', start_idx)  # Find the index of ')' after the start_idx
    if start_idx > 0 and end_idx > start_idx:
        hash_string = s[start_idx:end_idx]
        print("Pick the body::" + hash_string)
        return extract_pattern(hash_string)
    
    return None  # Return None if '(' or ')' is not found or indices are incorrect


def call_get_page(): # type: ignore
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
            return matching_line
        else:
            print("The specified string was not found in the HTML content.")

    else:
        print("Failed to retrieve HTML. Status code:", response.status_code)


def call_login_api(username, password):
    # Define the headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Define the payload (form data)
    payload = {
        'username': username,  # replace with the actual username value
        'password': password,  # replace with the actual password value
        'dst': ''
    }

    print(payload)

    url = "http://10.11.0.1/mobile/login"

    print("\n\n============ \n")

    # Send the POST request
    response = requests.post(url, data=payload, headers=headers)

    # Print the response for debugging
    print("Response Status Code:", response.status_code)
    # print("Response Text:", response.text)
    print("\n\n============ ")

### Main function

response_md5 = call_get_page()
print(response_md5)
new_password = extract_substring(response_md5)

# Print the variables to ensure they are not None
call_login_api(username=username, password=new_password)
