
def extract_substring(s):
    start_idx = s.find('(') + 1  # Find the index of '(' and add 1 to exclude '('
    end_idx = s.find(')', start_idx)  # Find the index of ')' after the start_idx
    if start_idx > 0 and end_idx > start_idx:
        hash_string = s[start_idx:end_idx]
        new_string = hash_string.replace(' + document.login.password.value + ', 'mekong').replace("'",'')
        return new_string
    
    return None  # Return None if '(' or ')' is not found or indices are incorrect


# Example usage
input_string = "hexMD5('\\060' + document.login.password.value + '\\047\\020\\120\\257\\162\\167\\216\\163\\040\\171\\251\\111\\144\\261\\210\\141')"
substring = extract_substring(input_string)

print("Extracted substring:")
print(substring)
