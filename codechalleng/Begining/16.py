INDENTS = 4

poem = """
        Remember me when I am gone away,
        Gone far away into the silent land;
        When you can no more hold me by the hand,
        
        Nor I half turn to go yet turning stay.
        
        Remember me when no more day by day
        You tell me of our future that you planned:
        Only remember me; you understand
"""

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_format(indent, line):
    print('{}{}'.format(indent, line))


def print_hanging_indents(poem):
    lista = poem.split("\n")
    indent = False
    for line in lista:
        if line == '':
            indent = False
            continue
        if not indent:
            print_format(indent='', line=line.strip())
            indent = True
            continue
        if indent:
            print_format(indent=INDENTS * ' ', line=line.strip())
            continue


print_hanging_indents(shakespeare_unformatted)
