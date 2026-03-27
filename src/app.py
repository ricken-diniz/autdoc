"""
Aplicação principal CustomTkinter
Gerencia a janela principal e navegação entre views
"""

import threading
import asyncio
from services import AutDocBot
import customtkinter as ctk
from src.views import CNH
from src.views import CRLV
from src.views import GenericInfo
from src.components.tab_navigation import TabNavigation


class AutDocApp(ctk.CTk):

    def __init__(self, bot_token):
        super().__init__()
        self.settings()
        self.create_views()
        self.change_view("CRLV")
        self.log_history = []

        self.telegram_thread = threading.Thread(target=self.start_bot, daemon=True, args=(bot_token,))
        self.telegram_thread.start()
        



    def start_bot(self, bot_token):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.bot = AutDocBot(token = bot_token, ctkApp = self)
    



    def update_log_ui(self, message):
        self.log_history.append(message)
        self.log_view.insert("end", message + "\n")
        self.log_view.see("end")

        if len(self.log_history) > 100:
            self.log_history.pop(0)




    def settings(self):
        self.title("CRLV OCR - Sistema de Cadastro")
        self.geometry("1400x800")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.tab_nav = TabNavigation(
            self.main_container,
            tabs=["CRLV", "CNH", "Adicionais"],
            on_tab_change=self.change_view
        )
        self.tab_nav.pack(fill='x', pady=(0, 20))
        
        self.content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)
        
        self.create_log_footer()

        self.views = {}
        self.current_view = None




    def create_views(self):
        """Cria todas as views da aplicação"""
        self.views["CRLV"] = CRLV(
            self.content_frame,
            on_next=lambda: self.change_view("CNH")
        )
        
        self.views["CNH"] = CNH(
            self.content_frame,
            on_next=lambda: self.change_view("Adicionais")
        )
        
        self.views["Adicionais"] = GenericInfo(
            self.content_frame,
            on_finalize=self.finalize
        )
    



    def change_view(self, view_name):
        """Troca a view atual"""
        if self.current_view and self.current_view in self.views:
            self.views[self.current_view].pack_forget()
        
        if view_name in self.views:
            self.views[view_name].pack(fill="both", expand=True)
            self.current_view = view_name
            
            self.tab_nav.set_active(view_name)
    



    def create_log_footer(self):
        """Cria a seção de logs estilo rodapé"""
        self.log_container = ctk.CTkFrame(self.main_container, height=150)
        self.log_container.pack(fill="x", pady=(10, 0))
        self.log_container.pack_propagate(False) 

        self.log_label = ctk.CTkLabel(self.log_container, text="BOT LOGS", font=ctk.CTkFont(size=10, weight="bold"), text_color="gray")
        self.log_label.pack(anchor="w", padx=10)

        self.log_view = ctk.CTkTextbox(self.log_container, fg_color="#1a1a1a", text_color="#00ff00", font=("Consolas", 12))
        self.log_view.pack(fill="both", expand=True, padx=5, pady=5)




    def finalize(self):
        """Finaliza o formulário e coleta os dados"""
        data = {
            "CRLV": self.views["CRLV"].get_data(),
            "CNH": self.views["CNH"].get_data(),
            "Adicionais": self.views["Adicionais"].get_data()
        }
        
        print("=" * 50)
        print("DADOS COLETADOS:")
        print("=" * 50)
        for section, values in data.items():
            print(f"\n{section.upper()}:")
            for key, value in values.items():
                print(f"  {key}: {value}")
        print("=" * 50)




    def load_doc(self, doc_type):

        if doc_type == "CNH":
            self.views["CNH"].process_document()

        elif doc_type == "CRLV":
            self.views["CRLV"].process_document()

        else:
            raise Exception("INVALID DOC TYPE")
    