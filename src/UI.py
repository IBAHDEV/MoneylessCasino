import customtkinter as ctk
import backend

# root window
app = ctk.CTk()
app.title("MoneyLessCasino")
app.geometry("600x400")

#menu frame container
menu_frame = ctk.CTkFrame(master=app)
menu_frame.pack(pady=20, padx=60, fill="both", expand=True)

def appMain():
    # -------MAIN MENU-------
    # appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    

    #title label 
    title_label = ctk.CTkLabel(master=menu_frame, text="MoneyLessCasino", font=("Roboto", 24))
    title_label.pack(pady=30)

    # title label
    title_label = ctk.CTkLabel(master=menu_frame, text="MoneyLessCasino", font=("Roboto", 24))
    title_label.pack(pady=10)

    # buttons (Enter, Quit and Settings)
    enter_button = ctk.CTkButton(master=menu_frame, text="Enter", command=print("Entering Minigames........."))
    enter_button.pack(pady=10)

    settings_button = ctk.CTkButton(master=menu_frame, text="Settings", command=None)
    settings_button.pack(pady=10)

    exit_button = ctk.CTkButton(master=menu_frame, text="Exit", command=app.destroy)
    exit_button.pack(pady=10)

#-------MINIGAMES SECTION-------
#switching from main main menu to minigame selection page
def show_minigames():
    menu_frame.pack_forget() #removes main menu out of the display

    #new frame for minigame section
    minigame_selection_frame = ctk.CTkFrame(master=app)
    minigame_selection_frame.pack(pady=20, padx=60, fill="both", expand=True)

    minigame_label = ctk.CTkLabel(master=minigame_selection_frame, text="Return to Main Menu", command=lambda: return_to_menu(minigame_selection_frame))
    minigame_label.pack(pady=10)

#-------RETURN TO MAIN MENU FUNCTION-------
def return_to_menu(current_frame):
    current_frame.pack_forget() #hide the game screen
    menu_frame.pack(pady=20, padx=60, fill="both", expand=True) #show main menu again

#updated enter button
enter_button = ctk.CTkButton(master=menu_frame, text="Enter", command=show_minigames)

#make the app run in seprate window
app.mainloop()
