from tkinter import *
import random
import generate_question as gen
import os


class Quiz():


    def __init__(self):
        
        #globals
        global score
        score = 0


        #previous questions list
        self.question_history = []
        """
        quiz gui
        """
        #window
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        #heading
        self.quiz_heading = Label(self.quiz_frame, text="Math Quiz", font=("Arial", "20", "bold"))
        self.quiz_heading.grid(row=0)

        #instructions
        instructions = "Click the Start button to begin"
        self.quiz_instructions = Label(self.quiz_frame, text=instructions, wraplength=250, width=40, height=3, justify="center", font=("Arial", "14", "bold"))
        self.quiz_instructions.grid(row=1)

        #entry field
        self.quiz_entry = Entry(self.quiz_frame, font=("Arial", "14"))
        self.quiz_entry.grid(row=2, padx=10, pady=10)

        #score
        score_text = "Score: 0" #+ score
        self.score_gui_text = Label(self.quiz_frame, text=score_text, fg="#000000", font=("Arial", "14", "bold"))
        self.score_gui_text.grid(row=3)

        #conversion, help, and history
        self.button_frame = Frame(self.quiz_frame)
        self.button_frame.grid(row=4)

        #button list (text/bg color/command/row/column)
        button_details_list = [
            ["Submit Answer", "#990099", lambda:self.check_input(), 0, 1],
            ["History", "#009900", lambda:self.history(self.question_history), 1, 0],
            ["Quit", "#CC6600", lambda:self.quit(), 1, 1],
            ["Start", "#004C99", lambda:self.next_question(), 1, 2]
        ]

        #hold the buttons
        self.button_ref_list = []

        #create buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], fg="#FFFFFF", font=("Arial", "12", "bold"),
                                       width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        self.gui_instructions = self.quiz_instructions
        self.next_button = self.button_ref_list[3]

    
        
    def check_input(self):

        #get input
        user_input = self.quiz_entry.get()

        #reset label and entry box 
        
        self.quiz_entry.config(bg="#FFFFFF")
        

        try:
            user_input = float(user_input)

            self.answer_question(user_input)

        except ValueError:
            pass


        

        #create next question and display

    def next_question(self):
        global new_question
        new_question = gen.generate.generate_question()
        global new_answer
        new_answer = new_question[1]
        self.gui_instructions.config(text = new_question[0])
        self.next_button.config(text = "Next Question")
        self.has_answered = False

    
    #compare user input and answer then add to the history list

    def answer_question(self, user_input):
        print(new_answer)
        if user_input == float(new_answer):
            self.gui_instructions.config(text = "Correct!")
            global has_answered
            if self.has_answered == False:
                global score
                score += 1
                self.has_answered = True
                full_hist = str(new_question[2] + " = " + str(user_input) + "(Correct)")
            self.score_gui_text.config(fg="#000000", font=("Arial", "13", "bold"), text= "Score: " + str(score))

        else:
            self.gui_instructions.config(text = "Incorrect!")
            self.has_answered = True
            full_hist = str(new_question[2] + " = " + str(user_input) + " (Incorrect)")
        self.question_history.append(full_hist + "nlr")
    
    #move the history list to a file and open it
    def history(self, list):
        history_statement = str(list).strip("[]").replace("'", "").replace(",", "").replace("nlr", "\n")
        history_file = open("history.txt", "w")
        history_file.write(history_statement)
        os.startfile("history.txt")


    def quit(self):
        quit()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.maxsize(500, 300)
    root.minsize(500, 300)
    root.title("Math Quiz")
    Quiz()
    root.mainloop()