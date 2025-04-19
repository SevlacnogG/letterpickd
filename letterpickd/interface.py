import webbrowser

import customtkinter as ctk

from logic import control

class GUI:
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # WINDOW - size and title:
        self.root = ctk.CTk()
        self.root.geometry("480x480")
        self.root.title("Letterpickr")
        self.controller = control()


        #FIRST FRAME - size and settings:
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=15, padx=70, fill="both", expand=False)

        #Text and vertical spacing (pady) within the first frame:
        self.labelIntro = ctk.CTkLabel(master=self.frame, text="Seja bem-vindo.", font=("Roboto", 22))
        self.labelIntro.pack(pady=10)
        self.labelIntro2 = ctk.CTkLabel(master=self.frame, text="Informe as especificações desejadas:",
                                        font=("Roboto", 18), width=100)
        self.labelIntro2.pack(pady=10)


        #SECOND FRAME - set with a grid:
        self.frame2 = ctk.CTkFrame(master=self.root)
        self.frame2.columnconfigure(0, weight=1, pad=20)
        self.frame2.columnconfigure(1, weight=1, pad=20)
        self.frame2.columnconfigure(2, weight=1, pad=20)

        # User definition (need to use to_lowercase on the returned info):
        self.labelUser = ctk.CTkLabel(master=self.frame2, text="Usuário:", font=("Roboto", 16))
        self.labelUser.grid(row=0, column=0, pady=10)
        self.entryUser = ctk.CTkEntry(master=self.frame2, width=150)
        self.entryUser.grid(row=0, column=1)

        # Genre definition:
        self.labelGen = ctk.CTkLabel(master=self.frame2, text="Gênero:", font=("Roboto", 16))
        self.labelGen.grid(row=1, column=0, pady=10)
        self.dropGen = ctk.CTkComboBox(master=self.frame2, width=150, state="readonly",
                                    values=["Ação", "Aventura", "Animação", "Comédia", "Crime", "Documentário", "Drama",
                                            "Família", "Fantasia", "Ficção Científica", "Filme para TV", "Guerra",
                                            "História", "Horror", "Mistério", "Música", "Romance", "Suspense",
                                            "Velho Oeste"])
        self.dropGen.grid(row=1, column=1, pady=10)  # <-- Positioning on the grid.
        # self.drop.get() # <-- Returns the selected option.

        # Period selection:
        self.labelPer = ctk.CTkLabel(master=self.frame2, text="Década:", font=("Roboto", 16))
        self.labelPer.grid(row=2, column=0, pady=10)
        self.dropPer = ctk.CTkComboBox(master=self.frame2, width=150, state="readonly",
                                    values=["2020", "2010", "2000", "1990", "1980", "1970", "1960", "1950", "1940",
                                            "1930", "1920", "1910", "1900", "1890", "1880", "1870"])
        self.dropPer.grid(row=2, column=1, pady=10)

        # Button
        self.botao1 = ctk.CTkButton(master=self.frame2, text="Buscar", font=("Roboto", 20),
                                    command = self.c_acessList) # <-- Realiza ação ao clicar
        self.botao1.grid(row=5, column=1, pady=10)

        # Packs and makes the frame visible:
        self.frame2.pack()

        #Third frame - for selecting the user:
        # self.org = ctk.CTkFrame(self.root)
        # self.org.columnconfigure(0, weight=1, pad=20)
        # self.org.columnconfigure(1, weight=1, pad=20)
        # self.org.columnconfigure(2, weight=1, pad=20)
        #
        # self.labelMatricula = ctk.CTkLabel(master=self.org, text="Matrícula:", font=("Roboto", 16))
        # self.labelMatricula.grid(row=1, column=0)
        # self.entryMatricula = ctk.CTkTextbox(master=self.org, width=95, height=75, border_width=2, activate_scrollbars=0)
        # self.entryMatricula.grid(row=1, column=1, pady=10)
        #
        # self.botao2 = ctk.CTkButton(master=self.org, text="Verificar matrícula", font=("Roboto", 20))
        #                             , command=self.mostrar_resultado)
        # self.botao2.grid(row=1, column=2, pady=15)
        #
        # self.org.pack(pady=15)

        self.resultado = ctk.CTkTextbox(self.root, width=400, height=100, border_width=2)
        self.resultado.insert(0.0, "O resultado aparecerá aqui.\nCaso não escolha uma opção, serão "
                                   "considerados todos os\nfilmes possíveis.\nE sim, se não escolher nada, serão "
                                   "considerados todos os filmes já feitos na história da humanidade.",None)
        self.resultado.configure(state="disabled")
        self.resultado.pack(pady=15)

        self.root.mainloop()


    def c_acessList(self):
        user = self.entryUser.get()
        # decd = self.dropPer.get()
        # genr = self.dropGen.get()

        # resultado = self.controller.ciclo(user, decd, genr)

        resultado = self.controller.ciclo(user)
        self.displayReslt(resultado)


    def displayReslt(self, txt):
        self.resultado.configure(state="normal")
        self.resultado.delete(0.0, ctk.END)
        self.resultado.insert(0.0, f"O filme escolhido é: ")
        self.resultado.insert(ctk.END,  f"{txt[0]}", ("link", txt[1]))
        self.resultado.tag_config('link', foreground = "blue")
        self.resultado.tag_bind('link', '<Button-1>', lambda x: self.controller.abrir(txt[1]))
        self.resultado.configure(state="disabled")


if __name__ == '__main__': # For testing the GUI only.
    GUI()