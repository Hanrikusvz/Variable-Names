import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_strings(num_strings):
    min_length = 12
    max_length = 18

    strings = set()
    while len(strings) < num_strings:
        length = random.randint(min_length, max_length)
        new_string = generate_random_string(length)
        strings.add(new_string)

    return strings


unique_strings = generate_unique_strings(5)


for string in unique_strings:
    print(string)
