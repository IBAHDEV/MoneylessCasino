import customtkinter as ctk
import backend


def appMain():
    # -------MAIN MENU-------
    # appearance
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # root window
    app = ctk.CTk()
    app.title("MoneyLessCasino")
    app.geometry("600x400")

    # Menu frame
    menu_frame = ctk.CTkFrame(master=app)
    menu_frame.pack(pady=20, padx=60, fill="both", expand=True)

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

    # make the app run in seprate window
    app.mainloop()


