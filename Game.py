import tkinter as tk

window = tk.Tk()
window.title("Game Board")

button1 = tk.Button(window, text="1", width=10, height=5)
button1.grid(row=0, column=0)
button2 = tk.Button(window, text="2", width=10, height=5)
button2.grid(row=0, column=1)
button3 = tk.Button(window, text="3", width=10, height=5)
button3.grid(row=1, column=0)
button4 = tk.Button(window, text="4", width=10, height=5)
button4.grid(row=1, column=1)

init_config = [1, 1, 1, 1]

l_1 = [1,1,1,0]
l_2 = [1,1,0,1]
l_3 = [1,0,1,1]
l_4 = [0,1,1,1]

def add_button_press(v_1, v_2):
    result = []
    for i in range(len(v_1)):
        result.append( (v_1[i] + v_2[i]) % 2)
    init_config = result
    change_button_colors(init_config)

def take_user_input():
    init_config = [1, 1, 1, 1]
    while (sum(init_config) != 0):
        user_input = input("Enter button number:")
        if user_input == '1':
            init_config = add_button_press(l_1, init_config)
        elif user_input == '2':
            init_config = add_button_press(l_2, init_config)
        elif user_input == '3':
            init_config = add_button_press(l_3, init_config)
        elif user_input == '4':
            init_config = add_button_press(l_4, init_config)
        print(init_config)

def change_button_colors(configuration):
    for i in range(len(configuration)):
        if (configuration[i] == 0):
            if (i  == 0):
                button1.config(bg='dark grey')
            if (i  == 1):
                button2.config(bg='dark grey')
            if (i == 2):
                button3.config(bg='dark grey')
            if (i == 3):
                button4.config(bg='dark grey')
        else:
            if (i == 0):
                button1.config(bg='white')
            if (i == 1):
                button2.config(bg='white')
            if (i == 2):
                button3.config(bg='white')
            if (i == 3):
                button4.config(bg='white')


def main():
    init_config = [1, 1, 1, 1]
    # Create the main window
    change_button_colors(init_config)

    button1.config(command= add_button_press(l_1, init_config))
    button2.config(command=add_button_press(l_2, init_config))
    button3.config(command=add_button_press(l_3, init_config))
    button4.config(command=add_button_press(l_4, init_config))

    # Start the main event loop
    window.mainloop()






# Using the special variable
# __name__
if __name__=="__main__":
    main()