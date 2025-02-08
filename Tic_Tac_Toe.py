import tkinter as tk
from tkinter import messagebox
#Tkinter is the standard GUI (Graphical User Interface) library for Python, allowing developers to create windows, buttons, and other interactive components. It provides a simple way to build desktop applications with a graphical interface.

window = tk.Tk() #creates a main window for the game
 
window.title("Tic Tac Toe")
window.geometry("600x600")
window.update()
window.configure(bg = "lightblue")

#initialize the board and current player
board = [["" for _ in range (3)] for i in range(3)] #3x3 board initialized with empty strings

current_player = "X" #player X will start the game

# LETS CREATE A FUNCTION TO CHECK IF WE HAVE A WINNER AND THE GAME IS OVER.
def check_winner():

    for i in range(3):  
        if board[i][0]==board[i][1]==board[i][2] !="" :
           return board[i][0]   #row check
        if board[0][i]==board[1][i]==board[2][i] !="" :
           return board[0][i]  #column check
    
    if board[0][0]==board[1][1]==board[2][2] !="" :
        return board[0][0]  #diagonal check
    if board[0][2]==board[1][1]==board[2][0] !="" :
        return board[0][2]  #diagonal check
        
    return None

# we will write a function to handle the button clicks
def click_button(row,col):

    global current_player

    #checking if he button is already clicked
    if board[row][col] != "":
        return

    #Update the board with current players symbol 
    board[row][col] = current_player

    #Set button colour dynamically based on the current player
    if current_player == "X":
           buttons[row][col].config(text = current_player, bg= "red", fg = "black",state = "disabled" , font = ("Arial" , 36 , 'bold'), relief = "solid" , bd = 4,highlightthickness = 2) #once the button is clicked it will be disabled
    else:
           buttons[row][col].config(text = current_player, bg= "yellow",fg = "black",state = "disabled" , font = ("Arial" , 36 , 'bold'), relief = "solid" , bd = 4,highlightthickness = 2) #once the button is clicked it will be disabled.

    #Let's check if we have a winner after every move as click_button function is called after every move.
    winner = check_winner()

    if winner : 
        
        print(f"Player {winner} wins!")
        messagebox.showinfo("Game Over !", f"Player {winner} wins!")
        
        #once we found a winner , we will disable all the buttons to prevent further moves and game is over.

        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state = "disabled")
    
    else :
        #if there is no winner yet, we will check if the board is full and declare a draw.
        if all(board[i][j] != "" for i in range(3) for j in range(3)):

            messagebox.showinfo("Game over!", "It's a draw!")
        
        else:
        #if we dont have a winner yet, we will change the player.
            current_player = "O" if current_player == "X" else "X" 

#Let's create a restart function to restart the game.

def restart_game() :
    #Set player X to start the game
    global  current_player
    current_player = "X"
    
    # Set all buttons to normal state and clear the board
    for i in range (3):
        for j in range (3):
            buttons[i][j].config(text = "", state = "normal", relief = "solid", bg = "lightgray", bd = 2)
     
#Now we will create the Tic Tac Toe grid. (3x3)
buttons = [[None, None, None] for _ in range(3)] 

'''for _ in range(3) means "do this three times," so the list comprehension will loop 3 times.
Each time it loops, it creates a new list: [None, None, None]. This is a list with three None values.It crates a 3x3 grid that has all values set to none initially'''

for i in range(3):
    for j in range (3):
        buttons[i][j] = tk.Button(window, text = "", width=8 , height= 3, font=("Arial" , 36, 'bold'), bg= "lightgray",activebackground="lightyellow", relief="solid", command = lambda i=i,j=j: click_button(i,j) )
        buttons[i][j].grid(row = i , column =j, sticky = "nsew") 
        # In Tkinter, grid() is used to place widgets (like buttons, labels, etc.) in a grid layout.
        # The sticky option is used to specify how the widget would expand or contract to fill the space available to it.

        #now lets make rows and column stretchable , so that they can fill the entire window.
for i in range (3) : 
    window.grid_columnconfigure(i,weight=1)
    window.grid_rowconfigure(i,weight=1)

#Let's create a restart button to restart the game.
restart_button = tk.Button(window , text = "Restart Game" , width = 20 , height=2, command = restart_game,font = ("Arial" , 14 , 'bold'), bg = "lightgreen", activebackground = "lightyellow", relief = "solid")
restart_button.grid(row = 3 , column=0, columnspan= 3, pady=20)

window.mainloop() 
#runs the main loop of the game
