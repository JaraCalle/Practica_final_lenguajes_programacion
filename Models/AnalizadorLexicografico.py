from vars import BNF_EMOJIS
import os
import re


class AnalizadorLexicografico:
    def __init__(self, texto_: str) -> None:
        self.texto = texto_

    def analizar(self) -> tuple:
        self.remplazar_emojis()
        return self.texto, self.contar_palabras_en_espanol(), self.contar_emojis()

    def remplazar_emojis(self) -> None:
        for patron, emoji in BNF_EMOJIS.items():
            self.texto = re.sub(patron, emoji, self.texto)

    def contar_emojis(self) -> int:
        emojis = [emoji for _, emoji in BNF_EMOJIS.items()]
        patron = r'(?:' + '|'.join(emojis) + r')'
        coincidencias = re.findall(patron, self.texto, re.IGNORECASE)
        return len(coincidencias)

    def contar_palabras_en_espanol(self) -> int:
        carpeta = "C:\\Users\\Lenovo\\PycharmProjects\\Practica_final_lenguajes_programacion\\static\\dics"
        palabras = []
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".txt"):
                with open(os.path.join(carpeta, archivo), 'r', newline='', encoding='utf-8') as diccionario:
                    for line in diccionario:
                        palabra = re.sub(r'\d', '', line.strip())
                        palabra = palabra.strip().split(',')[0]
                        palabras.append(re.escape(palabra))

        patron = r'\b(?:' + '|'.join(palabras) + r')\b'
        coincidencias = re.findall(patron, self.texto, re.IGNORECASE)
        print(coincidencias)
        return len(coincidencias)
