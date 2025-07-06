from modules.phone_lookup import lookup_number
from modules.email_extractor import extract_identity
from modules.report_writer import write_report  # ✅ Make sure this is imported
from utils.banner import show_banner
from colorama import Fore, Style
import os

def main():
    show_banner()
    print(Fore.YELLOW + "Welcome to NulOs - The Phone Number OSINT Toolkit" + Style.RESET_ALL)

    number = input(Fore.CYAN + "\nEnter phone number (with country code, e.g. +91xxxxxxxxxx): " + Style.RESET_ALL)

    # Auto-add +91 if missing and number is 10 digits
    if not number.startswith("+"):
        if len(number) == 10:
            number = "+91" + number
        else:
            print(Fore.RED + "\n❌ Invalid number format." + Style.RESET_ALL)
            return

    print(Fore.GREEN + f"\n[✔] Number received: {number}")
    print("[...] Starting investigation...\n" + Style.RESET_ALL)

    # 📞 Phone number lookup
    info = lookup_number(number)

    if info["valid"]:
        print(Fore.MAGENTA + "📍 Region      :", info["region"])
        print("📶 Carrier     :", info["carrier"])
        print("🌍 Country Code: +{}".format(info["country_code"]))
        print("📱 Local Number:", str(info["national_number"]) + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n❌ Invalid number or failed to process.")
        if "error" in info:
            print("Error:", info["error"])
        return

    # 🧠 Simulated identity extraction
    identity = extract_identity(number)

    print(Fore.BLUE + "\n👤 Name       :", identity["name"])
    print("📧 Email      :", identity["email"])
    print("🏢 Company    :", identity["company"])
    print("🔗 Source     :", identity["source"] + Style.RESET_ALL)

    # 📝 Save report using report_writer module
    report_path = write_report(number, info, identity)
    if "ERROR" not in report_path:
        print(Fore.YELLOW + f"\n[💾] Report saved to {report_path}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\n[✘] {report_path}" + Style.RESET_ALL)

    print(Fore.GREEN + "\n[✔] Investigation finished. | NulOs v1.0 Beta" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
