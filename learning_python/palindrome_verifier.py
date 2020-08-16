''' Verify if the input phrase is a palindrome '''

print('\nPALINDROME VERIFIER\n')

phrase = str(input('Type a phrase you want to verify: ')).strip().lower()

def prepare_phrase_for_validation(phrase):
    separate_words = phrase.split()
    words_together = ''.join(separate_words)
    return words_together

def verify_if_is_palindrome(prepared_word):
    reverse_phrase = ''

    for letter in range(len(prepared_word) -1, -1, -1):
        reverse_phrase += prepared_word[letter]
    print(f'{prepared_word}, {reverse_phrase}')

    if prepared_word == reverse_phrase:
        print('\nIt\'s a palindrome!\n')

    else:
        print('\nIsn\'t a palindrome!\n')

prepared_word = prepare_phrase_for_validation(phrase)
verify_if_is_palindrome(prepared_word)
