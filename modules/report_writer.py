import os
import json
from datetime import datetime
from pathlib import Path

def sanitize_filename(number):
    """Remove symbols and format filename cleanly"""
    return number.replace("+", "").replace("-", "").strip()

def write_report(number, phone_info, identity, google_results=[]):
    try:
        # Create output folder if not exists
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        # Timestamped + clean filename
        clean_number = sanitize_filename(number)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"{clean_number}_{timestamp}"

        # ========== TEXT REPORT ==========
        txt_path = output_dir / f"{base_filename}.txt"
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write("=" * 60 + "\n")
            txt_file.write("📞 Phone OSINT Report - NulOs v1.1\n")
            txt_file.write(f"Generated: {datetime.now()}\n")
            txt_file.write("=" * 60 + "\n\n")

            txt_file.write("📞 Phone Info:\n")
            for key in ["region", "carrier", "country_code", "national_number", "valid", "timezones"]:
                if key in phone_info:
                    txt_file.write(f"- {key}: {phone_info[key]}\n")

            txt_file.write("\n🧠 Extracted Identity:\n")
            for key in ["name", "email", "company", "source"]:
                txt_file.write(f"- {key}: {identity.get(key, 'N/A')}\n")

            if google_results:
                txt_file.write("\n🔍 Google Dork Results:\n\n")
                for res in google_results:
                    txt_file.write(f"[Dork] {res['query']}\n")
                    txt_file.write(f"  ↪ URL    : {res['url']}\n")
                    if res.get("snippet"):
                        txt_file.write(f"  ↪ Snippet: {res['snippet']}\n")
                    txt_file.write("\n")
            else:
                txt_file.write("\n🔍 Google Dork Results: None found or search failed.\n")

        # ========== JSON REPORT ==========
        json_path = output_dir / f"{base_filename}.json"
        report_data = {
            "timestamp": str(datetime.now()),
            "number": number,
            "phone_info": phone_info,
            "identity": identity,
            "google_dorks": google_results
        }

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(report_data, json_file, indent=4)

        return str(txt_path)

    except Exception as e:
        return f"ERROR: Failed to write report – {e}"
