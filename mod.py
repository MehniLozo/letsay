import random 
import string
from talk import talk
from utils import trs



class Engine:
    def __init__(self):
        self.current_letter = None
        self.current_group = 1 
        self.score = 0
        self.maxt = 5
        self.cur_t = 0
        from handsframes import lang
    def start_new(self):
        self.generate_letter()
        self.score = 0
        self.current_group = 1
    def generate_letter(self):
        self.current_letter = random.choice(string.ascii_uppercase)
        return self.current_letter
    def validate_user_resp(self,user_response):
        return user_response == self.current_letter
    def switch_to_group_2(self):
        self.current_group = 2
        self.current_letter = random.choice(string.ascii_uppercase)
        return self.current_letter

    def repeat_letter(self,letter):
        from handsframes import lang
        lc = "en-US" if lang == "en" else "es-ES" # language code
        if not letter or not self.validate_user_resp(letter):
            if self.current_group == 2:
                speech_text = trs[lang]["lost_score"] + str(self.score)
                talk(trs[lang]['lost'],lc)
                print(speech_text)
                exit(0)
            else:
                #l = self.switch_to_group_2()
                l = self.generate_letter()
                speech_text = trs[lang]['inc_l'] + l
                talk(speech_text,lc)
        else:
            self.cur_t += 1
            if self.cur_t <= self.maxt:
                self.score += ord(letter)
                let = self.generate_letter()
                speech_text = trs[lang]['cn'] + let
                talk(speech_text,lc)
            else:
                speech_text = (
                    trs[lang]['finish'] +
                    str(self.score) + trs[lang]['congrats']
                )
                talk(speech_text,lc)
        return speech_text

	
