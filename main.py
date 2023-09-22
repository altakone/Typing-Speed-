import random
import tkinter as tk
from words import WORDS


def num_conve(n):
    if n == 0:
        return "0 "
    if n > 9:
        return n
    return f"{n} "


background_color = "#EDEDED" #"#FFF5E0"
COUNT_TIME = 60
count_f = None
proceed_f = None
press_f = None 
start_id = False
wrong = 0
correct = 0


wn = tk.Tk()
wn.title("Typing Speed Test")
wn.config(pady=10, bg=background_color, height=520, padx=30)



def time_finish():
    """Function calls reset and displays score once the time reaches 0.""" 
    global start_id, correct, wrong
    start_id = False
    sc = (correct - wrong)
    cor = correct
    wr = wrong
    reset()
    score.config(text=f"Score:{num_conve(sc)}\nCorrect:{num_conve(cor)}\nWrong:{num_conve(wr)}")


def LOG(event=None):
    ### MAIN ###
    global count_f, proceed_f, press_f, correct, wrong
    press_f = pressed()


def pressed(event=None):
    """Starts the game And changes score."""      
    global timer, sc, count_f, proceed_f, press_f, start_id, correct, wrong
    text = entry.get("1.0", "end-1c").strip()
    if start_id == False and correct == 0 and wrong == 0:
        score.config(text=f"Correct:{num_conve(correct)}\nWrong:{num_conve(wrong)}")
        proceed(start_id)
        start_id = True
        count_down(COUNT_TIME)
        entry.delete("1.0", "end") 
    else:
        if check_word(text):
            entry.delete("1.0", "end")
        else:
            entry.delete("1.0", "end")
        score.config(text=f"Correct:{num_conve(correct)}\nWrong:{num_conve(wrong)}")
        proceed(start_id)
                

def proceed(start):
    ### Replaces next_q with question and fetches new word for next_q ###
    global sc, score, count_f, press_f, proceed_f, start_id, correct, wrong
    if not start:
        question_canvas.itemconfigure(question, text=random.choice(WORDS))
        question_canvas.itemconfigure(next_q, text=random.choice(WORDS))
    else:
        question_canvas.itemconfigure(question, text=question_canvas.itemcget(next_q, "text"))
        question_canvas.itemconfigure(next_q, text=random.choice(WORDS))


def count_down(second):
    """Basic mechanics of count_down and it also changes entry color.""" 
    global timer, count_f, press_f, proceed_f
    #color changes for entry part
    text = entry.get("1.0", "end-1c").strip() 
    current_len = len(text.lower())
    if text.lower()[:current_len] == question_canvas.itemcget(question, "text").lower()[:current_len]:
        if text.lower() == question_canvas.itemcget(question, "text").lower():
            entry.config(fg="#004225")
        else:
            entry.config(fg="#071952")
            
    else:
        entry.config(fg="red")
    #count_down
    if second > 0:
        timer.configure(text=f"Time:{num_conve(int(second))}")
        count_f = wn.after(200, count_down, second - 0.2)
        
    else:
         timer.config(text=f"Time:{num_conve(int(second))}")
         time_finish()


def check_word(word):
    """Checks correctness of the answer and returns a boolean value of it.""" 
    global sc, score, count_f, press_f, proceed_f, correct, wrong
    result = word.lower() == question_canvas.itemcget(question, "text").lower()
    if result:
        correct += 1
    else:
        wrong += 1
    return result  
    

def reset():
    """Function resets everything back to its starting stage."""
    global count_f, press_f, proceed_f, sc, start_id, correct, wrong
    start_id = False
    entry.config(fg="black")
    sc = 0
    wn.after_cancel(count_f)
    timer.config(text=f"Time:{COUNT_TIME}")
    correct = 0
    wrong = 0
    score.config(text=f"Correct:{num_conve(correct)}\nWrong:{num_conve(wrong)}")
    question_canvas.itemconfig(question, text="")
    question_canvas.itemconfig(next_q, text=f"")


TITLE_LABEL = tk.Label(text=f"Typing Speed Test", highlightbackground=background_color, 
                 background=background_color, fg="black", font=("Courier",30, "bold"),
                 padx=10)
TITLE_LABEL.grid(row=0, column=1)

clock_img = tk.PhotoImage(file="clock.png")
clock_canvas = tk.Canvas(width=350, height=350, bg=background_color, highlightbackground=background_color)
image = clock_canvas.create_image(175, 175, image=clock_img)
clock_canvas.grid(row=1, column=1)



timer = tk.Label(text=f"Time:{COUNT_TIME}", highlightbackground=background_color, 
                 background=background_color, fg="black", font=("Courier", 24, "bold"),
                 padx=10)
timer.grid(row=1, column=2)

score = tk.Label(text=f"Correct:{num_conve(correct)}\nWrong:{num_conve(wrong)}", highlightbackground=background_color, 
                 background=background_color, fg="black", font=("Courier", 24, "bold"),
                 padx=10)
score.grid(row=1, column=0)

question_canvas = tk.Canvas(width=400, height=30, bg=background_color, highlightbackground=background_color)
question = question_canvas.create_text(120, 15, text=f"", fill="black", font=("Courier", 24, "bold"))
next_q = question_canvas.create_text(280, 15, text=f"", fill="black", font=("Courier", 20, "bold"))
question_canvas.grid(row=2, column=1)

entry = tk.Text(width=24, height=1, font=("Sans Serif", 24, "bold"), borderwidth=2, )
entry.grid(row=3, column=1)
entry.bind("<Return>", LOG)

reset_button = tk.Button(text="Reset", height=1, width=8, font=("Sans Serif", 16, "bold"), bg=background_color, command=reset)
reset_button.grid(row=3, column=2)

start_label = tk.Label(text=f"Press Enter", highlightbackground=background_color, 
                 background=background_color, fg="black", font=("Courier", 18, "bold"),
                 padx=10)
start_label.grid(row=3, column=0)

wn.mainloop()
