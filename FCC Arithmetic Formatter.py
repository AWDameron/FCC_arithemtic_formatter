def arithmetic_arranger(problems, show_answers=False):
    answers = []

    if len(problems) > 5:
        return print("Error: Too many problems.")
    
    top_numbers, operators, bottom_numbers = sort_arithmetic(problems)
    answers = solve_arithmetic(top_numbers,operators,bottom_numbers)
    print_arithmetic(top_numbers,operators,bottom_numbers,answers)
    
    if show_answers:
        print('   '.join(answer_strings))
    
    return

# Wanted to use OOP principles and break out more complicated methods and keep them seperate
# This function is designed to take the initial list [problems] and break it into 3 seperate lists.
# It also doubles as my validation method to make sure the data that is input meets FCC's projects requirements.
def sort_arithmetic(problems):
    top_numbers = []
    operators = []
    bottom_numbers = []
    
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
    

    return top_numbers,operators,bottom_numbers

# This method is designed to just simply get the answers for the math problems, in the future I am going to
# go back through and make this and sort_arithmetic() a single function
def solve_arithmetic(top_numbers,operators,bottom_numbers):
    answers = []
    problem = 0
    top_numbers = [int(top) for top in top_numbers]
    bottom_numbers = [int(bot) for bot in bottom_numbers]
    while problem <= len(top_numbers)-1:
        if operators[problem] == "+":
            answers.append(str(top_numbers[problem] + bottom_numbers[problem]))
        else: 
            answers.append(str(top_numbers[problem] - bottom_numbers[problem]))
        problem += 1
         
  
    return answers

# This method simply prints out all of the information.  Originally I had several different for/while but learned about
# python's zip method, which is a great time saver.
def print_arithmetic(top_numbers,operators,bottom_numbers,answers):
    top_strings = []
    bottom_strings = []
    answer_strings = []
    dashes = []
    x = 0

    for top, op, bot,ans in zip(top_numbers, operators, bottom_numbers,answers):
        width = max(len(top), len(bot)) + 2
        
        top_strings.append(f"{top:>{width}}")
        bottom_strings.append(f"{op} {bot:>{width-2}}")
        dashes.append('-' * width) 
        answer_strings.append(f"{ans:>{width}}")
    

    print('    '.join(top_strings))
    print('    '.join(bottom_strings))
    print('    '.join(dashes))
 
    return answer_strings
        
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])