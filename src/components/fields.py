import customtkinter as ctk

def next_btn(frame, command):
    """Cria um componente de botão"""
    next_btn = ctk.CTkButton(
        frame,
        text="Próximo",
        width=200,
        height=40,
        corner_radius=8,
        fg_color="#d1d5db",
        hover_color="#9ca3af",
        text_color="#374151",
        font=("Segoe UI", 14, "bold"),
        command=command
    )
    next_btn.pack(side="right", padx=30, pady=(0, 30))
    return next_btn




def create_field(parent, placeholder, row):
    """Cria um campo de entrada completo"""
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
    entry.grid(row=row, column=0, sticky="ew", pady=10)
    return entry




def create_inline_field(parent, placeholder, column):
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
