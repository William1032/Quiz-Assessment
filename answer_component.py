def generate_answer(first_part, second_part, operator):
        if operator == 1:
            solution = first_part + second_part
            
        elif operator == 2:
            solution = first_part - second_part

        elif operator == 3:
            divided = first_part / second_part
            solution = round(divided, 2)

        elif operator == 4:
            solution = first_part * second_part
        print(solution)
        return solution