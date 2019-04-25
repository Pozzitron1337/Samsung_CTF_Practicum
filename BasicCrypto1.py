def caesar(text, shift):
    result=''
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(text)):
        if text[i].isupper():
            result = result+ALPHABET[(ALPHABET.find(text[i]) + shift) % len(ALPHABET)]
        else:
            result = result + alphabet[(alphabet.find(text[i]) + shift) % len(alphabet)]
    return result


cyphertext = 'ZkZjEfkTcrjjztrcTrvjriTzgyvi'
shift = 9

print(caesar(cyphertext , shift))