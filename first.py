import tkinter as tk

import tkinter as tk
import json

def load_questions_from_file(filename='questions.json'):
    """Load questions from a JSON file."""
    try:
        # ใช้ 'r' สำหรับอ่าน, encoding='utf-8' เพื่อรองรับภาษาไทยถ้ามี
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        # Return a fallback question list if file is missing
        return [{'question': 'Failed to load questions.'}]
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filename}. Check file syntax.")
        return [{'question': 'JSON format error.'}]


questions = load_questions_from_file()

window = tk.Tk()
window.title('Mini Quiz')
window.minsize(width=300, height=300)

    

window_label = tk.Label(master=window, text='Mini Quiz')
window_label.pack()

window_question = tk.Label(master=window, text='')
window_question.pack(pady=20)

current_index = 0
select_choice = tk.StringVar()
score = 0

def load_question():
    global current_index
    global score
    if current_index < len(questions):
        q = questions[current_index]
        window_question.config(text=q['question'])
        select_choice.set(None)
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()
        for choice in q['choice']:
            tk.Radiobutton(window, text=choice, 
                           variable=select_choice, 
                           value=choice).pack(anchor='w')
    else:
        score = str(score)
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
               widget.destroy()
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
               widget.destroy()
               window_question.config(text='')
               result_label.config(text='Congraturation')
               score_label.config(text='score = ' + score +'/20')

def check_answer():
    global current_index
    global score
    if select_choice.get() == questions[current_index]['answer']:
        result_label.config(text='correct')
        current_index += 1
        score += 1
        load_question()
    else:
        result_label.config(text='not correct')
        current_index += 1
        load_question()

check_button = tk.Button(window, text='check answer', 
                         command=check_answer)
check_button.pack(pady=10)

result_label = tk.Label(master=window, text='')
result_label.pack(pady=10)

score_label = tk.Label(master=window, text='')
score_label.pack(pady=11)

score2_label = tk.Label(master=window, text='')
score2_label.pack()
        

load_question()


window.mainloop()