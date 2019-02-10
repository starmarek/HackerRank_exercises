if __name__ == '__main__':

    L = []
    for _ in range(int(input())):
        s = input().split()
        f = s[0]
        ar = s[1:]

        if f != 'print':
            f += '(' + ','.join(ar) + ')'
            eval('L.' + f)
        elif f == 'print':
            print(L)


