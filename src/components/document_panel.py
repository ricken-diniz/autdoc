"""
Painel lateral com visualização de documento
"""

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from services import extractor, scan
import shutil
from sysvars import SysVars as svar

class DocumentPanel(ctk.CTkFrame):

    def __init__(self, parent, title, on_document_loaded, width=350, is_crlv=True):
        super().__init__(parent, fg_color="white", corner_radius=15, width=width)
        
        self.title = title
        self.on_document_loaded = on_document_loaded
        self.is_crlv = is_crlv
        self.loaded_img = False
        
        self.pack_propagate(False)
        self.create_widgets()
    



    def create_widgets(self):
        """Cria os widgets do painel"""
        
        title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=("Segoe UI", 16, "bold"),
            text_color="#1f2937"
        )
        title_label.pack(pady=(20, 10))
        
        self.image_frame = ctk.CTkFrame(
            self,
            fg_color="#f3f4f6",
            corner_radius=10,
            width=300,
            height=400
        )
        self.image_frame.pack(padx=20, pady=10)
        self.image_frame.pack_propagate(False)
        
        self.image_label = ctk.CTkLabel(
            self.image_frame,
            text="Nenhuma imagem carregada",
            font=("Segoe UI", 12),
            text_color="#9ca3af"
        )
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")
        
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)
        
        scan_btn = ctk.CTkButton(
            button_frame,
            text="Escanear",
            width=130,
            height=35,
            corner_radius=8,
            fg_color="#e5e7eb",
            hover_color="#d1d5db",
            text_color="#374151",
            font=("Segoe UI", 13),
            command=self.scan_document
        )
        scan_btn.grid(row=0, column=0, padx=5)
        
        load_btn = ctk.CTkButton(
            button_frame,
            text="Carregar",
            width=130,
            height=35,
            corner_radius=8,
            fg_color="#e5e7eb",
            hover_color="#d1d5db",
            text_color="#374151",
            font=("Segoe UI", 13),
            command=self.select_document
        )
        load_btn.grid(row=0, column=1, padx=5)



    
    def scan_document(self):
        """Simula escaneamento de documento"""

        scan()
        self.load_document()
        


    
    def select_document(self):
        """Carrega documento do sistema de arquivos"""

        file_path = filedialog.askopenfilename(
            title=f"Selecionar {self.title}",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if file_path:
            shutil.copyfile(file_path, svar.UPLOADS_PATH / "document.png")
            self.load_document()
            self.loaded_img = True
    



    def load_document(self):
        """Processa o documento"""
        data = extractor(self.is_crlv)
        self.on_document_loaded(data)
        self.display_image(svar.UPLOADS_PATH / "document.png")
        self.loaded_img = True




    def display_image(self, image_path):
        """Exibe a imagem carregada"""

        self.loaded_img = True
        img = Image.open(image_path)
        
        max_width = 280
        max_height = 380
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        ctk_image = ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(img.width, img.height)
        )
        
        self.image_label.configure(image=ctk_image, text="")
        self.image_label.image = ctk_image


    

    def get_image_status(self):
        return self.loaded_img