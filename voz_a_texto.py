
"""voz_a_texto.ipynb
# *Generar Voz desde Texto *
**Autor**: Emilio Estefan <br>
**Fecha de creacion**: 22 de agosto del 2021
"""


texto = "Equis de de de de de saludos carita fachera facherita" 
lenguage = "es"
from gtts import gTTS
import os 

myobj = gTTS(text = texto, lang= lenguage, slow= False)
myobj.save("Audio.mp3")
os.system("Audio.mp3")

