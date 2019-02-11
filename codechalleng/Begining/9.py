import string

alphanum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
# ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
def is_alfanumerical(char):
    if char == '':
        return False
    if str(char) in alphanum:
        return True
    return False

def get_index_different_char(chars):
    a_list = []
    nona_list = []
    for index, char in enumerate(chars):

        if is_alfanumerical(char):
            a_list.append((index, char))
        else:
            nona_list.append((index, char))
    if len(a_list) == 1:
        return a_list[0][0]
    else:
        return nona_list[0][0]

inputs = (
    ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
)
for element in inputs:
    response =get_index_different_char(element)
    print(response)
