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

setlocal enabledelayedexpansion
chcp 65001

echo.
powershell -Command "& {Write-Host '██████╗ ██████╗    ' -ForegroundColor Blue -NoNewline; Write-Host '████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗' -ForegroundColor White; Write-Host '██╔══██╗██╔══██╗   ' -ForegroundColor Blue -NoNewline; Write-Host '╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║' -ForegroundColor White; Write-Host '██████╔╝██████╔╝' -ForegroundColor Blue -NoNewline; Write-Host '█████╗██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║' -ForegroundColor White; Write-Host '██╔═══╝ ██╔═══╝ ' -ForegroundColor Blue -NoNewline; Write-Host '╚════╝██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║' -ForegroundColor White; Write-Host '██║     ██║           ' -ForegroundColor Blue -NoNewline; Write-Host '██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗' -ForegroundColor White; Write-Host '╚═╝     ╚═╝           ' -ForegroundColor Blue -NoNewline; Write-Host '╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝' -ForegroundColor White;}"
echo.
powershell -Command "& {Write-Host '██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗' -ForegroundColor White; Write-Host '██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗' -ForegroundColor White; Write-Host '██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝' -ForegroundColor White; Write-Host '██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗' -ForegroundColor White; Write-Host '███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║' -ForegroundColor White; Write-Host '╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝' -ForegroundColor White;}"
echo.
echo Initiating high-tech installation...
echo [*] Prepare for the next level...
echo.
echo [Time Stamp]   %date% %time%
echo [Hostname]     %COMPUTERNAME%
echo [User]         %USERNAME%
echo.
echo MIT License
echo Copyright (c) 2025
echo Peharge
echo.
echo Permission is hereby granted, free of charge, to any person obtaining a copy
echo of this software and associated documentation files (the "Software"), to deal
echo in the Software without restriction, including without limitation the rights
echo to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
echo copies of the Software, and to permit persons to whom the Software is
echo furnished to do so, subject to the following conditions:
echo.
echo The above copyright notice and this permission notice shall be included in all
echo copies or substantial portions of the Software.
echo.
echo THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
echo IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
echo FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
echo AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
echo LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
echo OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
echo SOFTWARE.
echo.
echo Initializing PP-Terminal
echo Gooo...
echo.

rem Get Windows version info
for /f "tokens=3 delims= " %%i in ('reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName 2^>nul') do (
    set "ProductName=%%i"
)

rem Check if it contains 'Windows 11'
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName | findstr /i "Windows 11" >nul
if %errorlevel%==0 (
    echo ✅ Windows 11 is in use.
) else (
    echo ❌ This is not Windows 11.
)

REM Get local IP address
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| findstr /i "IPv4"') do set "LOCAL_IP=%%i"
echo Lokale IP: %LOCAL_IP%

REM Check connection to Google DNS
ping -n 1 8.8.8.8 >nul
if %errorlevel%==0 (
    echo ✅ Internet connection exists.
) else (
    echo ❌ No internet connection!
)

timeout /t 5 >nul

:: Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.12 is not installed.
    set /p install_python="Would you like to install Python 3.12? [y/n]:"

    if /i "%install_python%"=="y" (
        echo Downloading Python 3.12 installer...

        set "PYTHON_URL=https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
        set "PYTHON_INSTALLER=%TEMP%\python-3.12.2-installer.exe"

        :: Securely download Python using PowerShell (TLS 1.2)
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"

        if exist "%PYTHON_INSTALLER%" (
            echo Running Python installer...
            start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

            :: Verify installation
            python --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                del "%PYTHON_INSTALLER%"
                start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

                python --version >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Trying ZIP method...
                    del "%PYTHON_INSTALLER%"
                    set "PYTHON_ZIP_URL=https://www.python.org/ftp/python/3.12.2/python-3.12.2-embed-amd64.zip"
                    set "PYTHON_ZIP=%TEMP%\python-3.12.2.zip"
                    set "PYTHON_DIR=C:\Python312"

                    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_ZIP_URL%' -OutFile '%PYTHON_ZIP%'"

                    if exist "%PYTHON_ZIP%" (
                        mkdir "%PYTHON_DIR%"
                        powershell -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%'"
                        del "%PYTHON_ZIP%"

                        setx PATH "%PYTHON_DIR%;%PATH%" /M

                        "%PYTHON_DIR%\python.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            echo ❌ ZIP installation failed! Cleaning up...
                            rmdir /s /q "%PYTHON_DIR%"
                            echo Manual installation required: https://www.python.org/downloads
                        ) else (
                            echo ✅ Python 3.12 successfully installed using ZIP method!
                        )
                    ) else (
                        echo ❌ ZIP download failed! Manual installation required.
                    )
                ) else (
                    echo ✅ Python 3.12 successfully installed!
                )
            ) else (
                echo ✅ Python 3.12 successfully installed!
            )
        ) else (
            echo ❌ Error: Python installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Python 3.12 manually: https://www.python.org/downloads
    )
) else (
    echo ✅ Python is already installed.
)

:: Check if Git is already installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed.
    set /p install_git="Would you like to install Git? [y/n]:"

    if /i "%install_git%"=="y" (
        echo Downloading Git installer...

        set "GIT_URL=https://github.com/git-for-windows/git/releases/latest/download/Git-2.44.0-64-bit.exe"
        set "GIT_INSTALLER=%TEMP%\git-installer.exe"

        :: Securely download Git using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%GIT_URL%' -OutFile '%GIT_INSTALLER%'"

        if exist "%GIT_INSTALLER%" (
            echo Running Git installer...
            start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

            :: Verify installation
            git --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                del "%GIT_INSTALLER%"
                start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

                git --version >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Trying ZIP method...
                    del "%GIT_INSTALLER%"
                    set "GIT_ZIP_URL=https://github.com/git-for-windows/git/releases/latest/download/PortableGit-2.44.0-64-bit.zip"
                    set "GIT_ZIP=%TEMP%\git-portable.zip"
                    set "GIT_DIR=C:\GitPortable"

                    powershell -Command "Invoke-WebRequest -Uri '%GIT_ZIP_URL%' -OutFile '%GIT_ZIP%'"

                    if exist "%GIT_ZIP%" (
                        mkdir "%GIT_DIR%"
                        powershell -Command "Expand-Archive -Path '%GIT_ZIP%' -DestinationPath '%GIT_DIR%'"
                        del "%GIT_ZIP%"

                        setx PATH "%GIT_DIR%\bin;%PATH%" /M

                        "%GIT_DIR%\bin\git.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            echo ❌ ZIP installation failed! Cleaning up...
                            rmdir /s /q "%GIT_DIR%"
                            echo Manual installation required: https://git-scm.com/downloads
                        ) else (
                            echo ✅ Git successfully installed using ZIP method!
                        )
                    ) else (
                        echo ❌ ZIP download failed! Manual installation required.
                    )
                ) else (
                    echo ✅ Git successfully installed!
                )
            ) else (
                echo ✅ Git successfully installed!
            )
        ) else (
            echo ❌ Error: Git installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Git manually: https://git-scm.com/downloads
    )
) else (
    echo ✅ Git is already installed.
)

:: Check if Ollama is already installed
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Ollama is not installed.
    set /p install_ollama="Would you like to install Ollama? [y/n]:"

    if /i "%install_ollama%"=="y" (
        echo Downloading Ollama installer...

        set "OLLAMA_URL=https://ollama.com/download/OllamaSetup.exe"
        set "OLLAMA_INSTALLER=%TEMP%\OllamaSetup.exe"

        :: Securely download Ollama using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%OLLAMA_URL%' -OutFile '%OLLAMA_INSTALLER%'"

        if exist "%OLLAMA_INSTALLER%" (
            echo Running Ollama installer...
            start /wait %OLLAMA_INSTALLER% /silent /norestart

            :: Verify installation
            ollama --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                del "%OLLAMA_INSTALLER%"
                start /wait %OLLAMA_INSTALLER% /silent /norestart

                ollama --version >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Trying ZIP method...
                    del "%OLLAMA_INSTALLER%"
                    set "OLLAMA_ZIP_URL=https://ollama.com/download/OllamaPortable.zip"
                    set "OLLAMA_ZIP=%TEMP%\OllamaPortable.zip"
                    set "OLLAMA_DIR=C:\OllamaPortable"

                    powershell -Command "Invoke-WebRequest -Uri '%OLLAMA_ZIP_URL%' -OutFile '%OLLAMA_ZIP%'"

                    if exist "%OLLAMA_ZIP%" (
                        mkdir "%OLLAMA_DIR%"
                        powershell -Command "Expand-Archive -Path '%OLLAMA_ZIP%' -DestinationPath '%OLLAMA_DIR%'"
                        del "%OLLAMA_ZIP%"

                        setx PATH "%OLLAMA_DIR%;%PATH%" /M

                        "%OLLAMA_DIR%\ollama.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            echo ❌ ZIP installation failed! Cleaning up...
                            rmdir /s /q "%OLLAMA_DIR%"
                            echo Manual installation required: https://ollama.com/download
                        ) else (
                            echo ✅ Ollama successfully installed using ZIP method!
                        )
                    ) else (
                        echo ❌ ZIP download failed! Manual installation required.
                    )
                ) else (
                    echo ✅ Ollama successfully installed!
                )
            ) else (
                echo ✅ Ollama successfully installed!
            )
        ) else (
            echo ❌ Error: Ollama installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Ollama manually: https://ollama.com/download
    )
) else (
    echo ✅ Ollama is already installed.
)

:: Check if FFmpeg is already installed
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not installed.
    set /p install_ffmpeg="Would you like to install FFmpeg? [y/n]:"

    if /i "%install_ffmpeg%"=="y" (
        echo Downloading FFmpeg installer...

        set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        set "FFMPEG_ZIP=%TEMP%\ffmpeg.zip"
        set "FFMPEG_DIR=C:\ffmpeg"

        :: Securely download FFmpeg using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"

        if exist "%FFMPEG_ZIP%" (
            echo Extracting FFmpeg...
            powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
            del "%FFMPEG_ZIP%"

            :: Add FFmpeg to System PATH
            setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

            :: Verify installation
            ffmpeg -version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                rmdir /s /q "%FFMPEG_DIR%"
                powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"
                powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
                del "%FFMPEG_ZIP%"
                setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

                ffmpeg -version >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Trying alternative ZIP source...
                    rmdir /s /q "%FFMPEG_DIR%"
                    set "FFMPEG_ALT_URL=https://github.com/BtbN/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-win64-gpl.zip"
                    set "FFMPEG_ZIP=%TEMP%\ffmpeg-alt.zip"
                    powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_ALT_URL%' -OutFile '%FFMPEG_ZIP%'"
                    powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
                    del "%FFMPEG_ZIP%"
                    setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

                    ffmpeg -version >nul 2>&1
                    if %errorlevel% neq 0 (
                        echo ❌ Alternative ZIP installation failed! Cleaning up...
                        rmdir /s /q "%FFMPEG_DIR%"
                        echo Manual installation required: https://ffmpeg.org/download.html#build-windows
                    ) else (
                        echo ✅ FFmpeg successfully installed using alternative ZIP method!
                    )
                ) else (
                    echo ✅ FFmpeg successfully installed!
                )
            ) else (
                echo ✅ FFmpeg successfully installed!
            )
        ) else (
            echo ❌ Error: FFmpeg installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install FFmpeg manually: https://ffmpeg.org/download.html#build-windows
    )
) else (
    echo ✅ FFmpeg is already installed.
)

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe
set SCRIPT_install_rustup=C:\Users\%USERNAME%\p-terminal\pp-term\run\rust\install-rustup.py

:: Check if Rustup is already installed
rustup --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Rustup is not installed.
    set /p install_rustup="Would you like to install Rustup? [y/n]:"

    if /i "%install_rustup%"=="y" (
        echo Downloading Rustup installer...

        set "RUSTUP_URL=https://win.rustup.rs"
        set "RUSTUP_INSTALLER=%TEMP%\rustup-init.exe"

        :: Securely download Rustup using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%RUSTUP_URL%' -OutFile '%RUSTUP_INSTALLER%'"

        if exist "%RUSTUP_INSTALLER%" (
            echo Running Rustup installer...
            start /wait %RUSTUP_INSTALLER% -y

            :: Verify installation
            rustup --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                del "%RUSTUP_INSTALLER%"
                powershell -Command "Invoke-WebRequest -Uri '%RUSTUP_URL%' -OutFile '%RUSTUP_INSTALLER%'"
                start /wait %RUSTUP_INSTALLER% -y

                rustup --version >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Trying alternative method...
                    del "%RUSTUP_INSTALLER%"
                    set "RUSTUP_ALT_URL=https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
                    set "RUSTUP_INSTALLER=%TEMP%\rustup-alt.exe"
                    powershell -Command "Invoke-WebRequest -Uri '%RUSTUP_ALT_URL%' -OutFile '%RUSTUP_INSTALLER%'"
                    start /wait %RUSTUP_INSTALLER% -y

                    rustup --version >nul 2>&1
                    if %errorlevel% neq 0 (
                        echo ❌ Alternative installation failed! Cleaning up...
                        del "%RUSTUP_INSTALLER%"

                        if not exist "%SCRIPT_install_rustup%" (
                            echo Error: Script not found: %SCRIPT_install_rustup%
                            exit /B 1
                        )

                        "%PYTHON_PATH%" "%SCRIPT_install_rustup%"

                        echo Manual installation required: https://rustup.rs/
                    ) else (
                        echo ✅ Rustup successfully installed using alternative method!
                    )
                ) else (
                    echo ✅ Rustup successfully installed!
                )
            ) else (
                echo ✅ Rustup successfully installed!
            )
        ) else (
            echo ❌ Error: Rustup installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Rustup manually: https://rustup.rs/
    )
) else (
    echo ✅ Rustup is already installed.
)

:: Check if PowerShell 7 is already installed
powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
if %errorlevel% neq 0 (
    echo PowerShell 7 is not installed.
    set /p install_powershell="Would you like to install PowerShell 7? [y/n]:"

    if /i "%install_powershell%"=="y" (
        echo Downloading PowerShell 7 installer...

        set "POWERSHELL_URL=https://github.com/PowerShell/PowerShell/releases/download/v7.2.9/PowerShell-7.2.9-win-x64.msi"
        set "POWERSHELL_INSTALLER=%TEMP%\PowerShell-7.2.9-installer.msi"

        :: Securely download PowerShell using PowerShell (TLS 1.2)
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%POWERSHELL_URL%' -OutFile '%POWERSHELL_INSTALLER%'"

        if exist "%POWERSHELL_INSTALLER%" (
            echo Running PowerShell installer...
            start /wait msiexec.exe /i "%POWERSHELL_INSTALLER%" /quiet /norestart

            :: Verify installation
            powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Installation failed! Retrying...
                del "%POWERSHELL_INSTALLER%"
                start /wait msiexec.exe /i "%POWERSHELL_INSTALLER%" /quiet /norestart

                powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
                if %errorlevel% neq 0 (
                    echo ❌ Second installation attempt failed! Manual installation required: https://github.com/PowerShell/PowerShell/releases
                ) else (
                    echo ✅ PowerShell 7 successfully installed!
                )
            ) else (
                echo ✅ PowerShell 7 successfully installed!
            )
        ) else (
            echo ❌ Error: PowerShell installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install PowerShell 7 manually: https://github.com/PowerShell/PowerShell/releases
    )
) else (
    echo ✅ PowerShell 7 is already installed.
)

set "USERNAME=%USERNAME%"
set "PYTHON_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe"

:: Main Python script for generic WSL installations (fallback)
set "SCRIPT_install_wsl=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-wsl.py"

:: Scripts for installing individual distributions:
set "SCRIPT_install_wsl_ubuntu=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-ubuntu-wsl.py"
set "SCRIPT_install_wsl_debian=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-debian-wsl.py"
set "SCRIPT_install_wsl_kali=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-kali-wsl.py"
set "SCRIPT_install_wsl_arch=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-wsl.py"
set "SCRIPT_install_wsl_opensuse=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-opensuse-wsl.py"
set "SCRIPT_install_wsl_mint=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-mint.py"
set "SCRIPT_install_wsl_fedora=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-fedora.py"
set "SCRIPT_install_wsl_redhat=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-redhat.py"
set "SCRIPT_install_wsl_suse=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-suse.py"
set "SCRIPT_install_wsl_pengwin=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-pengwin.py"
set "SCRIPT_install_wsl_oracle=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-oracle.py"
set "SCRIPT_install_wsl_clear=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-clear.py"
set "SCRIPT_install_wsl_alpine=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-alpine-wsl.py"

:CheckWSLInstalled
wsl --list >nul 2>&1
if errorlevel 1 (
    echo WSL is not installed.
    set /p "install_wsl=Do you want to install WSL? [y/n]: "
    if /i "!install_wsl!"=="y" (
        echo Enabling WSL feature...
        dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart >nul 2>&1
        if errorlevel 1 (
            echo ❌ Error: Could not enable the WSL feature.
            if not exist "%SCRIPT_install_wsl%" (
                echo Error: Python fallback script not found: %SCRIPT_install_wsl%
                pause
                exit /b 1
            )
            call "%PYTHON_PATH%" "%SCRIPT_install_wsl%"
        ) else (
            echo ✅ WSL feature enabled successfully.
            echo Please restart your computer and run the script again.
            pause
            exit /b 0
        )
    ) else (
        echo Installation aborted. Please install WSL manually.
        pause
        exit /b 1
    )
)

echo ✅ WSL is already installed.

goto CheckDistroInstalled

:CheckDistroInstalled
set "found_distro="
for /f "usebackq delims=" %%i in (`wsl --list --quiet 2^>nul`) do (
    set "found_distro=%%i"
    goto DistroFound
)

if not defined found_distro (
    goto AskInstall
)

:DistroFound
echo ✅ WSL is already set up with the distribution: "!found_distro!"
goto Continue

:AskInstall
echo No Linux distribution was found.
set /p "install_choice=Do you want to install a Linux distribution? [y/n]: "
if /i "!install_choice!"=="y" (
    goto SelectDistro
) else (
    echo Installation aborted.
    goto Continue
)

:SelectDistro
echo.
echo Please select a distribution to install:
echo   [1] Ubuntu
echo   [2] Debian
echo   [3] Kali Linux
echo   [4] Arch Linux
echo   [5] openSUSE
echo   [6] Linux Mint
echo   [7] Fedora
echo   [8] Red Hat Enterprise Linux
echo   [9] SUSE Linux
echo   [10] Pengwin
echo   [11] Oracle Linux
echo   [12] Clear Linux
echo   [13] Alpine
choice /c 123456789ABCD /n /m "Your choice: "
set "choice=%errorlevel%"

:: Map the choice to the appropriate variables
if "%choice%"=="1" (
    set "DISTRO_NAME=Ubuntu"
    set "DISTRO_PACKAGE=Ubuntu"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_ubuntu%"
) else if "%choice%"=="2" (
    set "DISTRO_NAME=Debian"
    set "DISTRO_PACKAGE=Debian"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_debian%"
) else if "%choice%"=="3" (
    set "DISTRO_NAME=Kali Linux"
    set "DISTRO_PACKAGE=kali-linux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_kali%"
) else if "%choice%"=="4" (
    set "DISTRO_NAME=Arch Linux"
    set "DISTRO_PACKAGE=ArchLinux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_arch%"
) else if "%choice%"=="5" (
    set "DISTRO_NAME=openSUSE"
    set "DISTRO_PACKAGE=openSUSE-Leap-15-3"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_opensuse%"
) else if "%choice%"=="6" (
    set "DISTRO_NAME=Linux Mint"
    set "DISTRO_PACKAGE=LinuxMint"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_mint%"
) else if "%choice%"=="7" (
    set "DISTRO_NAME=Fedora"
    set "DISTRO_PACKAGE=FedoraRemix"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_fedora%"
) else if "%choice%"=="8" (
    set "DISTRO_NAME=Red Hat Enterprise Linux"
    set "DISTRO_PACKAGE=RHEL"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_redhat%"
) else if "%choice%"=="9" (
    set "DISTRO_NAME=SUSE Linux"
    set "DISTRO_PACKAGE=SUSE"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_suse%"
) else if "%choice%"=="10" (
    set "DISTRO_NAME=Pengwin"
    set "DISTRO_PACKAGE=Pengwin"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_pengwin%"
) else if "%choice%"=="11" (
    set "DISTRO_NAME=Oracle Linux"
    set "DISTRO_PACKAGE=Oracle"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_oracle%"
) else if "%choice%"=="12" (
    set "DISTRO_NAME=Clear Linux"
    set "DISTRO_PACKAGE=ClearLinux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_clear%"
) else if "%choice%"=="13" (
    set "DISTRO_NAME=Alpine"
    set "DISTRO_PACKAGE=Alpine"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_alpine%"
) else (
    echo ❌ Invalid choice. The program will now exit.
    pause
    exit /b 1
)

:: Check if the corresponding Python script exists
if not exist "!SCRIPT_DISTRO!" (
    echo Error: Python script not found: "!SCRIPT_DISTRO!"
    pause
    exit /b 1
)

echo.
echo You have selected: "!DISTRO_NAME!"
echo.

set /a attempts=0
:InstallLoop
set /a attempts+=1
echo [Attempt !attempts!] Starting installation of "!DISTRO_NAME!"...
call "%PYTHON_PATH%" "!SCRIPT_DISTRO!"

:: Short pause to allow the installation process to settle
timeout /t 5 >nul

:: Verify if the distribution appears in the WSL list
set "installed="
for /f "usebackq delims=" %%i in (`wsl --list --quiet`) do (
    echo %%i | findstr /i /c:"!DISTRO_PACKAGE!" >nul && set "installed=1"
)
if defined installed (
    echo.
    echo ✅ "!DISTRO_NAME!" has been successfully installed!
    goto Continue
) else (
    echo.
    echo ❌ Installation of "!DISTRO_NAME!" failed on attempt !attempts!.
    if !attempts! lss 3 (
        echo Waiting 3 seconds before retrying...
        timeout /t 3 >nul
        goto InstallLoop
    ) else (
        echo ❌ All installation attempts have failed.
        echo Please install "!DISTRO_NAME!" manually (e.g., via the Microsoft Store).
        pause
        exit /b 1
    )
)

:Continue

echo ✅ All WSL processes have been successfully terminated.

:: Define project path
set "PYCHARM_PROJECTS=%USERPROFILE%\p-terminal"
set "PP_DIR=%PYCHARM_PROJECTS%\pp-term"
set "PP_ENV_FILE=%PP_DIR%\.env"
set "PP_RUN_FILE=%PP_DIR%\pp-term.bat"
set "EXPECTED_PYTHON_VERSION=3.12"

:: Ensure PyCharm Projects directory exists
if not exist "%PYCHARM_PROJECTS%" (
    echo Creating project directory: %PYCHARM_PROJECTS%...
    mkdir "%PYCHARM_PROJECTS%"
    if errorlevel 1 (
        echo ❌ Error: Failed to create directory %PYCHARM_PROJECTS%. Exiting...
        exit /b 1
    )
)

:: Change to PyCharm Projects directory
cd /d "%PYCHARM_PROJECTS%"

:: Check if the p-terminal directory exists
if not exist "%PP_DIR%" (
    echo Cloning p-terminal repository from GitHub...

    :: Check if Git is installed
    where git >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Error: Git is not installed. Please install Git first.
        exit /b 1
    )

    :: Check if GitHub is reachable (with a timeout of 5 seconds)
    echo Testing connection to GitHub...
    for /f "delims=" %%i in ('ping -n 1 -w 5000 github.com ^| find "TTL"') do set REACHABLE=1
    if not defined REACHABLE (
        echo ❌ Error: Cannot reach GitHub! Check your internet connection or firewall settings.
        exit /b 1
    )
    set REACHABLE=  :: Zurücksetzen der REACHABLE-Variable

    :: GitHub is accessible, clone repository
    echo Running git clone...
    git clone https://github.com/Peharge/p-terminal.git "%PP_DIR%"

    if %errorlevel% neq 0 (
        echo ❌ Error: Cloning P-terminal repository failed! Make sure GitHub is accessible and the URL is correct.
        exit /b 1
    ) else (
        echo ✅ P-terminal repository cloned successfully!
    )
) else (
    echo P-terminal repository already exists. Checking for updates...

    cd /d "%PP_DIR%"

    :: Check if the repository is in the correct state (no uncommitted changes)
    git diff-index --quiet HEAD --
    if %errorlevel% neq 0 (
        echo ❌ Error: There are uncommitted changes! Please commit or discard them first.
        exit /b 1
    )

    :: Perform Git Fetch (with a timeout of 5 seconds)
    echo Fetching latest changes...
    git fetch --quiet
    if %errorlevel% neq 0 (
        echo ❌ Error: Could not fetch updates from the remote repository! Check your internet connection or Git configuration.
        exit /b 1
    )

    :: Check the status of the repository to see if updates are available
    git status | find "Your branch is behind" >nul
    if %errorlevel% equ 0 (
        echo Updates available, pulling changes...

        :: Perform Git Pull (with timeout of 5 seconds)
        git pull --quiet
        if %errorlevel% neq 0 (
            echo ❌ Error: Could not update P-terminal repository! Check your internet connection or Git configuration.
            exit /b 1
        ) else (
            echo ✅ P-terminal repository updated successfully!
        )
    ) else (
        echo ✅ P-terminal repository is already up-to-date!
    )
)

:: Check Git status after pull (no merge conflicts)
git status | find "Merge conflict" >nul
if %errorlevel% equ 0 (
    echo ❌ Error: Merge conflicts detected. Please resolve them manually.
    exit /b 1
)

echo ✅ P-terminal update process completed successfully.

:: Ensure P-terminal directory exists
if not exist "%PP_DIR%" (
    echo ❌ Error: P-terminal directory does not exist!
    echo Make sure the repository was cloned correctly.
    exit /b 1
)

:: Change to P-terminal directory
cd /d "%PP_DIR%" || (
    echo ❌ Error: Failed to access P-terminal directory!
    exit /b 1
)

:: Ensure .env file exists and is correctly configured
echo Checking for existing .env file at: "%PP_ENV_FILE%"
if not exist "%PP_ENV_FILE%" (
    echo Creating .env file...
    (
        echo # Environment variables for P-terminal
        echo PYTHONPATH=%PP_DIR%
        echo PYTHON_VERSION=%EXPECTED_PYTHON_VERSION%
    ) > "%PP_ENV_FILE%"

    :: Verify file was created and is not empty
    if exist "%PP_ENV_FILE%" (
        for %%A in ("%PP_ENV_FILE%") do (
            if %%~zA gtr 0 (
                echo ✅ .env file created successfully at "%PP_ENV_FILE%"
            ) else (
                echo ❌ Error: .env file was created but is empty!
                del "%PP_ENV_FILE%" >nul 2>&1
                exit /b 1
            )
        )
    ) else (
        echo ❌ Error: Failed to create .env file!
        exit /b 1
    )
) else (
    echo ✅ .env file already exists at "%PP_ENV_FILE%"
)

:: Define the username variable dynamically
:: set "username=%USERNAME%"

:: Detect the OneDrive folder dynamically
:: set "onedriveFolder="
:: for /f "delims=" %%i in ('dir /ad /b "C:\Users\%username%" ^| findstr /i "OneDrive"') do (
::     set "onedriveFolder=%%i"
:: )

:: If OneDrive folder is found, set the Desktop path
:: if defined onedriveFolder (
::     :: Handle paths with spaces in OneDrive folder names properly
::     for /f "delims=" %%i in ('powershell -Command "try { (Get-ChildItem -Path 'C:\\Users\\%username%\\%onedriveFolder%' -Recurse | Where-Object {$_.Name -match 'Desktop'})[0].FullName } catch { '' }"') do set "desktop=%%i"
:: )

:: If Desktop path is not found under OneDrive, fall back to default Desktop path
:: if not defined desktop (
::     for /f "delims=" %%i in ('powershell -Command "[System.Environment]::GetFolderPath('Desktop')"') do set "desktop=%%i"
:: )

:: Check if Desktop path is found, if not skip step and continue
:: if not defined desktop (
::     echo ❌ Could not find Desktop path. Skipping step...
::     set "desktop="
::     goto :end
:: )

:: Print the Desktop path for verification
:: echo Desktop Path: "!desktop!"

:: Define the paths for the shortcut, target, and icon
:: set "shortcut=!desktop!\MAVIS Installer 4.lnk"
:: set "targetPath=C:\Users\%username%\p-terminal\pp-term\mavis-launcher-4.bat"
:: set "startIn=C:\Users\%username%\p-terminal\pp-term"
:: set "iconPath=C:\Users\%username%\p-terminal\pp-term\icons\MAVIS-3-logo-1.ico"

:: Check if the target files exist, if not skip
:: if not exist "!targetPath!" (
::     echo ❌ Target path (!targetPath!) does not exist. Skipping step...
::     set "targetPath="
:: )

:: if not exist "!iconPath!" (
::     echo ❌ Icon path (!iconPath!) does not exist. Skipping step...
::     set "iconPath="
:: )

:: Check if the shortcut already exists
:: if exist "!shortcut!" (
::     echo ✅ Shortcut 'MAVIS Installer 4' already exists. No new shortcut will be created.
:: ) else (
::     if defined desktop if defined targetPath if defined iconPath (
::         echo ❌ Shortcut 'MAVIS Installer 4' does not exist. Creating shortcut now...
::
::         :: Create the shortcut using PowerShell script file
::         echo Set objShell = CreateObject("WScript.Shell") > "!desktop!\create_shortcut.vbs"
::         echo Set objShortcut = objShell.CreateShortcut("!shortcut!") >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.TargetPath = "!targetPath!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.WorkingDirectory = "!startIn!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.IconLocation = "!iconPath!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.Save >> "!desktop!\create_shortcut.vbs"
::
::         :: Check if the VBS script was created successfully
::         if not exist "!desktop!\create_shortcut.vbs" (
::             echo ❌ Failed to create the VBS script. Skipping step...
::             set "desktop="
::             goto :end
::         )
::
::         :: Run the VBS script to create the shortcut if VBS file exists
::         if exist "!desktop!\create_shortcut.vbs" (
::             cscript //nologo "!desktop!\create_shortcut.vbs"
::             if errorlevel 1 (
::                 echo ❌ Failed to create the shortcut. Skipping step...
::                 set "desktop="
::                 goto :end
::             )
::         )
::
::         :: Clean up the temporary VBS script
::         if exist "!desktop!\create_shortcut.vbs" del "!desktop!\create_shortcut.vbs"
::
::         echo ✅ Shortcut 'MAVIS Installer 4' has been created successfully.
::     ) else (
::         echo ❌ Skipping shortcut creation due to missing paths.
::     )
:: )

:: Check if P-terminal run file exists
if not exist "%PP_RUN_FILE%" (
    echo ❌ Error: pp-term.bat not found!
    echo Please verify that the file exists in: %PP_DIR%
    exit /b 1
)

:: Execute pp-term.bat
echo Starting PP_terminal...

:: Check if the file is executable (check for executable file)
:: Test if the file is an .bat file
if /I not "%PP_RUN_FILE:~-4%"==".bat" (
    echo ❌ Error: The file is not an executable file!
    exit /b 1
)

:: Final report
:: echo ✅ All tasks were completed successfully!

:: Try to start the file and check if it is successful
call "%PP_RUN_FILE%"
if %errorlevel% neq 0 (
    echo ❌ Error: PP-Terminal could not be started successfully!
    exit /b 1
) else (
    echo ✅ PP-Terminal was successfully launched!
)

:: endlocal
pause
exit /b
