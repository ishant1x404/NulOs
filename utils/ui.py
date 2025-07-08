from colorama import Fore, Style

def print_title(text):
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.YELLOW + f"🔍 {text.center(50)}")
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)

def print_section(title):
    print("\n" + Fore.CYAN + f"▶ {title}".ljust(60, " "))
    print(Fore.CYAN + "-" * 50 + Style.RESET_ALL)

def print_result(label, value):
    print(Fore.GREEN + f"✔ {label}: " + Style.RESET_ALL + f"{value}")

def print_warning(text):
    print(Fore.YELLOW + f"⚠ {text}" + Style.RESET_ALL)

def print_error(text):
    print(Fore.RED + f"✖ {text}" + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + f"{text}" + Style.RESET_ALL)

def print_dork(query, url, snippet=None):
    print(Fore.BLUE + f"\n[Dork] {query}" + Style.RESET_ALL)
    print(Fore.GREEN + f"  ↪ URL    : " + Style.RESET_ALL + url)
    if snippet:
        print(Fore.YELLOW + f"  ↪ Snippet: " + Style.RESET_ALL + snippet)
