def swap_case(s):
    new_itteration = []
    for i in s:
        if i.islower():
            new_itteration.append(i.upper())
        elif i.isupper():
            new_itteration.append(i.lower())
        else:
            new_itteration.append(i)
    word = ''.join([str(x)for x in new_itteration])
    return word 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
