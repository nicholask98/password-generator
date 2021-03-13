import random

def pass_gen():
    print('FIXME: pass_gen')
    # ASCII A-Z = 65 --> 90
    # ASCII a-z = 97 --> 122
    # ASCII Symbols: '!': 33, '# $ % &': 35 --> 38 
    chars = ['']
    num_chars = random.randint(8, 20)
    for num in range(num_chars):
        

    return -1


def main():
    user_input = ''
    while user_input != '0':
        pass_gen()
        user_input = input('Press enter to regen. 0 to quit\n')
    return -1

main()

# randomizer: mix lowercase, uppercase, nums and symbs
