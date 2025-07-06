# modules/report_writer.py

import os
from datetime import datetime

def write_report(number, info, identity):
    try:
        os.makedirs("output/reports", exist_ok=True)
        filename = f"output/reports/{info['national_number']}.txt"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write("📄 NulOs Investigation Report\n")
            f.write("=" * 40 + "\n")
            f.write(f"Generated On  : {timestamp}\n")
            f.write(f"Phone Number  : {number}\n")
            f.write("-" * 40 + "\n")
            f.write(f"📍 Region      : {info['region']}\n")
            f.write(f"📶 Carrier     : {info['carrier']}\n")
            f.write(f"🌍 Country Code: +{info['country_code']}\n")
            f.write(f"📱 Local Number: {info['national_number']}\n")
            f.write("-" * 40 + "\n")
            f.write(f"👤 Name        : {identity['name']}\n")
            f.write(f"📧 Email       : {identity['email']}\n")
            f.write(f"🏢 Company     : {identity['company']}\n")
            f.write(f"🔗 Source      : {identity['source']}\n")
            f.write("=" * 40 + "\n")
            f.write("Tool          : NulOs v1.0 Beta\n")
            f.write("Author        : Ankush (ishant1x404)\n")

        return filename
    except Exception as e:
        return f"[ERROR] Failed to write report: {e}"
