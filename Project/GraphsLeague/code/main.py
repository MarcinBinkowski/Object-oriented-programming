import tkinter as tk

class GraphsLeagueApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")

        choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}

        tk.mainloop()


a = GraphsLeagueApp()