@echo off

REM Englisch Peharge: This source code is released under the MIT License.
REM
REM Usage Rights:
REM The source code may be copied, modified, and adapted to individual requirements.
REM Users are permitted to use this code in their own projects, both for private and commercial purposes.
REM However, it is recommended to modify the code only if you have sufficient programming knowledge,
REM as changes could cause unintended errors or security risks.
REM
REM Dependencies and Additional Frameworks:
REM The code relies on the use of various frameworks and executes additional files.
REM Some of these files may automatically install further dependencies required for functionality.
REM It is strongly recommended to perform installation and configuration in an isolated environment
REM (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
REM
REM Disclaimer:
REM Use of the code is entirely at your own risk.
REM Peharge assumes no liability for damages, data loss, system errors, or other issues
REM that may arise directly or indirectly from the use, modification, or redistribution of the code.
REM
REM Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

REM Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
REM
REM Nutzungsrechte:
REM Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
REM Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
REM Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
REM da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
REM
REM Abhängigkeiten und zusätzliche Frameworks:
REM Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
REM Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
REM Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
REM um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
REM
REM Haftungsausschluss:
REM Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
REM Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
REM die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
REM
REM Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

REM Français Peharge: Ce code source est publié sous la licence MIT.
REM
REM Droits d'utilisation:
REM Le code source peut être copié, édité et adapté aux besoins individuels.
REM Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
REM Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
REM car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
REM
REM Dépendances et frameworks supplémentaires:
REM Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
REM Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
REM Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
REM pour éviter d'éventuels conflits avec les installations de logiciels existantes.
REM
REM Clause de non-responsabilité:
REM L'utilisation du code est entièrement à vos propres risques.
REM Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
REM pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
REM
REM Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

:: -----------------------------------------------------------------------------
:: Batch-Skript: Installiert ggf. Visual Studio C++ Build Tools und kompiliert
::               und startet dann das Programm p-term.cpp
:: -----------------------------------------------------------------------------
setlocal enableextensions enabledelayedexpansion

REM === 1. Visual Studio Install-Skript ausführen ===
set "INSTALL_SCRIPT=%USERPROFILE%\p-terminal\p-term\install\cpp\install-vs.py"
if not exist "%INSTALL_SCRIPT%" (
    echo Fehler: Installationsskript nicht gefunden: %INSTALL_SCRIPT%
    goto :error
)
echo.
echo *** Schritt 1: Installationsskript fuer VS Build Tools ausfuehren ***
python "%INSTALL_SCRIPT%"
if errorlevel 1 (
    echo Fehler: Installationsskript schlug fehl.
    goto :error
)
echo.

REM === 2. Visual Studio Umgebungs-Init (vcvarsall.bat) ===
echo *** Schritt 2: Visual Studio-Umgebung initialisieren ***

REM Default-Installation-Verzeichnis setzen (fallback)
set "VSINSTALL=%ProgramFiles%\Microsoft Visual Studio\2022\Community"

REM Versuche VS-Installation via vswhere.exe zu finden und überschreibe VSINSTALL
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "%VSWHERE%" (
    for /f "usebackq tokens=* delims=" %%i in (`"%VSWHERE%" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath`) do (
        set "VSINSTALL=%%i"
    )
) else (
    echo vswhere.exe nicht gefunden, verwende Standard: %VSINSTALL%
)

set "VCVARSALL=%VSINSTALL%\VC\Auxiliary\Build\vcvarsall.bat"
if not exist "%VCVARSALL%" (
    echo Fehler: vcvarsall.bat nicht gefunden unter %VCVARSALL%
    goto :error
)
call "%VCVARSALL%" x64
if errorlevel 1 (
    echo Fehler: VS-Umgebung konnte nicht initialisiert werden.
    goto :error
)
echo.

REM === 3. C++-Datei kompilieren und ausfuehren ===
set "SRC=%USERPROFILE%\p-terminal\p-term\p-term.cpp"
set "EXE=%USERPROFILE%\p-terminal\p-term\p-term.exe"
if not exist "%SRC%" (
    echo Fehler: Quelldatei nicht gefunden: %SRC%
    goto :error
)
echo *** Schritt 3: Kompilieren von %SRC% ***
cl.exe /EHsc "%SRC%" /Fe"%EXE%"
if errorlevel 1 (
    echo Fehler: Kompilierung schlug fehl.
    goto :error
)
echo.
echo *** Ausfuehren von %EXE% ***
"%EXE%"

goto :end

:error
echo.
echo *** Skript wurde mit Fehler beendet ***
pause
exit /b 1

:end
echo.
echo *** Fertig ***
endlocal
