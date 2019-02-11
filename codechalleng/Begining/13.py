from string import ascii_uppercase, digits
from random import choice

def gen_string(chars_per_part):
    characters = []
    ALFABET = ascii_uppercase + digits
    for a in range(chars_per_part):
        characters.append(choice(ALFABET))
    return "".join(characters)

def gen_key(parts=4, chars_per_part=8):
    part_list = []
    for part in range(parts):
        part_list.append(gen_string(chars_per_part))
    return "-".join(part_list)



