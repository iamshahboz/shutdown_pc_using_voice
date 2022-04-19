#importing required modules
import os
import pyttsx3
import speech_recognition as sr

#Creating Class
class ShutDown:
    #method to take choice commands
    def take_command(self):
        #using recognizer and microfon for imput voice
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            # number of seconds in non speaking audio
            r.pause_threshold = 0.7
            audio = r.listen(source)
            #voice input is identified
            try:
                #listening voice commands in English
                print("Recognizing")
                Query = r.recognize_google(audio, language="en-in")

                #Displaying the voice command
                print("The query is printed='", Query, "'")
            except Exception as e:
                #Displaing exception
                print(e)
                #Handling exception
                print("Say that again sir")
                return "None"
            return Query

    #method for voice output
    def Speak(self, audio):
        #constructor call for pyttsx3.init()
        engine = pyttsx3.init("sapi5")
        #setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty("voice", voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    #method to self shutdown system
    def quitSelf(self):
        self.Speak("do you want to switch off the computer")
        #input voice command
        take = self.take_command()
        choice = take
        if "yes" in choice:
            #shutting down
            print("Shutting down the computer")
            os.system("shutdown /s /t 30")
        if "no" in choice:
            print("Thank you sir")
            self.Speak("thank you sir")

if __name__ == '__main__':
    Maam = ShutDown()
    Maam.quitSelf()    


        

