from cipher_qh2231 import cipher_qh2231
import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert isinstance(shift, int), f"Shift should be an integer but got {type(shift)}."
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


def test_cipher_symbol():
    text = 'single!'
    shift = 3
    expected = 'vlqjoh!'
    actual = cipher(text, shift)
    assert actual == expected


    
