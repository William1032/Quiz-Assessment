import random
import quiz as main
class generate:

    solution = 0

    def generate_question():
            print("gen")
            #create the first and second numbers in the calculation
            first_part = random.randint(1, 100)
            second_part = random.randint(1, 100)
            #pick whether to add, subtract, multiply, or divide then turn it into text 
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
            #return the problem, solution, and text to display to the main file
            return problem, solution, question_text
            
            #cheating for test purposes gives me the answer
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
            
         
