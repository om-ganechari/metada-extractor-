# MetaSniff: Image and Document Metadata Extractor 🕵️‍♂️📄🖼️

MetaSniff is a lightweight Python tool designed for **ethical metadata extraction** from common image and document formats.  
It helps identify hidden or embedded information in files—useful for cybersecurity, audits, digital forensics, or even fun fact-checking!

## 🔍 What It Does

- Extracts **EXIF metadata** from `.jpg`, `.jpeg`, `.png` images
- Pulls **document properties** from `.pdf` files (author, title, creation date, etc.)
- Retrieves **Word doc info** from `.docx` (title, author, revision history, etc.)

## ✅ Supported File Types

| Type     | Extensions         | Metadata Extracted |
|----------|--------------------|---------------------|
| Image    | .jpg, .jpeg, .png  | EXIF info (camera, GPS, etc.) |
| PDF      | .pdf               | Document properties |
| Word     | .docx              | Core file metadata  |

## 🚀 How to Run (VS Code or Local)

1. Clone this repo:
```bash
git clone https://github.com/your-username/metasniff.git
cd metasniff
```

2. Create virtual environment & install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the script from terminal or inside your IDE.

## 👨‍🏫 Educational Use Cases

- Digital forensics practice 🧠  
- Metadata redaction before uploading 🔐  
- Building blocks for automation or compliance tools 💼  

## ⚠️ Ethical Use Only

Please use this tool only on files **you own or have permission to analyze**. Unauthorized extraction may violate privacy or legal boundaries.

---
Made with ❤️ by Omii | Powered by Python 🐍