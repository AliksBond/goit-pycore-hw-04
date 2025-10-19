# dir_tree.py

import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізацiя colorama 
init()

def print_tree(path: Path, prefix: str = ""):
    """
    Директорії з кольоровим форматуванням:
    - Сині директорії
    - Зелені файли
    """
    try:
        entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")
        return

    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "

        if entry.is_dir():
            print(f"{prefix}{Fore.BLUE}{connector}{entry.name}{Style.RESET_ALL}")
            print_tree(entry, prefix + ("    " if index == len(entries) - 1 else "│   "))
        else:
            print(f"{prefix}{Fore.GREEN}{connector}{entry.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python dir_tree.py <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: шлях '{dir_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: шлях '{dir_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.BLUE}{dir_path.resolve().name}{Style.RESET_ALL}")
    print_tree(dir_path)

if __name__ == "__main__":
    main()
