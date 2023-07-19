if __name__ == '__main__':
    N = int(input(''))
    lists = []
    printable = []
    for i in range(N):
        command = input('').split()
        if command[0] == 'insert':
            lists.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            list2 = list(map(int, lists))
            printable.append(list2)
        elif command[0] == 'remove':
            lists.remove(int(command[1]))
        elif command[0] == 'append':
            lists.append(int(command[1]))
        elif command[0] == 'sort':
            lists.sort()
        elif command[0] == 'pop':
            lists.pop()
        elif command[0] == 'reverse':
            lists.reverse()
    for i in range(len(printable)):
        print(printable[i])
