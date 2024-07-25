import speech_recognition as sr

def speechrecognition_from_mic():
  recogniser = sr.Recognizer()
    
  with sr.Microphone() as source:
       audio = recogniser.listen(source)
       print("please say something")

  try:
     text = recogniser.recognize_google(audio)
     print("you said" + text)
      
  except sr.RequestError():
        print("sorry this service is unavaliabel")  
 

  except sr.UnknownValueError():
      print("sorry i dont understand")

speechrecognition_from_mic()