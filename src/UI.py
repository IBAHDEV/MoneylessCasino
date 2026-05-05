import customtkinter as ctk
import backend

# root window
app = ctk.CTk()
app.title("MoneyLessCasino")
app.geometry("1000x700")

menu_frame = ctk.CTkFrame(master=app)
menu_frame.pack(pady=20, padx=60, fill="both", expand=True)

def appMain():
    #-------MINIGAMES SECTION-------
    #switching from main main menu to minigame selection page
    def show_minigames():
        menu_frame.pack_forget() #removes main menu out of the display

        #new frame for minigame section
        minigame_selection_frame = ctk.CTkFrame(master=app)
        minigame_selection_frame.pack(pady=20, padx=60, fill="both", expand=True)
        minigame_selection_frame.grid_columnconfigure(0, weight=1)
        minigame_selection_frame.grid_columnconfigure(1, weight=1)
        minigame_selection_frame.grid_columnconfigure(2, weight=1)
        minigame_selection_frame.grid_rowconfigure(1, weight=1)

        #the header - spanning 2 columns to stay centered
        selection_title = ctk.CTkLabel(master=minigame_selection_frame, text="Select your Minigame", font=("Roboto", 28, "bold"))
        selection_title.grid(row=0, column=1, pady=40)
        
        #-------BLACKJACK TILE SECTION-------
        #blackjack tile creation
        blackjack_tile = ctk.CTkFrame(master=minigame_selection_frame, width=350, height=450)
        blackjack_tile.grid(row=1, column=0, padx=40, pady=20)

        #blackjack image in tile
        blackjack_image_place = ctk.CTkButton(master=blackjack_tile, text="Blackjack Image", width=200, height=200, fg_color="green")
        blackjack_image_place.pack(pady=(10,0), padx=10)

        #blackjack label underneath image
        blackjack_label = ctk.CTkLabel(master=blackjack_tile, text="BlackJack", font=("Roboto",22))
        blackjack_label.pack(pady=15)

        #-------MIDDLE TILE SECTION-------
        #blackjack tile creation
        blackjack_tile = ctk.CTkFrame(master=minigame_selection_frame, width=350, height=450)
        blackjack_tile.grid(row=1, column=1, padx=40, pady=20)

        #blackjack image in tile
        blackjack_image_place = ctk.CTkButton(master=blackjack_tile, width=200, height=200, fg_color="green")
        blackjack_image_place.pack(pady=(10,0), padx=10)

        #blackjack label underneath image
        blackjack_label = ctk.CTkLabel(master=blackjack_tile, text="Coming Soon", font=("Roboto",22))
        blackjack_label.pack(pady=15)

        #-------RIGHT TILE SECTION-------
        #blackjack tile creation
        blackjack_tile = ctk.CTkFrame(master=minigame_selection_frame, width=350, height=450)
        blackjack_tile.grid(row=1, column=2, padx=40, pady=20)

        #blackjack image in tile
        blackjack_image_place = ctk.CTkButton(master=blackjack_tile, width=200, height=200, fg_color="green")
        blackjack_image_place.pack(pady=(10,0), padx=10)

        #blackjack label underneath image
        blackjack_label = ctk.CTkLabel(master=blackjack_tile, text="Coming Soon", font=("Roboto",22))
        blackjack_label.pack(pady=15)

        #-------BACK BUTTON SECTION-------
        #back button to return to main menu
        back_button = ctk.CTkButton(master=minigame_selection_frame, text="Return to main menu", command=lambda: return_to_menu(minigame_selection_frame))
        back_button.grid(row=2, column=1, pady=40)

        

    #-------RETURN TO MAIN MENU FUNCTION-------
    def return_to_menu(current_frame):
        current_frame.pack_forget() #hide the game screen
        menu_frame.pack(pady=20, padx=60, fill="both", expand=True) #show main menu again

    # -------MAIN MENU-------
    # appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    #title label 
    title_label = ctk.CTkLabel(master=menu_frame, text="MoneyLessCasino", font=("Roboto", 24))
    title_label.pack(pady=30)

    # buttons (Enter, Quit and Settings)
    enter_button = ctk.CTkButton(master=menu_frame, text="Enter", command=(show_minigames))
    enter_button.pack(pady=10)

    settings_button = ctk.CTkButton(master=menu_frame, text="Settings", command=None)
    settings_button.pack(pady=10)

    exit_button = ctk.CTkButton(master=menu_frame, text="Exit", command=app.destroy)
    exit_button.pack(pady=10)

    #make the app run in seprate window
    app.mainloop()

