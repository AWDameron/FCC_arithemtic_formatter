def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return print("Error: Too many problems.")
    
    top_numbers, operators, bottom_numbers, dashes = sort_arithmetic(problems)
    answers = solve_arithmetic(top_numbers,operators,bottom_numbers)
    
    print('    '.join(top_numbers))
    print('    '.join(operators))
    print('    '.join(bottom_numbers))
    print('    '.join(dashes))
    print('    '.join(str(answers)))

    return
    
def sort_arithmetic(problems):
    top_numbers = []
    operators = []
    bottom_numbers = []
    dashes = []
    x = 0
    y = 0


    for problem in problems:
        top,op,bot = problem.split()

        if not top.isdigit() or not bot.isdigit():
            return "Error: Numbers not only contain digits."

        if op not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        
        if len(top) > 4 or len(bot) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        top_numbers.append(top)
        operators.append(op)
        bottom_numbers.append(bot)
        
        while y < len(top_numbers):
            width = max(len(top_numbers[y]),len(bottom_numbers[y])) + 2
            dashes.append('-' * width)
            y += 1


    return top_numbers,operators,bottom_numbers,dashes

def solve_arithmetic(top_number,operator,bottom_number):
    answers = []
    problem = 0
    top_number = [int(top) for top in top_number]
    bottom_number = [int(bot) for bot in bottom_number]
    while problem < len(top_number):
        if operator[problem] == "+":
            answers.append(top_number[problem] + bottom_number[problem])
        else: 
            answers.append(top_number[problem] - bottom_number[problem])
        problem += 1
         
  
    return answers
    
  
        

 # "0 1 2", "3 4 5", "6 7 8", "9 10 11", "12 13 14"   
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])