import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {
        "question": "Analytical Engine, the first fully automatic calculating machine was developed by?",
        "options": ["Charles Babbage", "Blaise Pascal", "Leibniz", "John Von Neumann"],
        "correct_answer": "Charles Babbage",
    },
    {
        "question": "A computer system includes?",
        "options": ["Hardware", "software", "Peripheral devices", "All of these"],
        "correct_answer": "All of these",
    },
    {
        "question": "Which was the first mechanical calculating device?",
        "options": ["UNIVAC", "Abacus", "PASCALINE", "Leibniz Calculator"],
        "correct_answer": "Abacus",
    },
    {
        "question": "Who invented Zero?",
        "options": ["Oppenheimer", "Mithlesh", "Aryabhatta", "Adison"],
        "correct_answer": "Aryabhatta",
    }
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Game By Mithlesh")
        self.geometry("800x600")
        self.configure(bg="white")

        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.quiz_frame = tk.Frame(self.main_frame, bg="lightblue")
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.score = 0
        self.current_question = 0

        self.label_question = tk.Label(self.quiz_frame, text="", wraplength=600, font=('Arial', 16, 'bold'), bg="lightblue")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(-1) 

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(self.quiz_frame, text="", variable=self.radio_var, value=i, font=('Arial', 12), bg="lightblue")
            self.radio_buttons.append(radio)
            radio.pack(pady=5)
            radio.bind("<Enter>", lambda event, idx=i: self.highlight_option(idx))
            radio.bind("<Leave>", self.clear_highlight)

        self.button_next = tk.Button(self.quiz_frame, text="Next", command=self.next_question,
                                     font=('Arial', 14, 'bold'), bg="lightblue")
        self.button_next.pack(pady=20)
        self.load_question(0)

    def load_question(self, question_index):
        if question_index < len(quiz_data):
            self.label_question.config(text=quiz_data[question_index]["question"])
            for i in range(4):
                self.radio_buttons[i].config(text=quiz_data[question_index]["options"][i], font=('Arial', 12), bg="lightblue")
        else:
            self.show_result()

    def next_question(self):
        selected_option = int(self.radio_var.get())

        if selected_option == -1:
            messagebox.showwarning("Warning", "Please select an option.", font=('Arial', 10, 'bold'))
        else:
            correct_answer = quiz_data[self.current_question]["correct_answer"]
            if quiz_data[self.current_question]["options"][selected_option] == correct_answer:
                self.score += 1

            self.current_question += 1
            self.radio_var.set(-1)  

            if self.current_question < len(quiz_data):
                self.load_question(self.current_question)
            else:
                self.show_result()

    def show_result(self):
        messagebox.showinfo("Result", f"You scored {self.score}/{len(quiz_data)}")
        self.quit()

    def highlight_option(self, idx):
        self.radio_buttons[idx].config(highlightbackground="blue")

    def clear_highlight(self, event):
        for button in self.radio_buttons:
            button.config(highlightbackground="lightblue")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
