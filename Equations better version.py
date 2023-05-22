problems = ["32 + 698", "3801 - 2", "45 + 43", "1000 + 12"]

solve = True

def equation_formatter(problems):
# Lists to use for the formatting of the equations, line 1 is the first number, line 2 is the operator
# line 3 is the secondnum, and line 5 is the solution
    top_row = ""
    bottom_row = ""
    lines = ""
    sol_row = ""
# error message for too many problems
    if len(problems) > 5:
        return "Error: Too many problems"
# this splits the variables in the list into 2 lists for Line_1 and line_2
    for i in problems:
        firstnum = i.split()[0]
        operator = i.split()[1]
        secondnum = i.split()[2]
# error message does not contain digits
        if firstnum.isdigit():
            pass
        else:
            return "Error: Numbers must only contain digits"
        if secondnum.isdigit():
            pass
        else:
            return "Error: Numbers must only contain digits"
# error message for number length        
        if len(firstnum) > 4:
            return "Error: Numbers cannot be more than four digits"
        if len(secondnum) > 4:
            return "Error: Numbers cannot be more than four digits"
#sets solution, changes to int
        if operator == "+":
            solution = str(int(firstnum)+int(secondnum))
        elif operator == "-":
            solution = str(int(firstnum)-int(secondnum))
        else:
            return "Error: Operator must be '+' or '-'"
# formatting
        fill_dis = max(len(firstnum), len(secondnum))
        top_num = (firstnum.rjust(fill_dis + 2))
        bot_num = (operator + " " + secondnum.rjust(fill_dis))
        line = ((fill_dis + 2)*"_")
        sol_num = (solution.rjust(fill_dis + 2))

        if i != problems[-1]: #this means does not equal the last problem, insanely good to use
            top_row += top_num + "   "
            bottom_row += bot_num + "   "
            lines += line + "   "
            sol_row += sol_num + "   "
        else:
            top_row += top_num
            bottom_row += bot_num
            lines += line
            sol_row += sol_num

    if solve:
        output = str(top_row + "\n" + bottom_row + "\n" + lines + "\n" + sol_row)
    else:
        output = str(top_row + "\n" + bottom_row + "\n" + lines)


    return print(output)
       

equation_formatter(problems)