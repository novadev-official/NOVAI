import os
import sys
import time
import socket
import platform
import subprocess
from datetime import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.markdown import Markdown
    from rich.prompt import Prompt
except ImportError:
    print("Error: 'rich' library not found. Please run 'pip install rich'")
    sys.exit(1)

console = Console()

BANNER = """
[bold cyan]
 ███▄    █  ▒█████   ██▒   █▓ ▄▄▄       ██▓
 ██ ▀█   █ ▒██▒  ██▒▓██░   █▒▒████▄    ▓██▒
▓██  ▀█ ██▒▒██░  ██▒ ▓██  █▒░▒██  ▀█▄  ▒██▒
▓██▒  ▐▌██▒▒██   ██░  ▒██ █░░░██▄▄▄▄██ ░██░
▒██░   ▓██░░ ████▓▒░   ▒▀█░   ▓█   ▓██▒░██░
░ ▒░   ▒ ▒ ░ ▒░▒░▒░    ░ ▐░   ▒▒   ▓▒█░░▓  
░ ░░   ░ ▒░  ░ ▒ ▒░    ░ ░░    ▒   ▒▒ ░ ▒ ░
   ░   ░ ░ ░ ░ ░ ▒       ░░    ░   ▒    ▒ ░
         ░     ░ ░        ░        ░  ░ ░  
[/bold cyan]
[bold white]               N O V A   A I   T E R M I N A L[/bold white]
[dim white]                 The Future of Kali Linux CLI[/dim white]

[bold magenta]NOVAI - Kali Linux Security Tool[/bold magenta]
[cyan]Author  :[/cyan] [white]Shibin KS[/white]
[cyan]Company :[/cyan] [white]Nova Developments[/white]
[cyan]Version :[/cyan] [white]v1.0[/white]
[blue]cybernova171717@gmail.com[/blue]
[link=https://novadev-official.github.io/nova-ui-foundations/][u]https://novadev-official.github.io/nova-ui-foundations/[/u][/link]

[italic yellow]Use for educational purposes only[/italic yellow]
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    console.print(Panel(BANNER, border_style="bright_magenta", expand=False))

def get_system_info():
    info = {
        "OS": platform.system(),
        "Release": platform.release(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "Local IP": socket.gethostbyname(socket.gethostname()),
        "Current Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

def display_dashboard():
    info = get_system_info()
    table = Table(title="System Status", show_header=False, box=None)
    for key, value in info.items():
        table.add_row(f"[bold cyan]{key}:[/bold cyan]", f"[white]{value}[/white]")
    
    console.print(Panel(table, title="[bold green]NOVAI CORE[/bold green]", border_style="green"))

from tools.scanner import run_port_scan

def scan_ports(target):
    run_port_scan(console, target)

def mock_ai_assistant():
    console.print(Panel("Welcome to NOVAI Assistant. Ask me anything about Linux or Security.", title="[bold magenta]NOVAI AI[/bold magenta]"))
    while True:
        query = Prompt.ask("[bold magenta]NOVAI[/bold magenta] >")
        if query.lower() in ['exit', 'quit', 'back']:
            break
        
        # Simple mock responses for a "premium" feel
        with console.status("[bold blue]Thinking..."):
            time.sleep(1)
            if "nmap" in query.lower():
                console.print("[cyan]NOVAI:[/cyan] Nmap is a network scanner. You can use `nmap -sV <target>` to detect service versions.")
            elif "password" in query.lower():
                console.print("[cyan]NOVAI:[/cyan] For password security, I recommend using strong entropy and tools like John the Ripper for testing.")
            elif "who are you" in query.lower():
                console.print("[cyan]NOVAI:[/cyan] I am NOVAI, a terminal assistant designed for Kali Linux enthusiasts.")
            else:
                console.print(f"[cyan]NOVAI:[/cyan] Analyzing '{query}'... I am a simulated AI, but I can help you with base commands. Try asking about 'nmap' or 'security'.")

def main_menu():
    while True:
        clear_screen()
        show_banner()
        display_dashboard()
        
        console.print("\n[bold white]MAIN MENU[/bold white]")
        console.print("[1] [cyan]Network Scanner[/cyan]")
        console.print("[2] [cyan]NOVAI AI Assistant[/cyan]")
        console.print("[3] [cyan]System Information[/cyan]")
        console.print("[4] [red]Exit[/red]")
        
        choice = Prompt.ask("\n[bold yellow]Select an option[/bold yellow]", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            target = Prompt.ask("Enter target IP or Domain (e.g., 127.0.0.1)")
            scan_ports(target)
            input("\nPress Enter to return...")
        elif choice == "2":
            mock_ai_assistant()
        elif choice == "3":
            display_dashboard()
            input("\nPress Enter to return...")
        elif choice == "4":
            console.print("[bold red]Shutting down NOVAI... Goodbye.[/bold red]")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted. Exiting...[/bold red]")
        sys.exit(0)
