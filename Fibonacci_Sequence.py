# generate fibonacchi sequence


def fibonacchi_seq(n):
    a = 0
    b = 1
    print(b)
    for i in range(n-1):
        out = a + b
        print(out)
        a = b
        b = out


if __name__ == '__main__':
    fibonacchi_seq(5)

'''
0 1 1 2 3 5

a b out 
0 1 1
1 1 2
1 2 3
'''