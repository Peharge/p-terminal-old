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

from flask import Flask, render_template, request, jsonify, send_from_directory, session
import ollama
import os
from PIL import Image
from pix2tex.cli import LatexOCR
import base64
import io
import markdown
import re
import sys
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
import altair as alt
import datetime
import PyPDF2
import docx
import json
from werkzeug.utils import secure_filename

def extract_text_from_file(filepath):
    file_ext = filepath.rsplit('.', 1)[-1].lower()
    text = ""

    try:
        if file_ext == "txt":
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        elif file_ext == "pdf":
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        elif file_ext == "docx":
            doc = docx.Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
        elif file_ext == "py":
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        elif file_ext == "html":
            with open(filepath, "r", encoding="utf-8") as f:
                text = markdown.markdown(f.read())
        elif file_ext == "md":
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")

    return text

app = Flask(__name__)

# Setze einen geheimen Schlüssel für die Session
app.secret_key = os.urandom(24)  # Generiert einen zufälligen Schlüssel mit 24 Bytes

# Verzeichnisse konfigurieren
UPLOAD_FOLDER_LATEX = 'mavis-uploads_latex'
os.makedirs(UPLOAD_FOLDER_LATEX, exist_ok=True)
app.config['UPLOAD_FOLDER_LATEX'] = UPLOAD_FOLDER_LATEX
app.config['UPLOAD_URL'] = '/mavis-uploads/'
DEFAULT_IMAGE_PATH = r""

UPLOAD_FOLDER = 'mavis-uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
TEXT_EXTENSIONS = {'txt', 'pdf', 'docx', 'py', 'html', 'md'}

# Pfad zur JSON-Datei korrekt zusammensetzen
file_path = os.path.join(os.path.expanduser("~"), "p-terminal", "pp-term", "model-mavis-4.json")

# Datei öffnen und JSON laden
try:
    with open(file_path, 'r') as file:
        model_config = json.load(file)
    print("The JSON file was loaded successfully.")
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON file: {e}")

# Extrahiere die Modelle aus der Konfiguration
model1 = model_config['mavis-4']['model1']
model2 = model_config['mavis-4']['model2']
model3 = model_config['mavis-4']['model3']

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_text_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in TEXT_EXTENSIONS

# Modell für LaTeX-OCR initialisieren
model = LatexOCR()

def execute_python_code(md_content):

    import pandas as pd
    import numpy as np
    import sympy as sp
    import dash
    from dash import Dash, html, dcc, callback, Output, Input
    import math
    from IPython.display import display
    import os
    import datetime
    from bokeh.plotting import figure
    from mayavi import mlab
    from manim import Scene, Square, Create, Mobject

    # import scipy as sp (Problem mit sp)

    # ---für Physik/Chemie/Biologie(Medizin)/Erdkunde/Wirtschaft---

    # from astropy.coordinates import SkyCoord
    # import astropy.units as u
    # import astropy
    # import QuantLib as ql
    # import openmdao.api as om
    # import pybullet as p
    # import monai
    # import fenics (soon)
    # import pydy
    # import pycalculix
    # import solid
    # import pyomo.environ as pyo
    # from gekko import GEKKO
    # import casadi as ca
    # import control as ctrl
    # import rospy (soon)
    # import pybullet as p (soon)
    # import h2o
    # import pint
    # import CoolProp.CoolProp as CP
    # import pythermo
    # import geopandas as gpd
    # import Bio
    # import cv2
    # import SimpleITK as sitk
    # from nilearn import plotting
    # import deepchem
    # import pymedtermino
    # from lifelines import KaplanMeierFitter
    # from rdkit import Chem
    # from ase import Atoms
    # from chempy import Substance
    # from shapely.geometry import Point
    # import fiona
    # import cartopy.crs as ccrs
    # import statsmodels.api as sm
    # import yfinance as yf

    # import PySpice
    # import networkx as nx
    # from schematics.models import Model
    # import schemdraw
    # import ipywidgets as widgets
    # import pybullet as pb
    # import vtk
    # from diagrams import Diagram
    # import graphviz

    # ---ultimate für Deep Learning etc.---

    # Importiere die wichtigsten Komponenten von PyTorch für Deep Learning (sehr mächtig)

    # from torch import *
    # from torch.nn import *
    # from torch.optim import *
    # from torch.autograd import *
    # from torch.utils.data import *

    # Importiere die wichtigsten Komponenten von TensorFlow für Deep Learning (sehr mächtig)

    # import tensorflow as tf
    # from tensorflow import keras
    # from tensorflow.keras import layers, models, optimizers
    # from tensorflow.data import Dataset

    # Importiere die wichtigsten Komponenten von Scikit-Learn für Deep Learning (sehr mächtig)

    # import sklearn as skl

    # Importiere die wichtigsten Komponenten von Transformers für Deep Learning (sehr mächtig)

    # from transformers import pipeline

    # Sucht nach Python-Code im Markdown-Inhalt, führt ihn aus und fügt die Ausgaben (Text oder Bild) zum Markdown hinzu.
    # Unterstützt Matplotlib, Seaborn, Plotly und Altair.

    code_pattern = re.compile(r"```python(.*?)```", re.DOTALL)
    matches = code_pattern.findall(md_content)

    # Falls kein Code gefunden wird, gib einen leeren String zurück
    if not matches:
        return "---"

    # Verzeichnis für gespeicherte Bilder
    image_dir = os.path.join(os.path.expanduser("~"), "p-terminal", "pp-term", "static", "image")
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for match in matches:
        code = match.strip()
        try:
            # Umleiten der Ausgaben in einen String-Buffer
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            # Ersetze plt.show() durch Speichern der Grafik
            code = code.replace("plt.show()", "# plt.show() ersetzt durch Speichern der Grafik")

            # Kontext für die Code-Ausführung erstellen
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)

            # Erhalte alle Ausgaben, die während der Code-Ausführung erzeugt wurden
            output_text = sys.stdout.getvalue()
            # Wiederherstellen der normalen Ausgabe
            sys.stdout = old_stdout

            img_html = ""

            # Verarbeitung von Matplotlib- oder Seaborn-Grafiken
            fig = plt.gcf()  # Seaborn nutzt Matplotlib für die Visualisierung
            if fig and fig.get_axes():  # Überprüfen, ob eine Grafik vorhanden ist
                # Generiere einen eindeutigen Dateinamen
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                image_filename = f"fig_matplotlib_{timestamp}.png"
                image_path = os.path.join(image_dir, image_filename)
                # Diagramm speichern
                plt.savefig(image_path, format='png', bbox_inches='tight')
                plt.close(fig)  # Grafik schließen, um Speicher freizugeben
                # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                image_url = f"/static/image/{image_filename}"

                # Füge das Bild in den HTML-Output ein
                img_html += f'<img class="img-out" src="{image_url}" alt="Generated Matplotlib Plot" />'

            # Verarbeitung von Plotly-Grafiken
            for var_name, var_value in exec_locals.items():
                if hasattr(var_value, "write_html") and callable(var_value.write_html):
                    # Prüfen, ob die Variable eine Plotly-Figur ist
                    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                    html_filename = f"fig_plotly_{timestamp}.html"  # HTML-Datei
                    html_path = os.path.join(image_dir, html_filename)

                    # Diagramm als interaktive HTML-Datei speichern
                    var_value.write_html(html_path)

                    # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                    image_url = f"/static/image/{html_filename}"

                    # Füge das HTML-Dokument in den HTML-Output ein
                    img_html += f'<iframe src="{image_url}" width="900px" height="550px" frameborder="0"></iframe>'
                    break  # Nur das erste Plotly-Diagramm verarbeiten

            # Verarbeitung von Bokeh-Grafiken
            for var_name, var_value in exec_locals.items():
                if isinstance(var_value, figure):  # Richtige Prüfung auf Bokeh-Figur
                    try:
                        # Generiere einzigartigen Dateinamen mit Zeitstempel
                        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        html_filename = f"fig_bokeh_{timestamp}.html"
                        html_path = os.path.join(image_dir, html_filename)

                        # Diagramm als interaktive HTML-Datei speichern
                        var_value.output_backend = "webgl"  # Performance-Optimierung
                        var_value.output_backend = "canvas"  # Alternativ für bessere Kompatibilität
                        var_value.write_html(html_path)

                        # Relativer Pfad für HTML (z.B. für Flask-Static-Serving)
                        image_url = f"/static/image/{html_filename}"

                        # Füge das HTML-Dokument in den HTML-Output ein
                        img_html += f'<iframe src="{image_url}" width="900px" height="550px" frameborder="0"></iframe>'
                        break  # Nur das erste Bokeh-Diagramm verarbeiten

                    except Exception as e:
                        print(f"Error saving the bokeh graphic: {e}")

            for var_name, var_value in exec_locals.items():
                if hasattr(var_value, "scene") and callable(getattr(var_value.scene, "save", None)):
                    try:
                        # Prüfen, ob die Variable eine Mayavi-Figur ist
                        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        img_filename = f"fig_mayavi_{timestamp}.png"  # Bild-Datei
                        img_path = os.path.join(image_dir, img_filename)

                        # Diagramm als Bild speichern
                        mlab.savefig(img_path, figure=var_value)
                        mlab.close(var_value)  # Schließe die Szene nach dem Speichern

                        # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                        image_url = f"/static/image/{img_filename}"

                        # Füge das Bild in den HTML-Output ein
                        img_html += f'<img src="{image_url}" width="900px" height="550px" />'
                        break  # Nur das erste Mayavi-Diagramm verarbeiten!

                    except Exception as e:
                        print(f"Error saving the mayavi graphic: {e}")

            for var_name, var_value in exec_locals.items():
                if isinstance(var_value, Mobject):  # Prüfen, ob es ein Manim-Mobject ist
                    try:
                        # Timestamp für die Dateinamen
                        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        image_filename = f"fig_manim_{timestamp}.png"
                        image_path = os.path.join(image_dir, image_filename)

                        # Sicherstellen, dass das Verzeichnis existiert
                        os.makedirs(image_dir, exist_ok=True)

                        # Szene erstellen und Mobject rendern
                        scene = Scene()
                        scene.add(var_value)
                        scene.wait(1)  # Kurzes Warten für das Rendern

                        # Kamera-Einstellungen für hohe Auflösung
                        scene.renderer.camera.pixel_height = 1080
                        scene.renderer.camera.pixel_width = 1920

                        # Bild speichern
                        scene.renderer.save_image(image_path)

                        # Relativer Pfad für HTML (basierend auf Flask-Static-Serving)
                        image_url = f"/static/image/{image_filename}"

                        # Bild in den HTML-Output einfügen
                        img_html += f'<img src="{image_url}" width="900px" height="550px">'

                        break  # Nur das erste Manim-Objekt verarbeiten
                    except Exception as e:
                        print(f"Error rendering the object '{var_name}': {e}")
                        continue  # Weiter mit dem nächsten Objekt, falls ein Fehler auftritt

            for var_name, var_value in exec_locals.items():
                if isinstance(var_value, alt.Chart):  # Prüfen, ob es sich um ein Altair-Diagramm handelt
                    try:
                        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                        image_filename = f"fig_altair_{timestamp}.svg"
                        image_path = os.path.join(image_dir, image_filename)

                        # Versuchen, die SVG-Datei zu speichern
                        var_value.save(image_path, format="svg")

                        # Relativer Pfad für die HTML-Ausgabe
                        image_url = f"/static/image/{image_filename}"
                        img_html += f'<img class="img-out" src="{image_url}" width="600px" height="400px" />'

                    except Exception as e:
                        print(f"Error saving Altair diagram: {e}")
                        # Alternativ: Als PNG speichern
                        try:
                            png_filename = f"fig_altair_{timestamp}.png"
                            png_path = os.path.join(image_dir, png_filename)
                            var_value.save(png_path, format="png")
                            png_url = f"/static/image/{png_filename}"
                            img_html += f'<img class="img-out" src="{png_url}" width="600px" height="400px" />'
                        except Exception as png_error:
                            print(f"Error when falling back to PNG: {png_error}")
                            img_html += f"<div class='error'>Fehler: Altair-Diagramm konnte weder als SVG noch als PNG gespeichert werden.</div>"

            # Ersetze den Codeblock im Markdown durch den Ausgabeblock (Text oder Bild)
            result = f"<div class='code-output-box'>{output_text}{img_html}</div>"

        except Exception as e:
            # Fehler beim Ausführen des Codes
            error_msg = f"{e}"
            error_html = f"<div class='code-output-box error'>Execution Error: {error_msg}</div>"
            result = error_html

        session['result'] = result
        return result

@app.route('/')
def index():
    return render_template('index-mavis-4-3.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '').strip()
    file = request.files.get('image', None)

    if file and file.filename and allowed_text_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        extracted_text = extract_text_from_file(filepath)
        user_message += "\n" + extracted_text if extracted_text else ""

        try:
            response = ollama.chat(
                model=model1,
                messages=[{
                    'role': 'user',
                    'content': user_message
                }]
            )

            response_content = response['message']['content']
            response_content_code = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': DEFAULT_IMAGE_PATH,
                'code': response_content_code
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    if file and file.filename and allowed_file(file.filename):
        # Verarbeite die Nachricht mit dem hochgeladenen Bild
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            response = ollama.chat(
                model=model2,
                messages=[{
                    'role': 'user',
                    'content': user_message,
                    'images': [filepath]
                }]
            )

            response_content = response['message']['content']
            response_content_code = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            # Hier wird das 'md_content' mit der Antwort und dem Code (als 'code') gesendet
            return jsonify({
                'response': wrapped_html_content,
                'image_url': app.config['UPLOAD_URL'] + filename,
                'code': response_content_code
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    else:
        # Verarbeite die Nachricht ohne Bild, benutze das Standardbild
        try:
            response = ollama.chat(
                model=model1,
                messages=[{
                    'role': 'user',
                    'content': user_message
                }]
            )

            response_content = response['message']['content']
            response_content_code = execute_python_code(response_content)
            html_content = markdown.markdown(response_content, extensions=['extra'], output_format='html5')
            wrapped_html_content = f"<div class='response-box'>{html_content}</div>"

            return jsonify({
                'response': wrapped_html_content,
                'image_url': DEFAULT_IMAGE_PATH,
                'code': response_content_code
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        image_path_latex = os.path.join(app.config['UPLOAD_FOLDER_LATEX'], file.filename)
        file.save(image_path_latex)
        img_latex = Image.open(image_path_latex)
    elif 'image' in request.json:
        image_latex_data = request.json['image'].split(",")[1]
        image_latex_bytes = base64.b64decode(image_latex_data)
        img_latex = Image.open(io.BytesIO(image_latex_bytes))
    else:
        return jsonify({'error': 'No image data provided'}), 400

    try:
        latex_code = model(img_latex)
        return jsonify({'latex': latex_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Stelle sicher, dass pygame korrekt initialisiert wird
def init_pygame():
    import pygame

    try:
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        print("Pygame mixer initialized.")
    except pygame.error as e:
        print(f"Error initializing Pygame: {e}")

# Funktion zur Audioaufnahme mit pyaudio und webrtcvad
def record_audio(filename="input.wav", samplerate=16000, frame_duration_ms=30, vad_mode=1):

    import pyaudio
    import wave
    import webrtcvad

    # Initialisierung von VAD (Voice Activity Detection)
    vad = webrtcvad.Vad(vad_mode)  # VAD-Mode kann von 0 bis 3 gehen, wobei 3 am empfindlichsten ist

    # pyaudio Setup
    p = pyaudio.PyAudio()

    # Audio-Stream öffnen
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=samplerate,
                    input=True,
                    frames_per_buffer=int(samplerate * frame_duration_ms / 1000))

    print("Recording started...")

    frames = []
    silence_duration = 0  # Variable, um die Stille zu überwachen

    while True:
        # Audio-Frame aufnehmen
        audio_frame = stream.read(int(samplerate * frame_duration_ms / 1000))
        frames.append(audio_frame)

        # Überprüfen, ob Sprache erkannt wird
        if vad.is_speech(audio_frame, samplerate):
            silence_duration = 0  # Zurücksetzen des Schweigens, wenn Sprache erkannt wird
        else:
            silence_duration += frame_duration_ms / 1000  # Erhöhe die Stille-Zeit

        # Wenn keine Sprache für 1 Sekunde (1000 ms) erkannt wurde, Aufnahme beenden
        if silence_duration >= 1:
            print("No speech detected for 1 second, stopping recording.")
            break

    # Aufnahme beenden
    stream.stop_stream()
    stream.close()
    p.terminate()

    # WAV-Datei speichern
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))

    print("Recording finished.")
    return filename

# Funktion zur Transkription der Audiodatei
def transcribe_audio(file_path):

    import whisper

    model = whisper.load_model("small")

    # Load audio and pad/trim it to fit the model
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Store the transcribed text in 'message'
    message = result.text
    print(f"{message}")
    return message

# Sicherstellen, dass das Verzeichnis existiert
if not os.path.exists("static"):
    os.makedirs("static")

# Funktion für die TTS-Ausgabe (Text-to-Speech)
def text_to_speech(text):

    import pygame
    from TTS.api import TTS
    import time

    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")

    # Dynamischer Dateiname für jede Ausgabe
    output_file = f"static/output_{int(time.time())}.wav"

    try:
        # Speichern der Audio-Datei
        print("Saving audio file...")
        tts.tts_to_file(text=text, file_path=output_file)

        # Überprüfen, ob die Datei gespeichert wurde
        if os.path.exists(output_file):
            print(f"File saved: {output_file}")

            # Lade die Audiodatei
            pygame.mixer.music.load(output_file)

            # Spiele die Audiodatei ab
            print("Play the file...")
            pygame.mixer.music.play()

            # Warte, bis die Wiedergabe beendet ist
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            print("Audio played.")
        else:
            print(f"The file {output_file} does not exist.")
    except PermissionError as e:
        print(f"Error writing file: {e}")
    except pygame.error as e:
        print(f"Error playing file: {e}")
    except Exception as e:
        print(f"Error playing file: {e}")
    finally:
        pygame.mixer.quit()

    return output_file

# Funktion zur Kommunikation mit Ollama (für die Chat-Nachricht)
def chat_response(message):
    try:
        response = ollama.chat(
            model=model3,
            messages=[{
                'role': 'user',
                'content': message
            }]
        )
        print(f"{response['message']['content']}")
        return response['message']['content']
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return "There was a problem processing the request."

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        # Initialisiere pygame mixer zu Beginn jeder Anfrage
        init_pygame()

        # Audio aufnehmen
        file_path = record_audio()

        # Transkribieren
        message = transcribe_audio(file_path)

        # Anfrage an Ollama senden
        response_text = chat_response(message)

        # TTS-Ausgabe (Text-to-Speech) und Abspielen der Audiodatei
        text_to_speech(response_text)

        # Rückgabe der Antwort als JSON
        return jsonify({"response": response_text})

    except Exception as e:
        # Rückgabe der Fehlerdetails im JSON-Format
        print(f"Error processing request: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
