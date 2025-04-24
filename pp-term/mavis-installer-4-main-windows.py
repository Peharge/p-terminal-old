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

import os
import platform
import subprocess
import time
import sys

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

def check_ollama_update():
    """
    Prüft, ob eine neue Version von Ollama verfügbar ist, und bietet ein Update an.
    """
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            local_version = result.stdout.strip()
            remote_version = subprocess.run(["curl", "-s", "https://api.ollama.ai/version"],
                                            stdout=subprocess.PIPE, text=True).stdout.strip()

            if local_version != remote_version:
                print(f"{yellow}New Ollama version available: {remote_version} (Current: {local_version}){reset}")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"{green}Ollama updated successfully! Please restart the script.{reset}")
                        exit()
                    elif user_input in ["n", "no"]:
                        print("Skipping update.")
                        break
                    else:
                        print(f"{red}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")

def find_ollama_path():
    """
    Findet den Installationspfad von Ollama basierend auf dem Betriebssystem.
    """
    try:
        if platform.system() == "Windows":
            base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
            return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
        elif platform.system() == "Darwin":  # macOS
            return "/Applications/Ollama.app/Contents/MacOS/Ollama"
        else:
            raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"Error finding Ollama path: {e}")

def check_installed_model(model_name):
    """
    Prüft, ob ein bestimmtes Modell in Ollama installiert ist.
    :param model_name: Name des zu prüfenden Modells (z. B. "phi4").
    :return: True, wenn das Modell installiert ist, andernfalls False.
    """
    try:
        # Use ollama list or another Ollama command to check for installed models
        result = subprocess.run(["ollama", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            models_list = result.stdout.lower()
            if model_name.lower() in models_list:
                return True
            else:
                return False
        else:
            print(f"{red}Error fetching models list from Ollama: {result.stderr}{reset}")
            return False
    except Exception as e:
        print(f"{red}Error checking for installed model: {e}{reset}")
        return False

def start_ollama():
    """
    Startet Ollama, falls es noch nicht läuft.
    """
    try:
        # Überprüfen, ob Ollama bereits läuft
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")

def check_command_installed(command):
    """
    Überprüft, ob ein Befehlszeilentool installiert ist (z. B. ollama).
    :param command: Zu prüfender Befehlsname.
    :return: True, wenn installiert, andernfalls False.
    """
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}: {e}{reset}")
        return False

def run_batch_file(batch_name):
    """Führt die angegebene Batch-Datei aus."""
    file_path = os.path.join(os.path.expanduser("~"), "p-terminal", "pp-term", f"run-{batch_name}.bat")

    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    try:
        print(f"Start: {file_path}")
        exit_code = os.system(file_path)
        if exit_code == 0:
            print(f" '{file_path}' executed successfully.")
        else:
            print(f"Error executing '{file_path}' with exit code {exit_code}.")
    except Exception as e:
        print(f"Execution errors: {e}")

def display_versions():
    """Zeigt verfügbare MAVIS-Versionen und Batch-Dateien an."""
    versions = {
        "mavis-4": ("MAVIS 4 EAP", "NEW - Development of MAVIS 4 has begun – featuring new Vision Models, a more powerful and faster MAVIS Terminal, and access to over 200 models.", ""),
        "mavis-4-3": ("MAVIS 4 EAP", "NEW - Development of MAVIS 4 has begun – featuring new Vision Models, a more powerful and faster MAVIS Terminal, and access to over 200 models.", "")
    }

    print(f"All MAVIS versions are available here:\n\n{green}█{reset} Required LLM model for this MAVIS version is already installed\n{orange}█{reset} Required LLM model for this MAVIS version is not yet installed\n{blue}█{reset} LLM model is available for you - you have all the permissions\n{red}█{reset} LLM model is not available for you - you do not have permission to install the model")
    categories = {}
    for batch_name, (version, description, model_name) in versions.items():
        categories.setdefault(version, []).append((batch_name, description, model_name))

    for i, (version, batch_files) in enumerate(categories.items(), 1):
        print(f"\n{i}. {version}:")
        for batch_name, description, model_name in batch_files:
            # Check if model for the version is installed
            if check_installed_model(model_name):  # Check for the specific model
                print(f"   - {green}{batch_name}{reset}: {description} ({blue}{model_name}{reset} Installed)")
            else:
                print(f"   - {orange}{batch_name}{reset}: {description} ({blue}{model_name}{reset} Not Installed)")

    return versions

def get_user_input(versions):
    """Fragt nach einer MAVIS-Batch-Datei und führt sie aus."""
    while True:
        user_input = input("\nEnter a MAVIS batch file (e.g. 'mavis-4', 'mavis-4-3' or 'mavis-terminal-5'):").strip()
        if user_input in versions:
            run_batch_file(user_input)
            break
        else:
            print("Invalid input. Please try again.")

def main():
    ollama_installed = check_command_installed("ollama")
    if ollama_installed:
        print(f"{green}Ollama is installed.{reset}")
    else:
        print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")

    start_ollama()
    check_ollama_update()

    try:
        versions = display_versions()
        get_user_input(versions)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
