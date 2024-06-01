import re
import hashlib


# Generate Hashed Password
def generate_password(prefix, password, suffix):    
    # Combine the components into a single byte string
    combined_string = prefix + password + suffix
    print(combined_string, end='\n===\n')

    # Convert the combined string into a byte array, interpreting it as Latin-1 encoded text
    byte_string = combined_string.encode('latin1')

    # Compute the MD5 hash
    md5_hash = hashlib.md5(byte_string).hexdigest()
    return md5_hash


prefix = '\123'
suffix = '\043\267\245\157\150\035\211\035\054\362\107\123\071\207\374\301'


# Given string
input_string = r"'\077' + document.login.password.value + '\043\267\245\157\150\035\211\035\054\362\107\123\071\207\374\301'"

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

    
    print("First octal part:", prefix)
    print("Second octal part:", suffix)

    print(generate_password(octal1, 'mekong', octal2))

else:
    print("No match found")

# If you need to keep the strings as actual strings with escape sequences, wrap them in raw strings again


# print(generate_password())