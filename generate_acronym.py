import re


# defining function to take string as an input and generate acronym
def get_acronym(text):
    acronym = ''
    pattern = r'^\d'
    for word in text.split(' '):
        if not re.search(pattern, word):
            acronym = acronym + word[0].upper()
        else:
            return 'ERROR! Numbers found at the beginning of a word!'
    return acronym


# main code
if __name__ == '__main__':
    user_input = input('Enter a string to generate acronym for: ')
    result = get_acronym(user_input)
    print(f'Generated acronym: {result}')
