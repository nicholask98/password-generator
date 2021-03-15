import random

def pass_gen():
    chars = []
    num_chars = random.randint(8, 20)
    for num in range(num_chars):
        current_char = random.randint(0, 66)
        if current_char == 0:
            chars.append(chr(33)) # adds exclamation point
        elif current_char <= 4:
            chars.append(chr(current_char + 34)) # adds other symbols
        elif current_char <= 30:
            chars.append(chr(current_char + 60)) # adds capital letters
        elif current_char <= 56:
            chars.append(chr(current_char + 66)) # adds lowercase letters
        else:
            chars.append(str(current_char - 57)) # adds digits
    chars = ''.join(chars)
    print(chars)

    return -1


def main():
    user_input = ''
    while user_input != '0':
        pass_gen()
        user_input = input('Press enter to regen. 0 to quit\n')
    return -1

main()
