import pyttsx3                             #pyttsx3 is a module for tts support, which works offline aswell.

engine = pyttsx3.init()                    #init() function is used to create a new TTS engine instance

voices = engine.getProperty("voices")       #using getProperty() method to fetch different voices

rate = engine.getProperty("rate")           #using getProperty() method to fetch functionality of managing the speech rate.


def tts_sbreak():
    text_speech = "Your Work Session hass been completed, It's time for a short break!"

    for voice in voices:
        engine.setProperty("voice", voice.id)        #using setProperty() method to add fetched voices (it takes two arguments) 
        engine.setProperty("rate", rate-40)          #using setProperty() method to decrease speech rate.

        engine.say(text_speech)                      #say() method is used for tts implementation
        engine.runAndWait()                          #runAndwait() method is used to process the voice command.
                         

def tts_lbreak():
    text_speech = "All sessions have been completed!"

    for voice in voices:
        engine.setProperty("voice", voice.id)        #using setProperty() method to add fetched voices (it takes two arguments) 
        engine.setProperty("rate", rate-40)          #using setProperty() method to decrease speech rate.

        engine.say(text_speech)                      #say() method is used for tts implementation
        engine.runAndWait()                          #runAndwait() method is used to process the voice command.

def tts_work():
    text_speech = "The Break is over, Time to get back to the work!"

    for voice in voices:
        engine.setProperty("voice", voice.id)        #using setProperty() method to add fetched voices (it takes two arguments) 
        engine.setProperty("rate", rate-40)          #using setProperty() method to decrease speech rate.

        engine.say(text_speech)                      #say() method is used for tts implementation
        engine.runAndWait()                          #runAndwait() method is used to process the voice command.


