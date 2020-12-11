#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    state = False
    oper = "+-*/"
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        for operators in oper:
            if operators == sys.argv[2]:
                print('{} + {} = {}'.format(a, b, add(a, b)))
                state = True
                break
            if operators == sys.argv[2]:
                print('{} - {} = {}'.format(a, b, sub(a, b)))
                state = True
                break
            if operators == sys.argv[2]:
                print('{} * {} = {}'.format(a, b, mul(a, b)))
                state = True
                break
            if operators == sys.argv[2]:
                print('{} / {} = {}'.format(a, b, div(a, b)))
                state = True
                break
        if not state:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
