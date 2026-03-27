"""
Aplicação CRLV OCR - Formulário de Cadastro de Veículos
Ponto de entrada principal da aplicação
"""

from src.app import AutDocApp
from sysvars import SysVars as svar
import json

if __name__ == "__main__":

    TELEGRAM_TOKEN = svar.TELEGRAM_TOKEN
    PRIME_ID = svar.PRIME_ID

    try:
        with open(svar.WHITELIST_PATH, 'r') as f:
            ids = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        ids = {"ids": []}

    if PRIME_ID not in ids["ids"]:
        ids["ids"].append(PRIME_ID)
        
        with open(svar.WHITELIST_PATH, 'w') as f:
            json.dump(ids, f, indent=4)

    app = AutDocApp(TELEGRAM_TOKEN)
    app.mainloop()