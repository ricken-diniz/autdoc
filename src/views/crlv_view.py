"""
View de Informações do Carro
Primeira tela do formulário
"""

import customtkinter as ctk
from src.components.document_panel import DocumentPanel
from src.components.fields import create_field, create_inline_field, next_btn
from sysvars import SysVars as svar


class CRLV(ctk.CTkFrame):

    def __init__(self, parent, on_next):
        super().__init__(parent, fg_color="transparent")
        
        self.on_next = on_next
        self.entries = {}
        
        self.create_widgets()
    



    def create_widgets(self):
        """Cria os widgets da view"""
        
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True)
        
        left_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        title_frame = ctk.CTkFrame(left_frame, fg_color="#6b7280", corner_radius=15, height=80)
        title_frame.pack(fill="x", pady=(0, 20))
        title_frame.pack_propagate(False)

        title_label = ctk.CTkLabel(title_frame, text="Informações do Carro", font=("Segoe UI", 24, "bold"), text_color="white")
        title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        form_frame = ctk.CTkFrame(left_frame, fg_color="white", corner_radius=15)
        form_frame.pack(fill="both", expand=True)
        
        scroll_frame = ctk.CTkScrollableFrame(form_frame, fg_color="transparent", scrollbar_button_color="#d1d5db", scrollbar_button_hover_color="#9ca3af")
        scroll_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        row_frame_1 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_1.grid(row=1, column=0, sticky="ew", pady=10)
        scroll_frame.grid_columnconfigure(0, weight=1)
        
        self.entries["ano_fabricacao"] = create_inline_field(row_frame_1, "Ano de fabricação", 0)
        self.entries["ano_modelo"] = create_inline_field(row_frame_1, "Ano Modelo", 1)
        self.entries["ano_emplacamento"] = create_inline_field(row_frame_1, "Ano do Emplacamento", 2)
        self.entries["modelo"] = create_field(scroll_frame, "Modelo do Carro no formato MARCA/MODELO DO CARRO", row=0)
        self.entries["renavam"] = create_field(scroll_frame, "Renavam", row=2)
        self.entries["chassi"] = create_field(scroll_frame, "Chassi", row=3)
        self.entries["placa"] = create_field(scroll_frame, "Placa do Carro", row=4)
        self.entries["cor"] = create_field(scroll_frame, "Cor do Carro", row=5)
        self.entries["quilometragem"] = create_field(scroll_frame, "Quilometragem", row=6)
        
        next_btn(form_frame, self.on_next)
        
        self.document_panel = DocumentPanel(
            main_container,
            title="Documento CRLV",
            width=350,
            on_document_loaded=self.set_data
        )
        self.document_panel.pack(side="right", fill="y")




    def get_data(self):
        """Retorna os dados do formulário"""
        img_path = svar.UPLOADS_PATH / "document.png" if self.document_panel.get_image_status else None

        return {
            "modelo": self.entries["modelo"].get(),
            "ano_fabricacao": self.entries["ano_fabricacao"].get(),
            "ano_modelo": self.entries["ano_modelo"].get(),
            "ano_emplacamento": self.entries["ano_emplacamento"].get(),
            "renavam": self.entries["renavam"].get(),
            "chassi": self.entries["chassi"].get(),
            "placa": self.entries["placa"].get(),
            "cor": self.entries["cor"].get(),
            "quilometragem": self.entries["quilometragem"].get(),
            "documento_imagem": img_path
        }




    def set_data(self, data):
        """Atualiza os dados do formulário"""
        
        self.entries["modelo"].delete(0, "end")
        self.entries["modelo"].insert(0, data["carro_modelo"])
        self.entries["ano_fabricacao"].delete(0, "end")
        self.entries["ano_fabricacao"].insert(0, data["ano_fabricacao"])
        self.entries["ano_modelo"].delete(0, "end")
        self.entries["ano_modelo"].insert(0, data["ano_modelo"])
        self.entries["ano_emplacamento"].delete(0, "end")
        self.entries["ano_emplacamento"].insert(0, data["carro_emplacamento"])
        self.entries["renavam"].delete(0, "end")
        self.entries["renavam"].insert(0, data["carro_renavam"])
        self.entries["chassi"].delete(0, "end")
        self.entries["chassi"].insert(0, data["carro_chassi"])
        self.entries["placa"].delete(0, "end")
        self.entries["placa"].insert(0, data["carro_placa"])
        self.entries["cor"].delete(0, "end")
        self.entries["cor"].insert(0, data["carro_cor"])




    def process_document(self):
        self.document_panel.load_document()
        
