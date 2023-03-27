import random
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
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

        result = ops[op](op1, op2)
        if result in result_range:
            return (op1, op2, op)
    
    raise GenerationException('Invalid combination')

def output_to_rtf_file(filename: str, line_gen, line_spaces, nbr_lines_per_page, nbr_pages):
    rtf_header = r'''{\rtf1\ansi\ansicpg936\deff0{\fonttbl{\f0\fnil Courier New;}{\f1\fnil\fcharset134 SimSun;}{\f2\fnil SimSun;}}
{\*\generator Msftedit 5.41.21.2510;}\viewkind4\uc1
'''

    rtf_tail = r'''
}
'''

    rtf_page_header_template = r'''\pard\lang2052\f1\sa200\sl376\slmult1\qc\'bf\'da\'cb\'e3\'c1\'b7\'cf\'b0 \lang1033\f2 %d\f3\par
\pard\sa200\sl426\slmult1\lang9\f0\fs26
'''

    rtf_page_tail = r'''\par
\lang2052\f1\'d0\'d5\'c3\'fb\'a3\'ba             \'d7\'f6\'b6\'d4\'a3\'ba             \'d3\'c3\'ca\'b1\'a3\'ba    \'b7\'d6    \'c3\'eb\lang1033\f2\par
\page
'''
    rtf_a_line_template = r'%s  \line '

    # rtf_page_break = r'\page '

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rtf_header)
        for page in range(1, nbr_pages):
            f.write(rtf_page_header_template % page)
            for _ in range(0, nbr_lines_per_page):
                a_line = next(line_gen)
                output_line = rtf_a_line_template % a_line
                output_line = output_line.replace('*', r"\'d7")
                output_line = output_line.replace('/', r"\'f7")
                f.write(output_line)
                for _ in range(line_spaces):
                    f.write(rtf_a_line_template % '')
            f.write(rtf_page_tail)

        f.write(rtf_tail)

def get_a_line():
    for _ in range(10000):
        exps = []
        for _ in range(4):
            op1, op2, op = generate_int(
                op1_range=range(10, 100),
                op2_range=range(10, 100),
                op='+',
                result_range=range(0,200)
            )
            exps.append(f'{op1} {op} {op2} = ')
        yield '       '.join(exps)

if __name__ == '__main__':
    print(generate_int(
        op1_range=range(10, 100),
        op2_range=range(10, 100),
        op='+',
        result_range=range(0,200)
    ))
    line_gen = get_a_line()
    output_to_rtf_file('test.rtf', line_gen, 4, 6, 3)
