from colorama import Fore, Style
import time

def show_banner():
    banner_text = [
        Fore.MAGENTA + r" _   _       _       ____              ",
        Fore.MAGENTA + r"| \ | |_   _| |__   / ___|  ___  _ __  ",
        Fore.MAGENTA + r"|  \| | | | | '_ \  \___ \ / _ \| '_ \ ",
        Fore.MAGENTA + r"| |\  | |_| | |_) |  ___) | (_) | | | |",
        Fore.MAGENTA + r"|_| \_|\__,_|_.__/  |____/ \___/|_| |_|",
        Fore.CYAN    + r"         [ NulOs v1.1 | OSINT Toolkit ]" + Style.RESET_ALL
    ]

    print("\n")
    for line in banner_text:
        print(line)
        time.sleep(0.05)  # ✨ Add a quick animation feel

    print(Fore.YELLOW + "-" * 50)
    print("📞  Investigate phone numbers like a pro.")
    print("🧠  Extract identity, emails, leaks, dorks.")
    print("🔍  Fast. Silent. Local. Open Source.")
    print("-" * 50 + Style.RESET_ALL)
