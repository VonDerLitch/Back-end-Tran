from docx import Document
import speech_recognition as sr
from tkinter import filedialog

r = sr.Recognizer()
Document = Document()
file_path = filedialog.askopenfilename()

harvad=sr.AudioFile(file_path)
with harvad as source:
    audio=r.record(source)
    val=r.recognize_google(audio, language="pt-BR")
    p = input(str("digite o nome do arquivo: "))
    paragraph = Document.add_paragraph("\n" + r.recognize_google(audio, language="pt-BR"))

    Document.save("{}.docx".format(p))