"""
View de Informações Adicionais
Terceira e última tela do formulário
"""

import customtkinter as ctk
from datetime import datetime


class GenericInfo(ctk.CTkFrame):

    def __init__(self, parent, on_finalize):
        super().__init__(parent, fg_color="transparent")
        
        self.on_finalize = on_finalize
        self.entries = {}
        
        self.create_widgets()
    



    def create_widgets(self):
        """Cria os widgets da view"""
        
        title_frame = ctk.CTkFrame(self, fg_color="#6b7280", corner_radius=15, height=80)
        title_frame.pack(fill="x", pady=(0, 20))
        title_frame.pack_propagate(False)

        title_label = ctk.CTkLabel(title_frame, text="Informações Adicionais", font=("Segoe UI", 24, "bold"), text_color="white")
        title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        form_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        form_frame.pack(fill="both", expand=True)

        scroll_frame = ctk.CTkScrollableFrame(form_frame, fg_color="transparent", scrollbar_button_color="#d1d5db", scrollbar_button_hover_color="#9ca3af")
        scroll_frame.pack(fill="both", expand=True, padx=50, pady=30)
        scroll_frame.grid_columnconfigure(0, weight=1)

        row_frame_1 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_1.grid(row=0, column=0, sticky="ew", pady=10)

        row_frame_2 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_2.grid(row=1, column=0, sticky="ew", pady=10)

        row_frame_3 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_3.grid(row=2, column=0, sticky="ew", pady=10)

        clausulas_label = ctk.CTkLabel(scroll_frame, text="Cláusulas", font=("Segoe UI", 16, "bold"), text_color="#1f2937", anchor="w")
        clausulas_label.grid(row=3, column=0, sticky="w", pady=(20, 10))
        
        self.entries["data_venda"] = self.create_inline_field(row_frame_1, "Data da Venda", 0)
        self.entries["hora_venda"] = self.create_inline_field(row_frame_1, "Hora da Venda", 1)
        self.entries["transferencia"] = self.create_inline_field(row_frame_1, "Transferência", 2)
        self.entries["nome_dono"] = self.create_inline_field(row_frame_2, "Nome do Dono", 0)
        self.entries["cpf_dono"] = self.create_inline_field(row_frame_2, "CPF do Dono", 1)
        self.entries["nome_vendedor"] = self.create_inline_field(row_frame_3, "Nome do Vendedor", 0)
        self.entries["cpf_vendedor"] = self.create_inline_field(row_frame_3, "CPF do Vendedor", 1)
        self.entries["clausula_5"] = self.create_textarea(scroll_frame, "Cláusula 5", row=4)
        self.entries["clausula_6"] = self.create_textarea(scroll_frame, "Cláusula 6", row=5)
        self.entries["clausula_7"] = self.create_textarea(scroll_frame, "Cláusula 7", row=6)
        self.entries["data_venda"].delete(0, "end")
        self.entries["data_venda"].insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entries["hora_venda"].delete(0, "end")
        self.entries["hora_venda"].insert(0, datetime.now().strftime("%H:%M"))
        
        finalize_btn = ctk.CTkButton(
            form_frame,
            text="Finalizar",
            width=200,
            height=40,
            corner_radius=8,
            fg_color="#d1d5db",
            hover_color="#9ca3af",
            text_color="#374151",
            font=("Segoe UI", 14, "bold"),
            command=self.on_finalize
        )
        finalize_btn.pack(side="right", padx=50, pady=(0, 30))
    



    def create_inline_field(self, parent, placeholder, column):
        """Cria um campo inline para layouts em linha"""
        parent.grid_columnconfigure(column, weight=1)
        
        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            height=45,
            corner_radius=8,
            border_width=1,
            border_color="#e5e7eb",
            fg_color="white",
            text_color="#374151",
            font=("Segoe UI", 13)
        )
        entry.grid(row=0, column=column, padx=5, sticky="ew")
        return entry
    



    def create_textarea(self, parent, placeholder, row):
        """Cria uma área de texto para cláusulas"""
        textbox = ctk.CTkTextbox(
            parent,
            height=100,
            corner_radius=8,
            border_width=1,
            border_color="#e5e7eb",
            fg_color="white",
            text_color="#374151",
            font=("Segoe UI", 13)
        )
        textbox.grid(row=row, column=0, sticky="ew", pady=10)
        
        textbox.insert("1.0", placeholder)
        textbox.configure(text_color="#9ca3af")
        
        def on_focus_in(event):
            if textbox.get("1.0", "end-1c") == placeholder:
                textbox.delete("1.0", "end")
                textbox.configure(text_color="#1f2937")
        
        def on_focus_out(event):
            if not textbox.get("1.0", "end-1c").strip():
                textbox.insert("1.0", placeholder)
                textbox.configure(text_color="#9ca3af")
        
        textbox.bind("<FocusIn>", on_focus_in)
        textbox.bind("<FocusOut>", on_focus_out)
        
        return textbox
    



    def get_data(self):
        """Retorna os dados do formulário"""

        def get_textarea_value(textbox, placeholder):
            """Obtém o valor de um textarea, ignorando placeholder"""
            value = textbox.get("1.0", "end-1c")
            return value if value != placeholder else ""
        
        return {
            "data_venda": self.entries["data_venda"].get(),
            "hora_venda": self.entries["hora_venda"].get(),
            "transferencia": self.entries["transferencia"].get(),
            "nome_dono": self.entries["nome_dono"].get(),
            "cpf_dono": self.entries["cpf_dono"].get(),
            "nome_vendedor": self.entries["nome_vendedor"].get(),
            "cpf_vendedor": self.entries["cpf_vendedor"].get(),
            "clausula_5": get_textarea_value(self.entries["clausula_5"], "Cláusula 5"),
            "clausula_6": get_textarea_value(self.entries["clausula_6"], "Cláusula 6"),
            "clausula_7": get_textarea_value(self.entries["clausula_7"], "Cláusula 7")
        }
