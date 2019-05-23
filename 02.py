
def tribonacci(signature, n):
    '''
    input: set of starting numbers, how many numbers you want returned\n
    output: the original sequence (unless n < len(signature)), 
    plus continuation in which the last 3 numbers in sequence 
    are added together and added to sequence (repeat until 
    len(sequence) = n)
    '''
    seq = []
    if n == 0:
        return seq
    else:
        for num in signature:
            if len(seq) != n:
                seq.append(num)
        while len(seq) < n:
            x = sum(seq[-3:])
            seq.append(x)
        return seq

def find_uniq(arr):
    '''
    given list of repeating numbers, returns the one number that
    is not repeated
    '''
    x = arr[0]
    y = arr[1]
    z = arr [2]
    if x != y and y == z:
        return x
    elif x == y and x != z:
        return z
    elif x != y and y != z:
        return y
    else:
        for num in arr:
            if num != x:
                return num

def likes(names):
    '''
    given a list of names, returns up to the first 3
    names 
    '''
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

def persistence(n):
    '''
    given a number, multiplies its digits together,
    then multiplies the digits of the product until a 
    single digit product is produced. \n
    Returns the number of times it was multiplied
    '''
    m = str(n)
    inst = 0
    if len(m) == 1:
        return 0
    while len(m) > 1:
        product = 1
        for num in m:
            num = int(num)
            product *= num
        inst += 1
        m = str(product)
    return inst

def fizzbuzz_solution_ex(number):
    '''
    given a number, returns the sum of all multiples of 
    3 or 5 less than that number (not inclusive)
    ex: 15 => 3 + 5 + 6 + 9 + 10 + 12 => 45
    '''
    add = []
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            add.append(num)
    return sum(add)

def fizzbuzz_solution_inc(number):
    '''
    given a number, returns the sum of all multiples of 
    3 or 5 less than or equal to that number (inclusive)
    ex: 15 => 3 + 5 + 6 + 9 + 10 + 12 + 15 => 60
    '''
    add = []
    for num in range(number+1):
        if num % 3 == 0 or num % 5 == 0:
            add.append(num)
    return sum(add)

def comp_DNA_strand(dna):
    '''
    returns complementary dna strand
    '''
    comp = []
    for base in dna:
        if base == "A":
            comp.append("T")
        elif base == "C":
            comp.append("G")
        elif base == "G":
            comp.append("C")
        elif base == "T":
            comp.append("A")
    comp_strand = "".join(comp)
    return comp_strand
