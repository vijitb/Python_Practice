"""Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach 1 using the following
process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. """


def collatz_conjecture(n):
    step = 1
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n / 2
            step += 1
        else:
            n = (n * 3) + 1
            step += 1

    return step


if __name__ == '__main__':
    while True:
        try:
            user_input = int(input('Please enter a number > 1: '))
        except ValueError:
            print('Invalid Input!')
            continue
        else:
            if user_input < 1:
                print('Wrong Input. Value is less than 1!')
                continue
            else:
                result: int = collatz_conjecture(int(user_input))
                print(f'Number of steps: {result}')
                break
