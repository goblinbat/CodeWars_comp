import math

def get_middle(s):
    '''
    returns middle character of a string \n
    if odd length, return single character \n
    if even length, return two characters
    '''
    x = len(s)
    y = x/2
    if x == 1 or x == 2:
        return s
    elif x % 2 == 0:
        z = "".join([s[y-1], s[y]])
        return z
    else:
        return s[y]

def opposite_num(number):
    return (number * -1)

def stammer(s):
    '''
    Takes in string, returns string with a stammer, 
    with each word having one more stammer than the previous
    '''
    x = 0
    lis = []
    for letter in s:
        set = []
        for y in range(x):
            set.append(letter.lower())
        set = "".join(set)
        lis.append(f"{letter.upper()}{set}")
        x += 1
    return "-".join(lis)

def find_odd_repeat_int(seq):
    '''
    Given a list of repeating numbers in which 
    only one of them is repeated an odd number of times,
    returns that number
    '''
    for num in seq:
        many = seq.count(num)
        if many % 2 != 0:
            return num

def high_and_low(numbers):
    '''
    Takes in a string of numbers, then returns 
    highest and lowest numbers (as a string)
    '''
    nums = numbers.split(" ")
    numbers = []
    for num in nums: 
        numbers.append(int(num))
    big = str(max(numbers))
    small = str(min(numbers))
    string = " ".join([big, small])
    return string

def disemvowel(string):
    '''
    Removes vowels from a string
    '''
    vowels = 'aeiouAEIOU'
    strng = []
    for letter in string:
        if letter not in vowels:
            strng.append(letter)
    strng = "".join(strng)
    return strng

def is_square(n):    
    '''
    returns whether a given number is a perfect square \n
    ex: 16 = True, 8 = False
    '''
    if n < 0:
        return False
    elif n == 0:
        return True
    m = math.sqrt(n)
    if m.is_integer():
        return True
    else:
        return False

def square_digits(num):
    '''
    squares each digit in a number \n
    ex: 374 => 3, 7, 4 => 9, 49, 16 => 94916
    '''
    num = str(num)
    squared = []
    for n in num:
        n = int(n)
        m = str(n*n)
        squared.append(m)
    return int("".join(squared))

def find_short_word(s):
    '''
    returns shortest word from a string
    '''
    splt = s.split(" ")
    length = []
    for word in splt:
        length.append(len(word))
    l = min(length)
    return l
