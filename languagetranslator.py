from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("1000x500")
root.config(bg="#F2CCC3")

languages = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=languages, state="readonly", width=20)
src_lang.place(relx=0.2, rely=0.25, anchor="w")
src_lang.set("english")


title_label = Label(root, text="LANGUAGE TRANSLATOR", bg="#F2CCC3", font=("Constantia", 20, "bold"))
title_label.place(relx=0.5, rely=0.1, anchor="center")

enter_text_label = Label(root, text="Enter Text :", bg="#F2CCC3", font=("Constantia", 15))
enter_text_label.place(relx=0.05, rely=0.25, anchor="w")

textarea = Text(root, bg="white", font=("Arial", 12, "normal"), height=10, wrap=WORD, width=40, padx=5, pady=5, bd=0)
textarea.place(relx=0.05, rely=0.5, anchor="w")

output_label = Label(root, text="Output : ", bg="#F2CCC3", font=("Constantia", 15))
output_label.place(relx=0.7, rely=0.25, anchor="w")

output_lang_combobox = ttk.Combobox(root, values=languages, state="readonly", width=20)
output_lang_combobox.place(relx=0.8, rely=0.25, anchor="w")
output_lang_combobox.set("Choose output language")

converted_textarea = Text(root, bg="white", font=("Arial", 12, "normal"), height=10, wrap=WORD, width=40, padx=5, pady=5, bd=0)
converted_textarea.place(relx=0.58, rely=0.5, anchor="w")

translate_button = Button(root, text="Translate", font=("Constantia", 12, "normal"), bg="#C2C4E2", activebackground="#A2A4C2", fg="black", relief=FLAT, pady=5)
translate_button.place(relx=0.5, rely=0.8, anchor="center")


root.mainloop()