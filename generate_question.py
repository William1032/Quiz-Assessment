import random
import quiz as main
class generate:

    solution = 0

    def generate_question():
            print("gen")
            first_part = random.randint(1, 100)
            second_part = random.randint(1, 100)
            operator = random.randint(1, 4)
            if operator == 1:
                solution = first_part + second_part
                question_text = str(first_part) + "+" + str(second_part)
                problem = ("Please enter an answer to the presented question: " + question_text)
            elif operator == 2:
                solution = first_part - second_part
                question_text = str(first_part) + "-" + str(second_part)
                problem = ("Please enter an answer to the presented question: " + question_text)
            elif operator == 3:
                divided = first_part / second_part
                solution = round(divided, 2)
                question_text = str(first_part) + "/" + str(second_part)
                problem = ("Please enter an answer to the presented question: " + question_text)
            elif operator == 4:
                solution = first_part * second_part
                question_text = str(first_part) + "x" + str(second_part)
                problem = ("Please enter an answer to the presented question: " + question_text)
            generate.generate_answer(first_part, second_part, operator)
            return problem, solution
            
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
            
         
