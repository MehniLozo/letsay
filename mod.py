import random 
import string
from talk import talk
class Engine:
    def __init__(self):
        self.current_letter = None
        self.current_group = 1 
        self.score = 0
        self.maxt = 5
        self.cur_t = 0
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
        if not letter or not self.validate_user_resp(letter):
            if self.current_group == 2:
                speech_text = "Lost game with score " + str(self.score)
                talk("Lost game")
                print(speech_text)
                exit(0)
            else:
                l = self.switch_to_group_2()
                speech_text = "Letra incorecta, ahora " + l
                talk("Incorrect letter now, " + l)
        else:
            self.cur_t += 1
            if self.cur_t <= moderator.maxt:
                self.score += ord(letter)
                let = self.generate_letter()
                speech_text = "Correcto ahora: " + let
                talk("Good job now " + let)
            else:
                speech_text = (
                    "Hemos acabado. Tu puntuación de hoy: " +
                    str(self.score) + "puntos ¡Enhorabuena!"
                )
                talk("We're done with score " + str(self.score))
        return speech_text

    def help_fun(self):
        speech_text = (
            "Voy a decir algunos letras. Escucha con atención y cuando yo haya terminado, "
            "repítalo inmediatamente. "
            "Si necesitas saber cómo se juega, ¡pregúntame!"
        )
        return speech_text

	
