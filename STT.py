import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        #audio = r.listen(source)
        audio = r.listen(source, phrase_time_limit = 0)
        print("Recognizing Now .... ")


        # recognize speech using google

        try:

            #print("You have said \n" + r.recognize_google(audio))
            text = r.recognize_google(audio, language ='en-US') 
            print("You have said \n" + text)
            print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))

        


        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
            
    return text


if __name__ == "__main__":
    main()