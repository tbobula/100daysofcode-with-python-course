from string import punctuation

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    string = []
    for char in input_string:
        if char in punctuation:
            continue
        string.append(char)
    return "".join(string)
