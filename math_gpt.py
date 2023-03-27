import random

def generate_question():
    operators = ['+', '-', '×', '÷']
    operators = ['+', '-']

    a = random.randint(10, 100)
    b = random.randint(10, 100)
    operator = random.choice(operators)

    if operator == '÷':
        a = a * b
    if operator == '-' and a < b:
        a, b = b, a

    question = f"{a} {operator} {b} = "
    return question

def generate_exercise_page(page_num, questions_per_line, lines_per_page):
    # page = f"第 {page_num} 页\n\n"
    page = ""

    for line in range(lines_per_page):
        questions_line = ""
        for q in range(questions_per_line):
            question = generate_question()
            questions_line += f"{question:<24}"
        page += questions_line + "\n\n\n\n\n\n"

    return page

def main():
    total_pages = 10
    questions_per_line = 4
    lines_per_page = 7

    for i in range(1, total_pages + 1):
        page = generate_exercise_page(i, questions_per_line, lines_per_page)
        print(page)
        if i != total_pages:
            print("\f")

if __name__ == "__main__":
    main()