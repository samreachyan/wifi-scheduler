import hashlib
import re

hash = '\326mekong\367\334\031\050\347\117\013\027\332\040\370\251\270\265\102\136'

pref = '\157'
suff = '\347\070\206\077\023\135\264\241\261\120\144\150\066\027\022\240'
mid = 'mekong'

# Function to convert octal escape sequences to hexadecimal escape sequences
def octal_to_hex(string):
    # Find all octal escape sequences
    octal_escapes = re.findall(r'\\[0-3]?[0-7]{1,2}', string)
    hex_string = string

    for octal_escape in octal_escapes:
        # Convert octal escape to integer
        octal_value = int(octal_escape[1:], 8)
        # Convert integer to hexadecimal escape sequence
        hex_escape = f'\\x{octal_value:02x}'
        # Replace octal escape with hexadecimal escape in the string
        hex_string = hex_string.replace(octal_escape, hex_escape)

    print(hex_string)
    return hex_string


# Generate Hashed Password
def generate_password(combined_string):    
    # Combine the components into a single byte string
    # combined_string = prefix + password + suffix

    # Convert the combined string into a byte array, interpreting it as Latin-1 encoded text
    byte_string = combined_string.encode('latin1')

    # Compute the MD5 hash
    md5_hash = hashlib.md5(byte_string).hexdigest()
    return md5_hash

octal_to_hex(pref)
octal_to_hex(suff)
print(suff)

# new_hash = octal_to_hex(hash)
# print(new_hash)
print(generate_password(pref + mid + suff))