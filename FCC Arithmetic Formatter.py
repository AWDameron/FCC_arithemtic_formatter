def arithmetic_arranger(problems, show_answers=False):
    answers = []

    if len(problems) > 5:
        print("Error: Too many problems.")
    
    result = sort_arithmetic(problems)
    if result is None:
        return
    
    top_numbers, operators, bottom_numbers = sort_arithmetic(problems)    
    answers = solve_arithmetic(top_numbers,operators,bottom_numbers)
    answer_strings = print_arithmetic(top_numbers,operators,bottom_numbers,answers)
    
    if show_answers:
        print('    '.join(answer_strings))
    
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
            print("Error: Numbers not only contain digits.")
            return 

        if op not in ["+","-"]:
            print("Error: Operator must be '+' or '-'.")
            return 
        
        if len(top) > 4 or len(bot) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return 
        
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

# class for throwing errors.
class ArithmeticError(Exception):
    pass

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) 
arithmetic_arranger(["3801 - 2", "123 + 49"])
arithmetic_arranger(["1 + 2", "1 - 9380"])
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) 
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["3 + 855", "988 + 40"], True)
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)