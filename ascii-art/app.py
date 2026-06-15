import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

COLORS = {
    "1": (Fore.CYAN,      "Cyan"),
    "2": (Fore.MAGENTA,   "Magenta"),
    "3": (Fore.YELLOW,    "Yellow"),
    "4": (Fore.GREEN,     "Green"),
    "5": (Fore.RED,       "Red"),
    "6": (Fore.WHITE,     "White"),
    "7": (Fore.BLUE,      "Blue"),
}

FONTS = {
    "1": ("big",        "Big"),
    "2": ("banner3",    "Banner"),
    "3": ("slant",      "Slant"),
    "4": ("block",      "Block"),
    "5": ("bubble",     "Bubble"),
    "6": ("digital",    "Digital"),
    "7": ("doom",       "Doom"),
}

def pick(label, options):
    print(f"\n{Style.BRIGHT}Choose {label}:")
    for k, (_, name) in options.items():
        print(f"  {k}) {name}")
    while True:
        choice = input(f"  > ").strip()
        if choice in options:
            return options[choice][0]
        print("  Invalid choice, try again.")

def render(text, font, color):
    art = pyfiglet.figlet_format(text, font=font)
    print()
    for line in art.splitlines():
        print(color + line)
    print(Style.RESET_ALL)

def main():
    print(Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("ASCII ART", font="slant"))
    print("Type text, pick a font and color. Ctrl+C to quit.\n")

    font  = FONTS["1"][0]
    color = COLORS["1"][0]

    while True:
        try:
            text = input(f"{Style.BRIGHT}Text: ").strip()
            if not text:
                continue

            print(f"\n{Style.BRIGHT}  [F] Change font   [C] Change color   [Enter] Keep current")
            action = input("  > ").strip().lower()
            if action == "f":
                font = pick("font", FONTS)
            elif action == "c":
                color = pick("color", COLORS)

            render(text, font, color)

        except KeyboardInterrupt:
            print(Fore.CYAN + "\n\nBye!\n")
            break

if __name__ == "__main__":
    main()
