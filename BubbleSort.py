def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j]<a[i]:
                a[i],a[j]= a[j],a[i]
                count += 1
    print('Array is sorted in {count} swaps.'.format(count = count))
    print('First Element: {elmnt}'.format(elmnt = a[0]))
    print('Last Element: {element}'.format(element = a[-1]))
