# 📞 NulOs v1.1 – Phone Number OSINT Toolkit

NulOs (Number Lookup OSINT) is a fast, modular, and user-friendly toolkit to investigate phone numbers using open-source intelligence (OSINT) techniques.

> ⚠️ For educational and ethical use only.

---

## 🚀 Features

- 📞 Phone number lookup (region, carrier, timezone)
- 🧠 Identity extraction (name, email, company – simulated)
- 🔍 Google Dork scanning (20+ Indian user-targeted dorks)
- 📝 Saves TXT and JSON reports automatically
- 🎨 Colored terminal UI with custom banner
- 💻 Runs locally — no login, API key, or tracking

---

## 📁 Folder Structure

NulOs/ ├── main.py ├── modules/ │   ├── phone_lookup.py │   ├── email_extractor.py │   ├── google_dorks.py │   └── report_writer.py ├── utils/ │   ├── banner.py │   └── ui.py ├── output/ └── README.md

---

## 🛠 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/nulos.git
cd nulos

2. Install dependencies

pip install -r requirements.txt

3. Run the tool

python main.py


---

💡 Example Use

$ python main.py

📞 Enter phone number (with country code): +911234567890

[✔] Region     : India
[✔] Carrier    : Airtel
[✔] Name       : Mohit Rathi
[✔] Email      : mohitrathi37@gmail.com
[✔] Company    : Infosys

🔍 Google Dork: site:quikr.com intext:"1234567890"
🔗 https://www.quikr.com/cars


---

📜 Disclaimer

NulOs is intended for educational and ethical use only.
You must not use this tool to target individuals or collect personal data without consent.

The developer is not responsible for any misuse.


---

👨‍💻 Author

Built by @ishant1x404
Made in 🇮🇳 with Python and purpose.



