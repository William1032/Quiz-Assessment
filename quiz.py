from tkinter import *
import random
import generate_question as gen


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
        instructions = gen.generate.generate_question()
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
            ["History", "#009900", lambda:self.history(self.all_calculations_list), 1, 0],
            ["Stats", "#CC6600", lambda:gen.generate.generate_question(), 1, 1],
            ["Next", "#004C99", lambda:self.next_question(), 1, 2]
        ]

        #hold the buttons
        self.button_ref_list = []

        #create buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF", font=("Arial", "12", "bold"),
                                       width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

    
        
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

        

        #convert

    def next_question(self):
        new_question = gen.generate.generate_question()
        self.quiz_instructions.config(text = new_question)

    

    def answer_question(self, user_input, solution):
        print(user_input)
        if user_input == gen.generate.generate_answer():
            print("yes")
    
    def history(self, list):
        history_statement = str(list).strip("[]").replace("'", "")
        self.answer_error.config(text=history_statement, wraplength=250)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    Quiz()
    root.mainloop()