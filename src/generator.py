import random
import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!#$%&()*+,-./:;<=>?@[]^_`{|}~'

def gen(length):
    password = ''.join(random.choice(chars) for i in range(length))
    password.strip(' ')
    return str(password)