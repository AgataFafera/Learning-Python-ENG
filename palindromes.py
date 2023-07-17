def remove_whitespace_punctuation(text):
    text = text.replace(" ", "")
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def palindrome(word):
    #clean_str = remove_whitespace_punctuation(word).lower()
    clean_str = ''.join( [ char for char in word if char not in string.punctuation+' ' ] )
    reversed_str = clean_str[::-1]
    if reversed_str == clean_str:
        return True 
    return False

word_input = input("Type word you want to check: ")
print(palindrome(word_input))
