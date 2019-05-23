from textwrap import wrap

def multiply(a, b):
    '''
    multiplies 2 numbers
    '''
    x = a * b
    return x

def descending_order(num):
    '''
    rearranges digits in num so that they're in order from
    largest to lowest
    '''
    numb=str(num)
    nums = list(numb)
    smun = nums.sort(reverse=True)
    mun = "".join(nums)
    mun = int(mun)
    return mun

def getCount(inputStr):
    '''
    given a string, returns number of vowels in it
    '''
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    nospace = inputStr.replace(" ", "")
    for letter in nospace:
        for vowel in vowels:
            if letter == vowel:
                num_vowels += 1
    
    return num_vowels

def song_decoder(song):
    '''
    Given a string with "WUB"s in it, replaces those WUB's
    with spaces so that it's legible
    '''
    spaceSong = song.replace("WUB", " ")
    theSong = " ".join(spaceSong.split())
    return theSong

def even_or_odd(number):
    '''
    returns whether a number is even or odd
    '''
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def find_outlier(integers):
    '''
    given a list of mostly even numbers with one odd number 
    (or vice versa), returns the one odd (or even) number
    '''
    odd = []
    even = []
    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]

def solution(strin):
    '''
    input: string
    output: divide string into pairs of characters 
    (if odd number of characters, last pair gets a '_')
    '''
    r = wrap(strin, 2)
    t = []
    for set in r:
        if len(set) < 2:
            set = f"{set}_"
            t.append(set)
        else: 
            t.append(set)
    return t

def spin_words(sentence):
    '''
    flips all words with 5+ characters in a given string\n
    ex: I'm a goblin => I'm a nilbog
    '''
    x = sentence.split()
    y = []
    for word in x:
        if len(word) >= 5:
            y.append(word[::-1])
        else:
            y.append(word)
    z = " ".join(y)
    return z

def narcissistic(value):
    '''
    each digit in value is raised to the power of the 
    length of value and added together. If this 
    sum == value, returns true
    '''
    val = str(value)
    numlen = len(val)
    sum = 0
    for num in val:
        num = int(num)
        sum += num**numlen
    if sum == value:
        return True
    else: 
        return False
