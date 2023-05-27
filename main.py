def check_if_palindrome(word: str):
    '''
    Cheks if given word is a palindrome.
    Arguments:
    word:   checked word
    '''
    assert isinstance(word, str), 'Please insert string!'
    if word == word[::-1]:
        return True
    else:
        return False