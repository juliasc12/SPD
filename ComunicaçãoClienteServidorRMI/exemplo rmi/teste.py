from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("teste1.mp3")
play(song)
