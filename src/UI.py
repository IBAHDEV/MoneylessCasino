import customtkinter as ctk
from PIL import Image #add images
import backend

# root window
app = ctk.CTk()
app.title("MoneyLessCasino")
app.geometry("1000x700")

menu_frame = ctk.CTkFrame(master=app)
menu_frame.pack(pady=20, padx=60, fill="both", expand=True)

def appMain():
    #-------Blackjack Main Game SECTION-------
    def Blackjack_Main(current_frame):
        current_frame.pack_forget() #removes minigame selection page

        #main game table
        Blackjack_game_frame = ctk.CTkFrame(master=app)
        Blackjack_game_frame.pack(pady=20, padx=60, fill="both", expand=True)

        #getting initial hands 
        deck = backend.CreateCards()
        hands = backend.ReturnHands(deck)

        #----Dealer Section----
        dealer_label = ctk.CTkLabel(master=Blackjack_game_frame, text="Dealer", font=("Roboto", 20))
        dealer_label.pack(pady=(10, 0))

        dealer_card_frame = ctk.CTkFrame(master=Blackjack_game_frame, fg_color="transparent")
        dealer_card_frame.pack(pady=10)

        #Showing the Dealer cards 
        for i in range(len(hands["Dealer"]["Card"])):
            rank = hands["Dealer"]["Card"][i]
            suit = hands["Dealer"]["Suit"][i]

            #translator for rank 1 of cards
            if rank == 1:
                rank = "A"

            #determining file name for cards
            path = f"images/Cards/{rank}_of_{suit}.png"

            img_data = Image.open(path)
            img_obj = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(100, 150))

            card_display = ctk.CTkLabel(master=dealer_card_frame, text="", image=img_obj)
            card_display.pack(side="left", padx=5)

        #----PLAYER Section----
        player_label = ctk.CTkLabel(master=Blackjack_game_frame, text="Your Hand", font=("Roboto", 20))
        player_label.pack(pady=(20, 0))

        player_card_frame = ctk.CTkFrame(master=Blackjack_game_frame, fg_color="transparent")
        player_card_frame.pack(pady=10)

        #displaying the players cards
        for i in range(len(hands["Player"]["Card"])):
            rank = hands["Player"]["Card"][i]
            suit = hands["Player"]["Suit"][i]

            #translator for rank 1 of cards
            if rank == 1:
                rank = "A"

            path = f"images/cards/{rank}_of_{suit}.png"

            img_data = Image.open(path)
            img_obj = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(100, 150))

            card_display = ctk.CTkLabel(master=player_card_frame, text="", image=img_obj)
            card_display.pack(side="left", padx=5)

        #----CONTROLS----
        btn_frame = ctk.CTkFrame(master=Blackjack_game_frame, fg_color="transparent")
        btn_frame.pack(pady=30)
        
        ctk.CTkButton(master=btn_frame, text="HIT", width=100, fg_color="darkred").pack(side="left", padx=10)
        ctk.CTkButton(master=btn_frame, text="STAND", width=100, fg_color="darkblue").pack(side="left", padx=10)


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

        #blackjack image loading
        blackjack_image_raw = Image.open("images/Minigame Selection Tile Images/Blackjack.jpg")
        blackjack_image_ctk = ctk.CTkImage(light_image=blackjack_image_raw, dark_image=blackjack_image_raw, size=(210,210))
        
        #blackjack image in tile
        blackjack_image_place = ctk.CTkButton(master=blackjack_tile, text="", image=blackjack_image_ctk, command=lambda: Blackjack_Main(minigame_selection_frame), width=200, height=200, fg_color="green")
        blackjack_image_place.pack(pady=(10,0), padx=10)

        #blackjack label underneath image
        blackjack_label = ctk.CTkLabel(master=blackjack_tile, text="BlackJack", font=("Roboto",22))
        blackjack_label.pack(pady=15)

        #-------MIDDLE TILE SECTION-------
        #UNKNOWN tile creation
        Unknown1_tile = ctk.CTkFrame(master=minigame_selection_frame, width=350, height=450)
        Unknown1_tile.grid(row=1, column=1, padx=40, pady=20)

        #UNKNOWN image in tile
        Unknown1_image_place = ctk.CTkButton(master=Unknown1_tile, width=200, height=200, fg_color="green")
        Unknown1_image_place.pack(pady=(10,0), padx=10)

        #UNKNOWN label underneath image
        Unknown1_label = ctk.CTkLabel(master=Unknown1_tile, text="Coming Soon", font=("Roboto",22))
        Unknown1_label.pack(pady=15)

        #-------RIGHT TILE SECTION-------
        #UNKNOWN tile creation
        Unknown2_tile = ctk.CTkFrame(master=minigame_selection_frame, width=350, height=450)
        Unknown2_tile.grid(row=1, column=2, padx=40, pady=20)

        #UNKNOWN image in tile
        Unknown2_image_place = ctk.CTkButton(master=Unknown2_tile, width=200, height=200, fg_color="green")
        Unknown2_image_place.pack(pady=(10,0), padx=10)

        #UNKNOWN label underneath image
        Unknown2_label = ctk.CTkLabel(master=Unknown2_tile, text="Coming Soon", font=("Roboto",22))
        Unknown2_label.pack(pady=15)

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