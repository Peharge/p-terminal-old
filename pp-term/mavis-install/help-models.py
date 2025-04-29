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

import subprocess
import logging
from tabulate import tabulate  # pip install tabulate

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def check_model_with_ollama(model_version: str) -> bool:

    try:
        result = subprocess.run(
            ["ollama", "show", model_version],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        return False
    except Exception as e:
        logging.error(f"Unknown error checking model {model_version}: {e}")
        return False

def fetch_models():
    # Example models with name, version, category, and rating.
    # Notice that the model identifier "xcpp:11b" is the one that users should always use.
    return [
        {"name": "Xc++ I 11b", "av": "only pro users", "version": "xcpp:11b", "category": "Vision Tool", "rating": 4},
        {"name": "Xc++ II 11b", "av": "only pro users", "version": "xcpp2:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Xc++ III 11b", "av": "only pro users", "version": "xcpp3:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Xc++ IV 11b", "av": "only pro users", "version": "xcpp4:11b", "category": "Vision Tool", "rating": 6},
        {"name": "Chat++ I 70b", "av": "only pro users", "version": "chatpp1:70b", "category": "Vision Tool", "rating": 2},
        {"name": "Chat++ II 70b", "av": "only pro users", "version": "chatpp2:70b", "category": "Vision Tool", "rating": 2},
        {"name": "Chat++ III 70b", "av": "only pro users", "version": "chatpp3:70b", "category": "Vision Tool", "rating": 3},
        {"name": "Chat++ IV 70b", "av": "only pro users", "version": "chatpp4:70b", "category": "Vision Tool", "rating": 4},
        {"name": "Chat++ mini 8b", "av": "only pro users", "version": "chatppmini:8b", "category": "Vision Tool", "rating": 4},
        {"name": "Chat++ V 70b", "av": "only pro users", "version": "chatpp5:70b", "category": "Vision Tool", "rating": 5},
        {"name": "Woyzy 8b", "av": "only pro users", "version": "woyzy:8b", "category": "Vision Tool", "rating": 4},
        {"name": "Qwen 3 0.6b", "av": "Free", "version": "qwen3:0.6b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 1.7b", "av": "Free", "version": "qwen3:1.7b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 4b", "av": "Free", "version": "qwen3:4b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 3 8b", "av": "Free", "version": "qwen3:8b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 14b", "av": "Free", "version": "qwen3:14b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 32b", "av": "Free", "version": "qwen3:32b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 30b-A3B", "av": "Free", "version": "qwen3:30b-a3b", "category": "Language Model", "rating": 6},
        {"name": "Qwen 3 235b-A3B", "av": "Free", "version": "qwen3:235b-a22b", "category": "Language Model",
         "rating": 6},
        {"name": "Gemma 3 1b", "av": "Free", "version": "gemma3:1b", "category": "Vision Tool", "rating": 5},
        {"name": "Gemma 3 4b", "av": "Free", "version": "gemma3:4b", "category": "Vision Tool", "rating": 5},
        {"name": "Gemma 3 12b", "av": "Free", "version": "gemma3:12b", "category": "Vision Tool", "rating": 6},
        {"name": "Gemma 3 27b", "av": "Free", "version": "gemma3:27b", "category": "Vision Tool", "rating": 6},
        {"name": "QwQ", "av": "Free", "version": "qwq", "category": "Language Model", "rating": 6},
        {"name": "Mistral Small 3.1 24b", "av": "Free", "version": "mistral-small3.1", "category": "Vision Tool", "rating": 6},
        {"name": "Llama 3.1 8b", "av": "Free", "version": "llama3.1:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 70b", "av": "Free", "version": "llama3.1:70b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.1 405b", "av": "Free", "version": "llama3.1:405b", "category": "Language Model", "rating": 5},
        {"name": "Llama 3.2 1b", "av": "Free", "version": "llama3.2:1b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 3b", "av": "Free", "version": "llama3.2:3b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3.2 Vision 11b", "av": "Free", "version": "llama3.2-vision:11b", "category": "Vision Tool", "rating": 5},
        {"name": "Llama 3.2 Vision 90b", "av": "Free", "version": "llama3.2-vision:90b", "category": "Vision Tool", "rating": 5},
        {"name": "Llama 3.3 70b", "av": "Free", "version": "llama3.3", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 14b", "av": "Free", "version": "phi4", "category": "Language Model", "rating": 5},
        {"name": "Phi 4 mini 3.8b", "av": "Free", "version": "phi4-mini", "category": "Language Model", "rating": 4},
        {"name": "DeepSeek-v3 671", "av": "Free", "version": "deepseek-v3", "category": "Language Model", "rating": 4},
        {"name": "DeepSeek-r1 1.5b", "av": "Free", "version": "deepseek-r1:1.5b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 7b", "av": "Free", "version": "deepseek-r1:7b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 8b", "av": "Free", "version": "deepseek-r1:8b", "category": "Language Model", "rating": 5},
        {"name": "DeepSeek-r1 14b", "av": "Free", "version": "deepseek-r1:14b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 32b", "av": "Free", "version": "deepseek-r1:32b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 70b", "av": "Free", "version": "deepseek-r1:70b", "category": "Language Model", "rating": 6},
        {"name": "DeepSeek-r1 671b", "av": "Free", "version": "deepseek-r1:671b", "category": "Language Model", "rating": 6},
        {"name": "DeepCodern 1.5b", "av": "Free", "version": "deepcoder:1.5b", "category": "Language Model", "rating": 5},
        {"name": "DeepCodern 14b", "av": "Free", "version": "deepcoder:14b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 3b", "av": "Free", "version": "cogito:3b", "category": "Language Model", "rating": 4},
        {"name": "Cogito 8b", "av": "Free", "version": "cogito:8b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 14b", "av": "Free", "version": "cogito:14b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 32b", "av": "Free", "version": "cogito:32b", "category": "Language Model", "rating": 5},
        {"name": "Cogito 70b", "av": "Free", "version": "cogito:70b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 0.5b", "av": "Free", "version": "qwen2.5:0.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 1.5b", "av": "Free", "version": "qwen2.5:1.5b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 3b", "av": "Free", "version": "qwen2.5:3b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 7b", "av": "Free", "version": "qwen2.5:7b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 14b", "av": "Free", "version": "qwen2.5:14b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 32b", "av": "Free", "version": "qwen2.5:32b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 72b", "av": "Free", "version": "qwen2.5:72b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 coder 0.5b", "av": "Free", "version": "qwen2.5-coder:0.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 1.5b", "av": "Free", "version": "qwen2.5-coder:1.5b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 3b", "av": "Free", "version": "qwen2.5-coder:3b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 7b", "av": "Free", "version": "qwen2.5-coder:7b", "category": "Language Model", "rating": 5},
        {"name": "Qwen 2.5 coder 14b", "av": "Free", "version": "qwen2.5-coder:14b", "category": "Language Model", "rating": 5},
        {"name": "Granite 3.3 2b", "av": "Free", "version": "granite3.3:2b", "category": "Language Model", "rating": 4},
        {"name": "Granite 3.3 8b", "av": "Free", "version": "granite3.3:8b", "category": "Language Model", "rating": 4},
        {"name": "Qwen 2.5 coder 32b", "av": "Free", "version": "qwen2.5-coder:32b", "category": "Language Model", "rating": 5},
        {"name": "EXAONE Deep 2.4b", "av": "Free", "version": "exaone-deep:2.4b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 7.8b", "av": "Free", "version": "exaone-deep:7.8b", "category": "Language Model", "rating": 3},
        {"name": "EXAONE Deep 32b", "av": "Free", "version": "exaone-deep:32b", "category": "Language Model", "rating": 3},
        {"name": "DeepScaleR 1.5b", "av": "Free", "version": "deepscaler", "category": "Language Model", "rating": 5},
        {"name": "Mistral Large 123B", "av": "Free", "version": "mistral-large", "category": "Language Model", "rating": 5},
        {"name": "Qwen 0.5b", "av": "Free", "version": "qwen:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 1.8b", "av": "Free", "version": "qwen:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 4b", "av": "Free", "version": "qwen:4b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 7b", "av": "Free", "version": "qwen:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 14b", "av": "Free", "version": "qwen:14b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 32b", "av": "Free", "version": "qwen:32b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 72b", "av": "Free", "version": "qwen:72b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 110b", "av": "Free", "version": "qwen:110b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 0.5b", "av": "Free", "version": "qwen2:0.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 1.5b", "av": "Free", "version": "qwen2:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 7b", "av": "Free", "version": "qwen2:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 110b", "av": "Free", "version": "qwen2:110b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 3.8b", "av": "Free", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3 14b", "av": "Free", "version": "phi3:14b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2b", "av": "Free", "version": "gemma:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 7b", "av": "Free", "version": "gemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 2b", "av": "Free", "version": "gemma3:2b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 9b", "av": "Free", "version": "gemma3:9b", "category": "Language Model", "rating": 3},
        {"name": "Gemma 2 27b", "av": "Free", "version": "gemma3:27b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 7b", "av": "Free", "version": "codellama:7b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 13b", "av": "Free", "version": "codellama:13b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 34b", "av": "Free", "version": "codellama:32b", "category": "Language Model", "rating": 3},
        {"name": "Code Llama 70b", "av": "Free", "version": "codellama:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 7b", "av": "Free", "version": "llama2:8b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 13b", "av": "Free", "version": "llama2:13b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 70b", "av": "Free", "version": "llama2:70b", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 8b", "av": "Free", "version": "llama3:8b", "category": "Language Model", "rating": 4},
        {"name": "Llama 3 70b", "av": "Free", "version": "llama3:70b", "category": "Language Model", "rating": 4},
        {"name": "Mistral 7b", "av": "Free", "version": "mistral", "category": "Language Model", "rating": 4},
        {"name": "Mistral nemo 12b", "av": "Free", "version": "mistral-nemo", "category": "Language Model", "rating": 4},
        {"name": "LlaVA 7b", "av": "Free", "version": "llava:7b", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA 13b", "av": "Free", "version": "llava:13b", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA 34b", "av": "Free", "version": "llava:34b", "category": "Vision Tool", "rating": 3},
        {"name": "Tinyllama 1.1b", "av": "Free", "version": "tinyllama", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 3b", "av": "Free", "version": "starcoder2:3b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 7b", "av": "Free", "version": "starcoder2:7b", "category": "Language Model", "rating": 3},
        {"name": "Star Coder 2 15b", "av": "Free", "version": "starcoder2:15b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 7b", "av": "Free", "version": "llama2-uncensored:7b", "category": "Language Model", "rating": 3},
        {"name": "Llama 2 uncensored 70b", "av": "Free", "version": "llama2-uncensored:70b", "category": "Language Model",
         "rating": 3},
        {"name": "DeepSeek coder v2 16b", "av": "Free", "version": "deepseek-coder-v2:16b", "category": "Language Model",
         "rating": 4},
        {"name": "DeepSeek coder v2 236", "av": "Free", "version": "deepseek-coder-v2:236b", "category": "Language Model",
         "rating": 4},
        {"name": "Minicpm v 8b", "av": "Free", "version": "minicpm-v", "category": "Vision Tool", "rating": 3},
        {"name": "Deepseek coder 1.3b", "av": "Free", "version": "deepseek-coder:1.3b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 6.7b", "av": "Free", "version": "deepseek-coder:6.7b", "category": "Language Model", "rating": 3},
        {"name": "Deepseek coder 33b", "av": "Free", "version": "deepseek-coder:33b", "category": "Language Model", "rating": 3},
        {"name": "Mixtral 8x7b", "av": "Free", "version": "mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Mixtral 8x22b", "av": "Free", "version": "mixtral:8x22b", "category": "Language Model", "rating": 5},
        {"name": "codegemma 2b", "av": "Free", "version": "codegemma:2b", "category": "Language Model", "rating": 3},
        {"name": "codegemma 7b", "av": "Free", "version": "codegemma:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Mixtral 8x7b", "av": "Free", "version": "dolphin-mixtral:8x7b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin Mixtral 8x22b", "av": "Free", "version": "dolphin-mixtral:8x22b", "category": "Language Model",
         "rating": 4},
        {"name": "Open Thinker 7b", "av": "Free", "version": "openthinker:7b", "category": "Language Model", "rating": 4},
        {"name": "Open Thinker 32b", "av": "Free", "version": "openthinker:32b", "category": "Language Model", "rating": 4},
        {"name": "Phi 2.7b", "av": "Free", "version": "phi", "category": "Language Model", "rating": 3},
        {"name": "LlaVA Llama3 8b", "av": "Free", "version": "llava-llama3", "category": "Vision Tool", "rating": 4},
        {"name": "Dolphin 3 8b", "av": "Free", "version": "dolphin3", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 7b", "av": "Free", "version": "olmo2:7b", "category": "Language Model", "rating": 3},
        {"name": "Olmo 2 13b", "av": "Free", "version": "olmo2:13b", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 135m", "av": "Free", "version": "smollm2:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 360m", "av": "Free", "version": "smollm2:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 2 1.7b", "av": "Free", "version": "smollm2:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 7b", "av": "Free", "version": "wizardlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Wizardlm 2 8x22b", "av": "Free", "version": "wizardlm2:8x22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 22b", "av": "Free", "version": "mistral-small:22b", "category": "Language Model", "rating": 4},
        {"name": "Mistral small 24b", "av": "Free", "version": "mistral-small:24b", "category": "Language Model", "rating": 4},
        {"name": "Dolphin mistral 7b", "av": "Free", "version": "dolphin-mistral:7b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 8b", "av": "Free", "version": "dolphin-llama3:8b", "category": "Language Model", "rating": 3},
        {"name": "Dolphin Llama 3 70b", "av": "Free", "version": "dolphin-llama3:70b", "category": "Language Model", "rating": 3},
        {"name": "Command r 35b", "av": "Free", "version": "command-r", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 3b", "av": "Free", "version": "orca-mini:3b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 7b", "av": "Free", "version": "orca-mini:7b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 13b", "av": "Free", "version": "orca-mini:13b", "category": "Language Model", "rating": 3},
        {"name": "Orca mini 70b", "av": "Free", "version": "orca-mini:70b", "category": "Language Model", "rating": 3},
        {"name": "yi 6b", "av": "Free", "version": "yi:6b", "category": "Language Model", "rating": 3},
        {"name": "yi 9b", "av": "Free", "version": "yi:69b", "category": "Language Model", "rating": 3},
        {"name": "yi 34b", "av": "Free", "version": "yi:34b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 1.5b", "av": "Free", "version": "qwen2-math:1.5b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 7b", "av": "Free", "version": "qwen2-math:7b", "category": "Language Model", "rating": 3},
        {"name": "Qwen 2 math 72b", "av": "Free", "version": "qwen2-math:72b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 3b", "av": "Free", "version": "hermes3:3b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 8b", "av": "Free", "version": "hermes3:8b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 70b", "av": "Free", "version": "hermes3:70b", "category": "Language Model", "rating": 3},
        {"name": "Hermes 3 405b", "av": "Free", "version": "hermes3:405b", "category": "Language Model", "rating": 3},
        {"name": "Phi 3.5 3.8b", "av": "Free", "version": "phi3.5", "category": "Language Model", "rating": 4},
        {"name": "Smollm 125m", "av": "Free", "version": "smollm:135m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 360m", "av": "Free", "version": "smollm:360m", "category": "Language Model", "rating": 3},
        {"name": "Smollm 1.7b", "av": "Free", "version": "smollm:1.7b", "category": "Language Model", "rating": 3},
        {"name": "Nuextract 3.8b", "av": "Free", "version": "nuextract", "category": "Language Model", "rating": 3},
        {"name": "Firefunction v2 70b", "av": "Free", "version": "firefunction-v2", "category": "Language Model", "rating": 3},
        {"name": "Llama 3 groq tool use 8b", "av": "Free", "version": "llama3-groq-tool-use:8b", "category": "Language Model",
         "rating": 3},
        {"name": "Llama 3 groq tool use 70b", "av": "Free", "version": "llama3-groq-tool-use:70b", "category": "Language Model",
         "rating": 3},
        {"name": "Mathstral 7b", "av": "Free", "version": "mathstral", "category": "Language Model", "rating": 3},
        {"name": "Codegee x4 9b", "av": "Free", "version": "codegeex4", "category": "Language Model", "rating": 3},
        {"name": "glm4 9b", "av": "Free", "version": "glm4", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1m", "av": "Free", "version": "internlm2:1m", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 1.8b", "av": "Free", "version": "internlm2:1.8b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 7b", "av": "Free", "version": "internlm2:7b", "category": "Language Model", "rating": 3},
        {"name": "Internlm 2 20b", "av": "Free", "version": "internlm2:20b", "category": "Language Model", "rating": 3},
        {"name": "Codestral 22b", "av": "Free", "version": "codestral", "category": "Language Model", "rating": 4},
        {"name": "Granite 3.2 Vision 2b", "av": "Free", "version": "granite3.2-vision", "category": "Vision Tool", "rating": 3},
        {"name": "Moon Dream 1.8b", "av": "Free", "version": "moondream", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA Llama3 8b", "av": "Free", "version": "llava-llama3", "category": "Vision Tool", "rating": 3},
        {"name": "LlaVA Phi3 3.8b", "av": "Free", "version": "llava-phi3", "category": "Vision Tool", "rating": 3},
        {"name": "Bak LlaVA 7b", "av": "Free", "version": "bakllava", "category": "Vision Tool", "rating": 3},
        {"name": "DBRX 132b", "av": "Free", "version": "dbrx", "category": "Language Model", "rating": 4},
        {"name": "notus 7b", "av": "Free", "version": "notus", "category": "Language Model", "rating": 4},
        {"name": "Tulu 3 8b", "av": "Free", "version": "tulu3:8b", "category": "Language Model", "rating": 4},
        {"name": "Tulu 3 70b", "av": "Free", "version": "tulu3:70b", "category": "Language Model", "rating": 4},
        {"name": "Notux 8x7b", "av": "Free", "version": "notux", "category": "Language Model", "rating": 4},
        {"name": "megadolphin 120b", "av": "Free", "version": "megadolphin", "category": "Language Model", "rating": 4},
        {"name": "Wizard Vicuna 13b", "av": "Free", "version": "wizard-vicuna", "category": "Language Model", "rating": 4},
        {"name": "Duckdb NSQL 7b", "av": "Free", "version": "duckdb-nsql", "category": "Language Model", "rating": 4}
    ]

def main():
    models = fetch_models()
    table_data = []

    # Table headers
    headers = ["Name", "Available", "Version", "Category", "Rating", "Status"]

    for model in models:
        installed = check_model_with_ollama(model["version"])
        status = f"{green}Installed{reset}" if installed else f"{red}Not Installed{reset}"

        table_data.append([
            model["name"],
            model["av"],
            model["version"],
            model["category"],
            model["rating"],
            status
        ])

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("")

if __name__ == "__main__":
    main()
