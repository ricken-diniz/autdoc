from sysvars import SysVars as svar
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CallbackQueryHandler, filters, CommandHandler
import json
from .ctk_logging import CTKLoggingHandler
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class AutDocBot():
    
    def __init__(self, token, ctkApp, drop_peding_updates = True):
        
        self.ctkApp = ctkApp

        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        self.handler = CTKLoggingHandler(self.ctkApp)
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(self.handler)

        self.application = ApplicationBuilder().token(token).build()

        self.uploaded_img = None
        self.last_inline_keyboard = None

        self.application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.show_options))
        self.application.add_handler(CallbackQueryHandler(self.onClick_show_options))
        self.application.add_handler(MessageHandler(filters.PHOTO, self.upload_image))
        self.application.add_handler(CommandHandler("autorizar", self.allow_user))

        self.application.run_polling(drop_pending_updates=drop_peding_updates)
        




    async def upload_image(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    
        if not self.auth_user_handler(update.effective_user.id):
            return
        if self.uploaded_img == None:
            return 
        
        image = update.message.photo[-1]
        image_file = await context.bot.get_file(image.file_id)
        image_path = f"document.png"
        await image_file.download_to_drive(svar.UPLOADS_PATH / image_path)
        
        self.ctkApp.after(0, self.ctkApp.load_doc, self.uploaded_img)
        self.uploaded_img = None
        



    async def show_options(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        if not self.auth_user_handler(update.effective_user.id):
            return
        self.clear_inline_keyboard(update, context)
        self.uploaded_img = None

        keyboard = [
            [
                InlineKeyboardButton("CNH", callback_data='CNH'),
                InlineKeyboardButton("CRLV", callback_data='CRLV'),
            ],
            [InlineKeyboardButton("Cancelar ❌", callback_data='cancelar')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)

        answer = await update.message.reply_text(
                "Oi! A conexão está ok. Escolha uma opção:",
                reply_markup=reply_markup
            )
        
        self.last_inline_keyboard = answer.message_id
        

        

    async def onClick_show_options(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        query = update.callback_query
        await query.answer()

        if query.data != 'cancelar':
            self.uploaded_img = query.data
            await query.edit_message_text(text="Esperando imagem...")
        else:
            await query.edit_message_text(text="Operação cancelada.")




    async def allow_user(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        if not self.auth_user_handler(update.effective_user.id):
            return

        if not context.args:
            await update.message.reply_text("Uso correto: /autorizar 123456789")
            return

        novo_id = int(context.args[0])

        try:
            with open(svar.WHITELIST_PATH, 'r') as f:
                dados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {"ids": []}

        if novo_id not in dados["ids"]:
            dados["ids"].append(novo_id)
            
            with open(svar.WHITELIST_PATH, 'w') as f:
                json.dump(dados, f, indent=4)
            
            await update.message.reply_text(f"✅ Usuário {novo_id} autorizado com sucesso!")
            
        else:
            await update.message.reply_text("⚠️ Este usuário já está na whitelist.")
    



    def auth_user_handler(self, id):

        with open(svar.WHITELIST_PATH, 'r') as f:
            permitidos = json.load(f)["ids"]

        if id not in permitidos:
            return False
        
        return True
    



    async def clear_inline_keyboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        if self.last_inline_keyboard != None and self.last_inline_keyboard in context.user_data:

            try:
                old_msg_id = context.user_data[self.last_inline_keyboard]
                await context.bot.edit_message_reply_markup(
                    chat_id=update.effective_chat.id,
                    message_id=old_msg_id,
                    reply_markup=None
                )

            except Exception as e:
                pass