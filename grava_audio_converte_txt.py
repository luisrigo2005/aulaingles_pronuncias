# Installar as bibliotecas
import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
recognizer = sr.Recognizer()

# Captura áudio do microfone
with sr.Microphone() as source:
    print('Diga algo: ')
    audio = recognizer.listen(source)

# Converte o áudio em texto utilizando o português como linguagem
try:
    text = recognizer.recognize_google(audio,language='pt-BR')
except sr.UnknownValueError:
    print("O Google Speech Recognition não entendeu o seu áudio")

# Salva o texto convertido em um arquivo
with open("texto.txt", "w") as f:
    f.write(text)

# Imprime o texto
print(text)