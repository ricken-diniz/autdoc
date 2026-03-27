import logging

class CTKLoggingHandler(logging.Handler):

    def __init__(self, app_ctk):

        super().__init__()
        self.app_ctk = app_ctk




    def emit(self, record):

        log_entry = self.format(record)
        
        if hasattr(self.app_ctk, "update_log_ui"):
            self.app_ctk.after(0, self.app_ctk.update_log_ui, log_entry)