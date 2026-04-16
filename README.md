# AutDoc - OCR Document Processing Application

A desktop and Telegram bot application for automated document processing, including OCR, document detection, and data extraction using AI-powered technologies.

## 📋 Overview

AutDoc is a comprehensive document processing solution that:
- **Extracts text** via OCR from detected documents
- **Processes vehicle documents** (CRLV - Vehicle Registration, CNH - Driver's License)
- **Generates formatted documents** (Word templates) from extracted data
- **Provides Telegram integration** for remote document submission and processing
- **Leverages AI** (Google Gemini) for intelligent data extraction and validation

## 🚀 Features

- **Multi-View Support**
  - CRLV (Vehicle Registration Document) processing
  - CNH (Driver's License) processing
  - Generic document information extraction

- **OCR & Document Detection**
  - YOLOv11-based document localization
  - Automatic document cropping
  - Advanced OCR with schema validation

- **AI-Powered Processing**
  - Google Gemini integration for intelligent field extraction
  - Data validation and formatting

- **Telegram Bot Integration**
  - Whitelist-based access control
  - Remote document submission
  - Real-time processing logs
  - User-friendly inline keyboard interactions
  - Use the "/autorizar [id]" command to allow new users

- **Desktop GUI**
  - Modern CustomTkinter interface
  - Tab-based navigation between document types
  - Real-time processing logs
  - Document upload and preview

- **Document Generation**
  - DOCX template support
  - Automated field filling from extracted data

## 📦 Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - `ultralytics` - YOLOv11 model
  - `customtkinter` - Modern GUI framework
  - `python-telegram-bot` - Telegram API wrapper
  - `google-genai` - Google Gemini API
  - `pillow` - Image processing
  - `docxtpl` - DOCX template generation
  - `pydantic` - Data validation
  - `python-dotenv` - Environment variable management

## ⚙️ Setup Instructions

### 1. Clone & Install Dependencies

```bash
cd autdoc
pip install -r requirements.txt
```

### 2. Create `.env` File

Create a `.env` file in the project root with the following variables:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
PRIME_ID=your_telegram_user_id
GEMINI_KEY=your_google_gemini_api_key
NAPS2_USER=your_naps2_username  # Optional: for NAPS2 scanner integration
```

### 3. Obtain Required Keys

- **Telegram Bot Token**: Create a bot via [@BotFather](https://t.me/botfather) on Telegram
- **Your Telegram ID**: Message [@userinfobot](https://t.me/userinfobot) to get your ID
- **Google Gemini API Key**: Get it from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Download YOLOv11 Model

The application expects `yolo11n.pt` in the project root. It will be automatically downloaded on first run.

## 🏃 Running the Application

### Desktop Application

```bash
python main.py
```

This starts:
- The CustomTkinter GUI window
- The Telegram bot in a background thread (daemon)
- Real-time processing logs visible in the GUI

### Project Structure

```
autdoc/
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── sysvars.py              # System variables & configuration
├── yolo11n.pt              # YOLOv11 model file
├── data/
│   ├── telegram/
│   │   └── whitelist.json  # Authorized Telegram user IDs
│   └── uploads/            # Uploaded documents storage
├── src/                    # GUI application code
│   ├── app.py              # Main application class
│   ├── components/         # GUI components
│   │   ├── document_panel.py
│   │   ├── fields.py
│   │   └── tab_navigation.py
│   └── views/              # Document type views
│       ├── cnh_view.py
│       ├── crlv_view.py
│       └── genericinfo_view.py
└── services/               # Core processing services
    ├── bot.py              # Telegram bot implementation
    ├── doc_builder.py      # Document generation
    ├── extractor.py        # Data extraction logic
    ├── scan.py             # Document scanning
    ├── ctk_logging.py      # GUI logging integration
    └── ocr/                # OCR & document detection
        ├── ocr.py
        ├── crop_doc.py
        └── schema.py
```

## 📱 Telegram Bot Usage

The bot is automatically started when running the desktop application. To interact with it:

1. Message your bot on Telegram
2. Only users in the whitelist (`data/telegram/whitelist.json`) can use the bot
3. Submit document images for processing
4. View results and extracted data

## 🔧 Configuration

All system variables are defined in `sysvars.py`:
- **ROOT**: Project root directory
- **DATA_ROOT**: Data storage location
- **WHITELIST_PATH**: Telegram user whitelist
- **UPLOADS_PATH**: Document uploads directory
- **NAPS2_PATH**: Scanner software path (Windows)
- **API Keys**: Loaded from `.env` file

## 📝 License

This project is provided as-is for document processing automation.
