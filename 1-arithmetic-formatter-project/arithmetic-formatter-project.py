def arithmetic_arranger(problems, show_answers=False):

    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems: 
        parts = problem.split(' ')

        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Validate the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Ensure both operands are numbers
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Ensure numbers are no more than four digits long
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width for formatting
        width = max(len(num1), len(num2)) + 2

        # Format the problem lines
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))  # Fix: Removed extra space
        dashes.append("-" * width)

        # Compute and store the result if show_answers is True
        if show_answers:
            result = str(eval(num1 + operator + num2))  # Fix: Ensuring eval uses valid numbers
            results.append(result.rjust(width))

    # Join and format the output
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)

    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print("\n")
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print("\n")
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print("\n")
