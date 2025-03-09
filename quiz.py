from tkinter import *
import random


class Quiz():

    def __init__(self):
        

        #previous list
        self.question_history = []
        """
        quiz gui
        """
        #window
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        #heading
        self.quiz_heading = Label(self.quiz_frame, text="Temperature Converter", font=("Arial", "20", "bold"))
        self.quiz_heading.grid(row=0)

        #instructions
        instructions = "hello"
        self.quiz_instructions = Label(self.quiz_frame, text=instructions, wraplength=250, width=40, justify="center", font=("Arial", "14", "bold"))
        self.quiz_instructions.grid(row=1)

        #entry field
        self.quiz_entry = Entry(self.quiz_frame, font=("Arial", "14"))
        self.quiz_entry.grid(row=2, padx=10, pady=10)
        solution = 1

        #errors
        error = ""
        self.answer_error = Label(self.quiz_frame, text=error, fg="#9C0000", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        #conversion, help, and history
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        #button list (text/bg color/command/row/column)
        button_details_list = [
            ["Submit Answer", "#990099", lambda:self.check_input(), 0, 1],
            ["To Fahrenheit", "#009900", "", 1, 0],
            ["Info / Help", "#CC6600", "", 1, 1],
            ["History / Export", "#004C99", lambda:self.history(self.all_calculations_list), 1, 2]
        ]

        #hold the buttons
        self.button_ref_list = []

        #create buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF", font=("Arial", "12", "bold"),
                                       width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    
        
    def check_input(self):

        #get input
        user_input = self.quiz_entry.get()

        #reset label and entry box in case of error
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.quiz_entry.config(bg="#FFFFFF")
        

        try:
            user_input = str(user_input)
            #if user_input >= min_temp:
            self.answer_question(user_input)

        except ValueError:
            pass
            #self.answer_error.config(text="Answer Invalid", fg="#9C0000", font=("Arial", "14", "bold"))

        self.generate_question()
        

        #convert


    def generate_question(self):
        print("gen")
        first_part = random.randint(1, 100)
        second_part = random.randint(1, 100)
        operator = random.randint(1, 4)
        if operator == 1:
            self.solution = first_part + second_part
            question_text = str(first_part) + "+" + str(second_part)
            problem = ("Please enter an answer to the presented question: " + question_text)
        elif operator == 2:
            self.solution = first_part - second_part
            question_text = str(first_part) + "-" + str(second_part)
            problem = ("Please enter an answer to the presented question: " + question_text)
        elif operator == 3:
            self.solution = first_part / second_part
            question_text = str(first_part) + "/" + str(second_part)
            problem = ("Please enter an answer to the presented question: " + question_text)
        elif operator == 4:
            self.solution = first_part * second_part
            question_text = str(first_part) + "x" + str(second_part)
            problem = ("Please enter an answer to the presented question: " + question_text)
        self.quiz_instructions.config(text=problem)


    def answer_question(self, user_input, solution):
        print(user_input)
        #if user_input == 
    
    #def history(self, list):
        #history_statement = str(list).strip("[]").replace("'", "")
        #self.answer_error.config(text=history_statement, wraplength=250)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    Quiz()
    root.mainloop()