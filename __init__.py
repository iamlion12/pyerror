from pydub import AudioSegment
from pydub.playback import play
import traceback

def error_check(func):
    def function_wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            song = AudioSegment.from_wav('error.wav')
            play(song)
    return function_wrapper

@error_check
def division(a,b):
    print(a/b)

division(a=2, b=3)
division(a=1, b=23)
division(a=1, b=0)
