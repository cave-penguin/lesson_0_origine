import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f"Successful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error("Dont divided by zero")
        return 0


# def add(a, b):
#     return a**2 + b**2


def sqrt(a):
    try:
        logging.info(f'Successful square {a} ** 0.5')
        return a**0.5
    except Exception as ex:
        logging.error(ex)
        return 0



def pow(a, b):
    return a**b


if __name__ == "__main__":
    # logging.debug('qw')
    # logging.info('we')
    # logging.warning('er')
    # logging.error('rt')
    # logging.critical('ty')
    
    logging.basicConfig(
        level=logging.INFO,
        filemode="w",
        filename="module12\py.log",
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    # print(div(5, 7))
    # print(div(5, 0))


    print(sqrt(3))
    print(sqrt(-32))
