from modules.phone_lookup import lookup_number
from modules.email_extractor import extract_identity
from modules.google_dorks import run_dork_scan
from modules.report_writer import write_report
from utils.banner import show_banner
from utils.ui import (
    print_title, print_section, print_result,
    print_warning, print_error, print_info
)
from colorama import Fore, Style, init
import socket

# Initialize colorama
init(autoreset=True)

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

def get_number():
    raw = input(Fore.CYAN + "\n📞 Enter phone number (with country code, e.g. +91xxxxxxxxxx): " + Style.RESET_ALL).strip()
    if not raw.startswith("+") and len(raw) == 10:
        return "+91" + raw
    elif raw.startswith("+") and len(raw) >= 10:
        return raw
    else:
        print_error("❌ Invalid number format.")
        return None

def main():
    show_banner()
    print_title("Welcome to NulOs - The Phone Number OSINT Toolkit")

    number = get_number()
    if not number:
        return

    if not check_internet():
        print_error("No internet connection. Please check your network.")
        return

    print_info("\n[✔] Number received: " + number)
    print_info("[...] Starting investigation...\n")

    # Step 1: Phone lookup
    print_section("📞 Phone Information")
    phone_info = lookup_number(number)
    if phone_info.get("valid"):
        print_result("Region", phone_info["region"])
        print_result("Carrier", phone_info["carrier"])
        print_result("Country Code", f"+{phone_info['country_code']}")
        print_result("Local Number", phone_info["national_number"])
        print_result("Timezone(s)", ", ".join(phone_info.get("timezones", [])))
    else:
        print_error("Phone number is invalid or untraceable.")
        if "error" in phone_info:
            print_error(phone_info["error"])
        return

    # Step 2: Extract identity
    print_section("🧠 Identity Extraction")
    identity = extract_identity(number)
    print_result("Name", identity["name"])
    print_result("Email", identity["email"])
    print_result("Company", identity["company"])
    print_result("Source", identity["source"])

    # Step 3: Google Dorks
    print_section("🔍 Google Dork Results")
    dork_results = run_dork_scan(number)

    if not dork_results:
        print_warning("No relevant results found via dorks.")

    # Step 4: Report saving
    print_section("💾 Report Summary")
    report_path = write_report(number, phone_info, identity, dork_results)
    if "ERROR" not in report_path:
        print_result("Report saved to", report_path)
    else:
        print_error(report_path)

    print(Fore.GREEN + "\n[✔] Investigation complete. | NulOs v1.1 Stable\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
