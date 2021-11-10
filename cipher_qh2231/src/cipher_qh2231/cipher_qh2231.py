def cipher(text, shift, encrypt=True):
    
    '''
    Caesar cipher. Encrypts text by replacing each letter by a letter some fixed number of positions down the alphabet.

    Parameters
    ----------
    text : string
      A string you want to encrypt.
    shift : integer
      The number of positions down the alphabet you want the text to be transformed. 
            encrypt : boolean 
        True - encrypt (default)
        False - decrypt
      

    Returns
    -------
    string
      The new encrypted or decrypted text.

    Examples
    --------
    >>> from cipher_qh2231 import cipher
    >>> cipher('abc',1, True)
    bcd
    >>> cipher('bcd',1, False)
    abc
    '''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
