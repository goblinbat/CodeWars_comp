
def xo(s):
    '''
    tests if string contains same number of x's and o's\n
    could potentially refactor so it can test if it has same number 
    of given characters (rathers than x + o specifically)
    '''
    x = 0
    o = 0
    for letter in s:
        letter = letter.lower()
        if letter == 'x':
            x += 1
        elif letter == 'o':
            o += 1
    if x == o:
        return True
    else:
        return False

def to_cap_case(string):
    '''
    Capitalizes first letter of each word in a string
    '''
    strng = string.split()
    mix = []
    for word in strng: 
        word = word.capitalize()
        mix.append(word)
    return(" ".join(mix))