import Pyro4
import os
from gtts import gTTS
from pygame import mixer

@Pyro4.expose
class Servidor:
    def __init__(self):
        pass

    def audio(self, txt, nome):
        self.tts = gTTS(text = txt, lang='pt')
        self.audio = self.tts.save(nome+'.mp3')
        mixer.init()
        mixer.music.load(nome+'.mp3')
        mixer.music.play()
        while(mixer.music.get_busy()): pass
        print("Reproduzido! =)" )

def main():
    Pyro4.Daemon.serveSimple({ Servidor: "tarefa5"})

if __name__ == "__main__":
    main()
