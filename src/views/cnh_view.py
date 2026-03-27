"""
View de Informações do Cliente
Segunda tela do formulário
"""

import customtkinter as ctk
from src.components.document_panel import DocumentPanel
from src.components.fields import create_field, create_inline_field, next_btn
from sysvars import SysVars as svar


class CNH(ctk.CTkFrame):

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
        
        title_label = ctk.CTkLabel(title_frame, text="Informações do Cliente", font=("Segoe UI", 24, "bold"), text_color="white")
        title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        form_frame = ctk.CTkFrame(left_frame, fg_color="white", corner_radius=15)
        form_frame.pack(fill="both", expand=True)
        
        scroll_frame = ctk.CTkScrollableFrame(form_frame, fg_color="transparent", scrollbar_button_color="#d1d5db", scrollbar_button_hover_color="#9ca3af")
        scroll_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        self.entries["nome"] = create_field(scroll_frame, "Nome Completo", row=0)
        
        row_frame_1 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_1.grid(row=1, column=0, sticky="ew", pady=10)
        row_frame_2 = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row_frame_2.grid(row=2, column=0, sticky="ew", pady=10)
        scroll_frame.grid_columnconfigure(0, weight=1)
        
        self.entries["cpf"] = create_inline_field(row_frame_1, "CPF", 0)
        self.entries["rg"] = create_inline_field(row_frame_1, "RG", 1)
        self.entries["orgao_emissor"] = create_inline_field(row_frame_1, "Órgão Emissor", 2)
        self.entries["data_nascimento"] = create_inline_field(row_frame_2, "Data de Nascimento", 0)
        self.entries["contato"] = create_inline_field(row_frame_2, "Contato", 1)
        self.entries["endereco"] = create_field(scroll_frame, "Endereço", row=3)
        
        row_frame_2.grid_columnconfigure(0, weight=1)
        row_frame_2.grid_columnconfigure(1, weight=2)
        
        next_btn(form_frame, self.on_next)
        
        self.document_panel = DocumentPanel(main_container, title="Documento CNH", width=350, is_crlv=False, on_document_loaded=self.set_data)
        self.document_panel.pack(side="right", fill="y")



    
    def get_data(self):
        """Retorna os dados do formulário"""
        img_path = svar.UPLOADS_PATH / "document.png" if self.document_panel.get_image_status else None

        return {
            "nome": self.entries["nome"].get(),
            "cpf": self.entries["cpf"].get(),
            "rg": self.entries["rg"].get(),
            "orgao_emissor": self.entries["orgao_emissor"].get(),
            "data_nascimento": self.entries["data_nascimento"].get(),
            "contato": self.entries["contato"].get(),
            "endereco": self.entries["endereco"].get(),
            "documento_imagem": img_path
        }




    def set_data(self, data):
        """Atualiza os dados do formulário"""
        
        self.entries["nome"].delete(0, "end")
        self.entries["nome"].insert(0, data["pessoa_nome"])
        self.entries["cpf"].delete(0, "end")
        self.entries["cpf"].insert(0, data["pessoa_cpf"])
        self.entries["rg"].delete(0, "end")
        self.entries["rg"].insert(0, data["pessoa_rg"])
        self.entries["orgao_emissor"].delete(0, "end")
        self.entries["orgao_emissor"].insert(0, data["orgao_emissor"])
        self.entries["data_nascimento"].delete(0, "end")
        self.entries["data_nascimento"].insert(0, data["pessoa_data_nascimento"])




    def process_document(self):
        self.document_panel.load_document()