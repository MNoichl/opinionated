
import requests
import zipfile
import io
import os
import shutil
from pathlib import Path
import opinionated # this works?



# download fonts from google fonts and save them in the fonts folder:
def download_googlefont(font='Roboto Condensed'):
    
    # download the font
    url = f'https://fonts.google.com/download?family={font}'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    # extract into the package folder
    font_folder = Path(opinionated.__file__).parent / 'fonts'
    z.extractall(font_folder)
    print(f'Font saved to: {font_folder / f}')