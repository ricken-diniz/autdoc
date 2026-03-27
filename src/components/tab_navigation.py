"""
Componente de navegação por abas
"""

import customtkinter as ctk


class TabNavigation(ctk.CTkFrame):

    def __init__(self, parent, tabs, on_tab_change):
        super().__init__(parent, fg_color="transparent")
        
        self.tabs = tabs
        self.on_tab_change = on_tab_change
        self.buttons = {}
        self.active_tab = None
        
        self.create_tabs()
    



    def create_tabs(self):
        """Cria os botões de navegação"""

        for i, tab_name in enumerate(self.tabs):
            btn = ctk.CTkButton(
                self,
                text=tab_name,
                width=140,
                height=40,
                corner_radius=10,
                fg_color="#9ca3af",
                hover_color="#6b7280",
                text_color="white",
                font=("Segoe UI", 14, "bold"),
                command=lambda t=tab_name: self.on_tab_click(t)
            )
            btn.grid(row=0, column=i, padx=5)
            self.buttons[tab_name] = btn
    



    def on_tab_click(self, tab_name):
        """Handler de clique em uma aba"""
        self.set_active(tab_name)
        self.on_tab_change(tab_name)
    



    def set_active(self, tab_name):
        """Define a aba ativa"""
        
        for name, btn in self.buttons.items():
            if name == tab_name:
                btn.configure(fg_color="#6b7280", text_color="white")
            else:
                btn.configure(fg_color="#9ca3af", text_color="#e5e7eb")
        
        self.active_tab = tab_name
