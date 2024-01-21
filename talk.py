from google.cloud import texttospeech
from playsound import playsound

def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content

#detected_letter = 'A'  
#audio_data = text_to_speech(detected_letter)

def talk():
    with open("output_audio.wav", "wb") as out_file:
        out_file.write(audio_data)
        
    playsound("output_audio.wav")
