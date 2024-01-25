import json

def load_text():
    translations_file = "responses.json"
    try:
        with open(translations_file, 'r', encoding='utf-8-sig') as file:
            file_content = file.read()
            print("File Content:")
            print(file_content)
            print("TYPE OF CONTENT ---> ", type(file_content))
            translations = json.load(file)
        return translations
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        raise


trs = {
  "en": {
    "farewell": "Goodbye, see you later!",
    "error": "An error occurred.",
    "lost_score": "Lost game with score",
    "lost": "Lost game",
    "inc_l": "Incorrect letter, now ",
    "cn": "correct, now ",
    "finish": "We're done with score ",
    "congrats": "Congrats",
    "pred": "Predicted character ",
    "perf": "Perform "
  },
  "es": {
    "farewell": "¡Adiós, hasta luego!",
    "error": "Se produjo un error.",
    "lost_score": "Juego perdido con score ",
    "lost": "juego perdido",
    "inc_l": "Letra incorrecta, ahora ",
    "cn": "correcto, ahora ",
    "finish": "Hemos acabado. Tu puntuación de hoy: ",
    "congrats": " puntos ¡Enhorabuena!",
    "pred": "carácter predicado ",
    "perf": "Demostra"
  }
}