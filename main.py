import fibonacciseries


def main():
    num = int(input('enter a number:'))
    series = fibonacciseries.fibonacci_series(num)

    if series is None:
        print('invalid oinput, enter positive number.')

    print(series)

main()