import re
import hashlib

prefix = '\272'
suffix = '\043\267\245\157\150\035\211\035\054\362\107\123\071\207\374\301'
password = 'mekong'


# Generate Hashed Password
def generate_password1(prefix, suffix): 
    print(type(prefix))
    # print(prefix, password, suffix)   
    combined_string = prefix + password + suffix
    print(combined_string)

    # Convert the combined string into a byte array, interpreting it as Latin-1 encoded text
    byte_string = combined_string.encode('latin1')

    # Compute the MD5 hash
    md5_hash = hashlib.md5(byte_string).hexdigest()
    return md5_hash


# Given string
input_string = r"'\061' + document.login.password.value + '\201\043\065\202\022\007\361\212\041\176\210\226\301\017\232\066'"

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

    print(generate_password1(decoded_prefix, decoded_suffix))

else:
    print("No match found")

