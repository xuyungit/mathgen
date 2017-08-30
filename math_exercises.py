import random
import operator

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


rtf_page_break = r'\page '


ops = {
    '+': operator.__add__,
    '-': operator.__sub__,
    '*': operator.__mul__
}


def gen_type0():
    """
    Return an operation 'a op b = ' where
    * 1 <= a <= 9
    * 1 <= b <= 9
    * op is '+' or '-'
    * 0 < a op b <= 10
    """
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    op = random.choice('+-')

    if 0 < ops[op](a, b) <= 10:
        return '%2d %s %2d = ' % (a, op, b)
    else:
        return gen_type0()

def gen_type1(max_result=20):
    """
    Return an operation 'a op b = ' where
    * 1 <= a <= 19
    * 1 <= b <= 19
    * op is '+' or '-'
    * 0 < a op b <= max_result
    * if op is '+' then ones_a + ones_b >= 10
    * if op is '-' then ones_a < ones_b
    """
    a = random.randint(1, max_result)
    b = random.randint(1, max_result)
    op = random.choice('+-')
    ones_a = a % 10
    ones_b = b % 10
    if 0 < ops[op](a, b) <= max_result and \
        (ops[op](ones_a, ones_b) >= 10 or ops[op](ones_a, ones_b) < 0):
        return '%2d %s %2d = ' % (a, op, b)
    return gen_type1(max_result)


def gen_type2(max_result=100):
    """
    Return an operation 'a op b = ' where
    * a is times of 10
    * b is times of 10
    * op is '+' or '-'
    * a op b <= max_result
    """
    max_times = max_result / 10 - 1

    a = random.randint(1, max_times) * 10
    b = random.randint(1, max_times) * 10
    op = random.choice('+-')

    if 0 < ops[op](a, b) <= max_result:
        return '%2d %s %2d = ' % (a, op, b)
    else:
        return gen_type2(max_result)

def gen_type3(max_result=100):
    """
    Return an operation 'a op b = ' where
    * 1 <= a < 100
    * 1 <= b < 100
    * either a or b is less than 10
    * either a or b is larger than 20
    * if op is '+' then ones_a + ones_b >= 10
    * if op is '-' then ones_a < ones_b
    * op is '+' or '-'
    * 0 < a op b <= 100
    """
    a = random.randrange(1, max_result)
    b = random.randrange(1, max_result)
    op_symbol = random.choice('+-')
    op = ops[op_symbol]
    ones_a = a % 10
    ones_b = b % 10

    if (a < 10 or b < 10) and (a > 20 or b > 20) and 0 < op(a, b) <= max_result:
        if op(ones_a, ones_b) >=10 or op(ones_a, ones_b) < 0:
            return '%2d %s %2d = ' % (a, op_symbol, b)
    return gen_type3(max_result)

def gen_type4():
    """
    Return an expression 'a * b = ' where
    * 1 <= a <= 9
    * 1 <= b <= 9
    """
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    return '%2d * %2d = ' % (a, b)

def gen_divide_type0():
    """
    * return an operation 'a / b = ' where
    * 1 < b <= 9
    * 1 < a / b <= 9
    """
    b = random.randrange(2, 10)
    prod = random.randrange( 2, 10) * b
    return '%2d / %2d = '  % (prod, b)

nbr_per_exercises = 80
nbr_per_file = 30
nbr_file = 20

total_exercises = nbr_per_exercises * nbr_per_file * nbr_file

gens = {
    gen_type1: int(0.35 * total_exercises),
    gen_type2: int(0.08 * total_exercises),
    gen_type3: int(0.15 * total_exercises),
    gen_type0: int(0.02 * total_exercises),
    gen_type4: int(0.2 * total_exercises),
    gen_divide_type0: int(0.2 * total_exercises),
}

all_exercises = []

for gen, nbr in gens.items():
    all_exercises.extend([gen() for i in range(nbr)])

def do(filename):
    with open(filename, 'wb') as f:
        f.write(rtf_header)
        for page in range(1, nbr_per_file):
            f.write(rtf_page_header_template % page)
            for i in range(0, nbr_per_exercises / 4):
                spaces = ' ' * 5
                exercises_a_line = [random.choice(all_exercises) for _ in range(4)]
                a_line = spaces.join(exercises_a_line)
                output_line = rtf_a_line_template % a_line
                output_line = output_line.replace('*', r"\'d7")
                output_line = output_line.replace('/', r"\'f7")
                f.write(output_line)
            f.write(rtf_page_tail)

        f.write(rtf_tail)

for i in range(1, nbr_file + 1):
    do(r'calculation_%d.rtf' % i)
