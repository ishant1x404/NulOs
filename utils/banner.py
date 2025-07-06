from colorama import Fore, Style

def show_banner():
    print(Fore.CYAN + Style.BRIGHT + """
   _   _       _     ____        _     
  | \ | | ___ | |_  / ___|  ___ | |__  
  |  \| |/ _ \| __| \___ \ / _ \| '_ \ 
  | |\  | (_) | |_   ___) | (_) | | | |
  |_| \_|\___/ \__| |____/ \___/|_| |_|
                                       
  """ + Fore.GREEN + Style.BRIGHT + "       Made by Ankush | OSINT Recon Tool\n" + Style.RESET_ALL)
