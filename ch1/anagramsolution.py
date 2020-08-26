def anagramsolution(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillok = True
    while pos1 < len(s1) and stillok: #raverse s1
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillok = False
            break
        pos1 += 1
    return stillok

def anagramSolution2(s1, s2):
    alist = list(s1)
    blist = list(s2)

    alist.sort()
    blist.sort()
    pos = 0
    match = True
    while pos < len(s1) and match:
        if alist[pos] == blist[pos] and match:
            pos += 1
        else:
            match = False
            break
    return match
def anagramsolution3(s1, s2):  # count alphabet
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):       # c1 alpha
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillok = True
    while j < 26 and stillok:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillok = False
            break
    return stillok

print(anagramsolution('abcd', 'dbac'))

print(anagramSolution2('python', 'typhon'))