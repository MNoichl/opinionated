
import requests
import zipfile
import io
import os
import shutil
from pathlib import Path




# download fonts from google fonts and save them in the fonts folder:
def download_font(font='Roboto Condensed'):
    
    # download the font
    url = f'https://fonts.google.com/download?family={font}'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    
    # move the font to the fonts folder
    font_folder = Path(__file__).parent / 'fonts'
    font_folder.mkdir(exist_ok=True)
    for f in os.listdir():
        if f.endswith('.ttf'):
            shutil.move(f, font_folder / f)
    
    # remove the downloaded font folder
    shutil.rmtree(font_folder / font)
    
    # update the font cache
    fm._rebuild()
    
    # print the font path
    print(f'Font saved to: {font_folder / f}')







