import tkinter as tk
import random
window = tk.Tk()
window.geometry("200x150")
window.title("Угадай число")
secret_number = random.randint(1, 100)
attempts = 10

def guess(event):
    global attempts
    #print("Работает")
    number = entry.get()
    if number == "":
        label["text"] = "Введи число от 1 до 100"
    else:
        if attempts > 0:
            attempts -= 1
            attempts_label["text"] = f"Количество попыток: {attempts}"
            number = int(number)
            if number == secret_number:
                label["text"] = "Поздравляю, ты угадал!"
                attempts = 0
                guess_button.configure(state = tk.DISABLED)
                reset_button.configure(state = tk.NORMAL)
            if number < secret_number:
                label["text"] = "Загаданное число больше!"
            if number > secret_number:
                label["text"] = "Загаданное число меньше!"
    entry.delete(0, "end")
                
def reset():
    global secret_number
    global attempts
    attempts = 10
    secret_number = random.randint(1, 100)
    attempts_label["text"] = f"Количество попыток: {attempts}"
    label["text"] = "Введи число от 1 до 100"
    entry.delete(0, "end")
    guess_button.configure(state = tk.NORMAL)
    reset_button.configure(state = tk.DISABLED)
    
    
    

label = tk.Label(window, text = "Угадай число от 1 до 100")
label.place(x = 30, y = 0)
attempts_label = tk.Label(window, text = f"Количество попыток: {attempts}")
attempts_label.place(x = 30, y = 30)
entry = tk.Entry(window)
entry.place(x = 40, y = 50)
entry.focus_set()
guess_button = tk.Button(window, text = "Проверить", width = 17, command = lambda e = "<Return>": guess(e))
guess_button.place(x = 35, y = 80)
reset_button = tk.Button(window, text = "Играть снова", width = 17, state = tk.DISABLED, command = reset)
reset_button.place(x = 35, y = 110)





window.bind("<Return>", guess)

window.mainloop()
