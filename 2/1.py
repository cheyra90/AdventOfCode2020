import re

fp = '2/input.txt'
dat = open(fp).read().strip().split('\n')

def is_valid(p1, p2, L, S):
    if S[p1-1] == L:
        if S[p2-1] != L:
            return True
    elif S[p2-1] == L:
        if S[p1-1] != L:
            return True
    return False   


i = 0

for row in dat:
    pwd = re.search(r'(\w+)$', row)[0]
    ltr = re.search(r'.{1}(?=:)', row)[0]
    n1 = int(re.findall(r'(\d+)', row)[0])
    n2 = int(re.findall(r'(\d+)', row)[1])

    if is_valid(n1, n2, ltr, pwd):
        i += 1

print(i)