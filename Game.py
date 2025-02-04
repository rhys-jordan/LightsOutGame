import tkinter as tk



l_1 = [1,1,1,0]
l_2 = [1,1,0,1]
l_3 = [1,0,1,1]
l_4 = [0,1,1,1]

def add_button_press(v_1, v_2):
    result = []
    for i in range(len(v_1)):
        result.append( (v_1[i] + v_2[i]) % 2)
    return (result)

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



def main():
    take_user_input()






# Using the special variable
# __name__
if __name__=="__main__":
    main()