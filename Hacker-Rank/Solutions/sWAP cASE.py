def swap_case(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char == char.upper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
            continue
    return result
