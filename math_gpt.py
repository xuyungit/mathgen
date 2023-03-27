import random

MIN_VALUE = 10
MAX_VALUE = 100
SPACE_BETWEEN_QUESTIONS = 24
QUESTIONS_PER_LINE = 4
LINES_PER_PAGE = 7

def generate_question():
    operators = ['+', '-', '×', '÷']
    operators = ['+', '-']

    a = random.randint(MIN_VALUE, MAX_VALUE)
    b = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(operators)

    if operator == '÷':
        a = a * b
    if operator == '-' and a < b:
        a, b = b, a

    question = f"{a} {operator} {b} = "
    return question
    
def generate_exercise_page(questions_per_line, lines_per_page):
    page = ""

    for line in range(lines_per_page):
        questions_line = ""
        for question_num in range(questions_per_line):
            question = generate_question()
            questions_line += f"{question:<{SPACE_BETWEEN_QUESTIONS}}"
        page += questions_line + "\n" * 6

    return page


def main():
    total_pages = 10

    for i in range(1, total_pages + 1):
        page = generate_exercise_page(QUESTIONS_PER_LINE, LINES_PER_PAGE)
        print(page)
        if i != total_pages:
            print("\f")

if __name__ == "__main__":
    main()