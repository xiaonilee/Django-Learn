import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = 'asqwerfychgnktofmaltm172839495060ZASDTYBBKOLJUOLKM'

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code