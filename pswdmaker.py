import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(15)
print(random_string)
