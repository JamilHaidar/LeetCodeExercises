import string
def find_start_base(num):
    zero_exists = False
    min_base = 1
    for digit in num:
        digit = int(digit,36)+1
        if digit==1:zero_exists = True
        if digit>min_base:min_base = digit
    if min_base == 2 and zero_exists:return 2
    if min_base == 2 and not zero_exists: return 1
    return min_base
def convert_to_int(num,base):
    if base == 1: return len(str(num))
    else: return int(num,base)

def test_operand(p,a,b,c):
    if p=='+': return a+b==c
    elif p=='-': return a-b==c
    elif p=='*': return a*b==c
    else: return a/b==c and a%b==0

t = int(input())
base_mapping = list(range(1,10))+list(string.ascii_lowercase) + [0]
for _ in range(t):
    a,p,b,_,c = input().split()
    start_base = max(find_start_base(a),find_start_base(b),find_start_base(c))
    possible_bases = ''
    possible = False
    for test_base in range(start_base,37):
        if test_operand(p,convert_to_int(a,test_base),convert_to_int(b,test_base),convert_to_int(c,test_base)):
            possible = True
            possible_bases += str(base_mapping[test_base-1])
    if not possible: print('invalid')
    else: print(possible_bases)