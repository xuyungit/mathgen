import random
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '×': operator.mul
}

class GenerationException(Exception):
    pass

def generate_int(op1_range: range, op2_range: range, op: str, result_range: range, max_attempts: int = 1000):
    """
    Generates operands for a specified arithmetic operation that result in a valid value within a range.

    Args:
    op1_range (range): The range of possible values for the first operand.
    op2_range (range): The range of possible values for the second operand.
    op (str): The arithmetic operation to perform, either '+', '-', or '*'.
    result_range (range): The range of valid results.
    max_attempts (int): The maximum number of attempts before returning None. Defaults to 1000.

    Returns:
    tuple: A tuple with the operands and the operation if a valid combination is found, otherwise None.
    """
    if op not in ops:
        raise GenerationException('Invalid op!')

    for _ in range(max_attempts):
        op1 = random.choice(op1_range)
        op2 = random.choice(op2_range)

        if op == '+':
            if len(str(op1)) < len(str(op2)):
                op1, op2 = op2, op1
        if op == '-':
            if op1 < op2:
                op1, op2 = op2, op1
        result = ops[op](op1, op2)
        if result in result_range:
            return (op1, op2, op)

    raise GenerationException('Invalid combination')

def generate_int2(op1_range: range, op2_range: range, op: str, result_range: range, max_attempts: int = 1000):
    if op not in ops:
        raise GenerationException('Invalid op!')

    op1_pool = list(range(11, 100)) * 7 + list(range(100, 1000))
    op2_pool = list(range(100, 1000))

    for _ in range(max_attempts):
        op1 = random.choice(op1_pool)
        op2 = random.choice(op2_pool)

        if op == '+':
            if len(str(op1)) < len(str(op2)):
                op1, op2 = op2, op1
        if op == '-':
            if op1 < op2:
                op1, op2 = op2, op1
        result = ops[op](op1, op2)
        if result in result_range:
            return (op1, op2, op)

    raise GenerationException('Invalid combination')

def print_vertical(colums_per_page=4, colume_spaces=6, items_per_page=8, line_spaces=3):
    for _ in range(items_per_page):
        output = [generate_int(range(10, 100), range(10, 100), random.choice(['+', '-']), range(1, 2000)) for _ in range(colums_per_page)]
        line1 = (' ' * colume_spaces).join([f'{item[0]:>6}' for item in output])
        line2 = (' ' * colume_spaces).join([f'{item[2]}{item[1]:>5}' for item in output])
        line3 = (' ' * (colume_spaces - 1)).join([('─' * 7) for _ in output])
        print(line1)
        print(line2)
        print(line3)
        print('\n' * line_spaces)

def print_vertical2(colums_per_page=4, colume_spaces=6, items_per_page=8, line_spaces=3):
    """
    三位数加两位数竖式加法,竖式，加法，不混合，只是加法
    """
    for _ in range(items_per_page):
        output = [generate_int(range(11, 1000), range(11, 1000), random.choice(['+',]), range(1, 2000)) for _ in range(colums_per_page)]
        line1 = (' ' * colume_spaces).join([f'{item[0]:>6}' for item in output])
        line2 = (' ' * colume_spaces).join([f'{item[2]}{item[1]:>5}' for item in output])
        line3 = (' ' * (colume_spaces - 1)).join([('─' * 7) for _ in output])
        print(line1)
        print(line2)
        print(line3)
        print('\n' * line_spaces)

def print_vertical3(colums_per_page=4, colume_spaces=6, items_per_page=8, line_spaces=3):
    for _ in range(items_per_page):
        output = [generate_int(range(10, 1000), range(10, 1000), random.choice(['+', '-']), range(1, 2000)) for _ in range(colums_per_page)]
        line1 = (' ' * colume_spaces).join([f'{item[0]:>6}' for item in output])
        line2 = (' ' * colume_spaces).join([f'{item[2]}{item[1]:>5}' for item in output])
        line3 = (' ' * (colume_spaces - 1)).join([('─' * 7) for _ in output])
        print(line1)
        print(line2)
        print(line3)
        print('\n' * line_spaces)

def print_vertical4(colums_per_page=4, colume_spaces=6, items_per_page=8, line_spaces=3):
    for _ in range(items_per_page):
        output = [generate_int(range(10, 1000), range(10, 1000), random.choice(['+', '-', '×']), range(1, 2000)) for _ in range(colums_per_page)]
        line1 = (' ' * colume_spaces).join([f'{item[0]:>6}' for item in output])
        line2 = (' ' * colume_spaces).join([f'{item[2]}{item[1]:>5}' for item in output])
        line3 = (' ' * (colume_spaces - 1)).join([('─' * 7) for _ in output])
        print(line1)
        print(line2)
        print(line3)
        print('\n' * line_spaces)

def print_vertical5(colums_per_page=4, colume_spaces=6, items_per_page=8, line_spaces=3):
    """
    两位数和三位数加两位数竖式加法,竖式。
    两位数的比例40%
    """
    for _ in range(items_per_page):
        output = [generate_int2(range(11, 1000), range(11, 1000), random.choice(['+',]), range(1, 2000)) for _ in range(colums_per_page)]
        line1 = (' ' * colume_spaces).join([f'{item[0]:>6}' for item in output])
        line2 = (' ' * colume_spaces).join([f'{item[2]}{item[1]:>5}' for item in output])
        line3 = (' ' * (colume_spaces - 1)).join([('─' * 7) for _ in output])
        print(line1)
        print(line2)
        print(line3)
        print('\n' * line_spaces)


for _ in range(80):
    # print_vertical()
    print_vertical5(
        colums_per_page=4,
        colume_spaces=8,
        items_per_page=8,
        line_spaces=2
    )
    print('\f')
