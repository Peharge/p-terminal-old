# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import sys
import getpass
import subprocess
import threading
import time
import importlib.util
import os
from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

required_packages = [
    "requests", "py-cpuinfo", "psutil"
]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"[{timestamp()}] [ERROR] Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{timestamp()}] [PASS] Virtual environment {venv_path} activated.")


def ensure_packages_installed(packages):
    """Installiert fehlende Pakete effizient."""
    to_install = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if to_install:
        print(f"[{timestamp()}] [INFO] Installing missing packages: {', '.join(to_install)}...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + to_install, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print(f"[{timestamp()}] [PASS] All missing packages installed.")
    else:
        print(f"[{timestamp()}] [INFO] All required packages are already installed.")


# Virtuelle Umgebung aktivieren und Pakete sicherstellen
venv_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)

import os
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
from typing import Tuple
import pip
import subprocess
import winreg

# Farbcodes definieren
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"


def format_bytes(byte_value: int) -> float:
    """Hilfsfunktion, um Bytes in GB umzuwandeln"""
    return round(byte_value / (1024 ** 3), 2)


def get_system_info() -> dict:
    """Funktion, um alle Systeminformationen zu sammeln"""
    system_info = {}

    # OS-Informationen
    system_info['os_name'] = platform.system()
    system_info['os_version'] = platform.version()
    system_info['os_release'] = platform.release()
    system_info['os_arch'] = platform.architecture()[0]

    # CPU-Informationen
    cpu_info = cpuinfo.get_cpu_info()
    system_info['cpu_model'] = cpu_info.get("brand_raw", "N/A")
    system_info['cpu_arch'] = cpu_info.get("arch", "N/A")
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)
    system_info['cpu_threads'] = psutil.cpu_count(logical=True)
    system_info['cpu_freq'] = psutil.cpu_freq().max if psutil.cpu_freq() else "N/A"

    # RAM Informationen
    ram = psutil.virtual_memory()
    system_info['ram_total'] = format_bytes(ram.total)
    system_info['ram_used'] = format_bytes(ram.used)
    system_info['ram_free'] = format_bytes(ram.available)
    system_info['ram_usage'] = ram.percent

    # Swap Informationen
    swap = psutil.swap_memory()
    system_info['swap_total'] = format_bytes(swap.total)
    system_info['swap_used'] = format_bytes(swap.used)
    system_info['swap_free'] = format_bytes(swap.free)

    # Festplatteninformationen
    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    system_info['storage_total'] = format_bytes(total_storage)
    system_info['storage_used'] = format_bytes(used_storage)
    system_info['storage_free'] = format_bytes(free_storage)

    # Netzwerkinformationen
    system_info['hostname'] = socket.gethostname()
    system_info['ip_address'] = socket.gethostbyname(system_info['hostname'])

    # Python und Pip Version
    system_info['python_version'] = platform.python_version()
    try:
        system_info['pip_version'] = subprocess.check_output(['pip', '--version'], text=True).split()[1]
    except Exception as e:
        system_info['pip_version'] = f'Error: {e}'

    # Netzwerk-Interfaces
    network_interfaces = psutil.net_if_addrs()
    interfaces_info = {}
    for interface, addresses in network_interfaces.items():
        interface_details = {}
        for address in addresses:
            if address.family == socket.AF_INET:
                interface_details['IPv4'] = address.address
            elif address.family == socket.AF_INET6:
                interface_details['IPv6'] = address.address
            elif address.family == psutil.AF_LINK:
                interface_details['MAC'] = address.address
        interfaces_info[interface] = interface_details
    system_info['network_interfaces'] = interfaces_info

    # Load Average
    if system_info['os_name'] == "Windows":
        system_info['load_avg'] = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    else:
        try:
            load_avg_values = os.getloadavg()
            system_info['load_avg'] = {
                "1m": load_avg_values[0],
                "5m": load_avg_values[1],
                "15m": load_avg_values[2]
            }
        except OSError:
            system_info['load_avg'] = "Not available"

    # Uptime des Systems
    uptime_seconds = time.time() - psutil.boot_time()
    system_info['uptime'] = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    # Benutzerinformationen
    user_info = psutil.users()
    system_info['user_info'] = [{
        'user': user.name,
        'terminal': user.terminal or 'N/A',
        'started': time.ctime(user.started)
    } for user in user_info]

    return system_info

def get_powershell_version():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving PowerShell version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] PowerShell is not installed or not in the PATH."

def get_wsl_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[0]  # WSL-Version extrahieren
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_kernel_version():
    try:
        result = subprocess.run(
            ["wsl", "uname", "-r"],
            capture_output=True, text=True, check=True
        )
        kernel_version = result.stdout.strip()
        return kernel_version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving kernel version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_wslg_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[4]  # 5. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_msrpc_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[6]  # 7. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_direct3d_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[8]  # 9. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_dxcore_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[10]  # 11. Zeile extrahieren
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installed or not in the PATH."

def get_visual_studio_version():
    try:
        # Open the registry key for Visual Studio
        registry_path = r"SOFTWARE\Microsoft\VisualStudio\14.0\Setup\VisualStudio"  # for Visual Studio 2015 (adjust the version accordingly)
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            version, _ = winreg.QueryValueEx(key, "Version")
            return version
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] Visual Studio not found"

def get_ollama_version():
    # First attempt: Query version
    try:
        return subprocess.check_output(['ollama', '--version'], text=True).strip()
    except subprocess.CalledProcessError:
        # If no running instance: Start Ollama
        try:
            subprocess.check_output(['ollama', 'start'], text=True)
        except subprocess.CalledProcessError:
            return f"[{timestamp()}] [INFO] Warning: Could not start Ollama."
        # Second attempt: Query version again
        try:
            return subprocess.check_output(['ollama', '--version'], text=True).strip()
        except subprocess.CalledProcessError:
            return f"[{timestamp()}] [INFO] Warning: Could not connect to a running Ollama instance."

def print_system_info(system_info: dict):
    """Funktion, um die Systeminformationen im Terminal auszugeben"""

    title = f"PP-Terminal - {os.getlogin()}"
    line = "-" * len(title)

    print(f"""
                   ██████      
                ████████████                                             {blue}{title}{reset}
             ██████████████████                                          {line}
          ████████████████████████                                       {blue}P-Terminal Version{reset}: 1
       ██████████████████████████████                                    {blue}PP-Terminal Version{reset}: 4
       █████████████████████████████████                                 {blue}PP-Terminal Launcher Version{reset}: 4
       ████████████████████████████████████                              {blue}Peharge C Compiler Version{reset}: 4
       ███████████████████████████████████████                           {blue}Peharge C++ Compiler Version{reset}: 4
       ██████████████████████████████████████████                        {blue}P-Terminal License{reset}: MIT
       █████████████████████████████████████████████                     {blue}MAVIS Version{reset}: 4.3
       ████████████       █████████████████████████████                  {blue}MAVIS Launcher Version{reset}: 4
       █████████             █████████████████████████████               {blue}MAVIS Terminal Version{reset}: 5
       ██████                   █████████████████████████████            {blue}MAVIS License{reset}: MIT
        ███           █████         ████████████████████████████╗        {blue}OS{reset}: {system_info['os_name']} {system_info['os_release']}    
                   ██████████         ██████████████████████████║        {blue}Version{reset}: {system_info['os_version']}      
                ████████████████         ███████████████████████║        {blue}Architecture{reset}: {system_info['os_arch']}       
             ██████████████████████         ████████████████████║        {blue}Hostname{reset}: {system_info['hostname']}          
          ████████████████████████████╗        █████████████████║        {blue}IP Address{reset}: {system_info['ip_address']}        
        █████████████████████████████╔╝        █████████████████║        {blue}CPU{reset}: {system_info['cpu_model']}        
       ███████████████████████████╔══╝      ████████████████████║        {blue}Architecture{reset}: {system_info['cpu_arch']} 
       ████████████████████████╔══╝      ███████████████████████║        {blue}Max Frequency{reset}: {system_info['cpu_freq']} MHz     
        ████████████████████╔══╝     ███████████████████████████║        {blue}RAM Usage{reset}: {system_info['ram_usage']}%     
        █████████████████╔══╝     █████████████████████████████╔╝        {blue}RAM Total{reset}: {system_info['ram_total']} GB       
        ███████████████╔═╝     █████████████████████████████╔══╝         {blue}PIP Version{reset}: {pip.__version__}      
        ███████████████║    █████████████████████████████╔══╝            {blue}PowerShell Version{reset}: {get_powershell_version()}
        ███████████████║    ██████████████████████████╔══╝               {blue}WSL Version{reset}: {get_wsl_version()}
        ███████████████║    ███████████████████████╔══╝                  {blue}Kernelversion{reset}: {get_kernel_version()}
        ███████████████║    ████████████████████╔══╝                     {blue}WSLg Version{reset}: {get_wslg_version()}
        ███████████████║    █████████████████╔══╝                        {blue}MSRDC Version{reset}: {get_msrpc_version()}
        ███████████████║    ██████████████╔══╝                           {blue}Direct3D Version{reset}: {get_direct3d_version()}
        ███████████████║    ███████████╔══╝                              {blue}DXCore Version{reset}: {get_dxcore_version()}
        ███████████████║    ████████╔══╝                                 {blue}Python Version{reset}: {system_info['python_version']}
        ███████████████║    █████╔══╝                                    {blue}PowerShell Version{reset}: {subprocess.check_output(['git', '--version'], text=True).strip()}
        ███████████████║    ██╔══╝                                       {blue}Ollama Version{reset}: {get_ollama_version()}
        ███████████████╚═╗  ╚═╝                                          {blue}Visual Studio Version{reset}: {get_visual_studio_version()}
        █████████████████╚╗                                              {blue}Rust Version{reset}: {subprocess.check_output(['rustc', '--version'], text=True).strip()}
        ██████████████████║                                              
        █████████████╔════╝                                              {show_color_palette_1()}
        ██████████╔══╝                                                   {show_color_palette_3()}
        ██████╔═══╝                             
        ███╔══╝
        ╚══╝
""")

def show_color_palette_1():
    """Funktion zur Anzeige der 16 Farbpaletten ohne Abstände und Zahlen"""
    palette = ""

    # Anzeige der Farben (0-7)
    for i in range(8):
        palette += f"\033[48;5;{i}m  \033[0m"  # Farben ohne Zahlen und ohne Abstände

    return palette

def show_color_palette_3():
    palette = ""
    # Anzeige der helleren Farben (8-15)
    for i in range(8, 16):
        palette += f"\033[48;5;{i}m  \033[0m"  # Farben ohne Zahlen und ohne Abstände

    # Noch ein Zeilenumbruch am Ende
    return palette

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
