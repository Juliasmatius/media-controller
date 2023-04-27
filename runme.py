import subprocess
import sys
import os
import os.path
def install(package):
    print(package+" not installed")
    print("Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("Installation of "+package+" compleated")

if os.path.isfile("CLMControl.exe"):
    pass
else:
    try:
        print("Checking if for some ungodly reason you dont have requests...")
        import requests
    except ImportError as e:
        install("requests")
    import requests
    print("Downloading CLMControl...")
    url = 'https://github.com/InvalidCastEx/CommandLineMedia/releases/download/v1.1.0.0/CLMControl.1.1.0.0.zip'
    r = requests.get(url, allow_redirects=True)
    open('clmcontrol.zip', 'wb').write(r.content)
    print("Download complete")
    print("Unzipping CLMControl...")
    import zipfile
    with zipfile.ZipFile("clmcontrol.zip", "r") as zip_ref:
        zip_ref.extractall("")
    print("Unzip complete")

try:
    print("Checking if pyfiglet is installed...")
    import pyfiglet
except ImportError as e:
    install("pyfiglet")
try:
    print("Checking if keyboard is installed...")
    import keyboard
except ImportError as e:
    install("keyboard")
try:
    print("Checking if Guli is installed...")
    import guli
except ImportError as e:
    install("guli")
try:
    print("Checking if pyglet is installed...")
    import pyglet
except ImportError as e:
        install("pyglet")
try:
    print("Checking if nicegui is installed...")
    import nicegui
except ImportError as e:
    from pyfiglet import Figlet
    custom_fig = Figlet(font='starwars')
    print(custom_fig.renderText('Nicegui install takes long!!'))
    import time
    time.sleep(5)
    install("nicegui")
import nicegui
import guli
import pyfiglet
from main import main
main()
