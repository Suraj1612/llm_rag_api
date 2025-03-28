import os
import webbrowser
import psutil

def open_chrome():
    """Opens Google Chrome."""
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens the system calculator."""
    os.system("calc" if os.name == "nt" else "gnome-calculator")

def get_cpu_usage():
    """Returns CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def run_shell_command(command: str):
    """Executes a shell command."""
    return os.popen(command).read().strip()

FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "get_cpu_usage": get_cpu_usage,
    "run_shell_command": run_shell_command
}
