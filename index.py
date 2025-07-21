import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('activated...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('Not understanding...')
        except sr.RequestError as e:
            print(e)

def speachtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

# function to create a file:
def create_file():
     file_path = 'C:/Users/Furqan Ahmed/Desktop/python-50 projects/Jarvis-voice/demo.txt'
     if os.path.exists(file_path):
          return 'exists'
     try:
          with open('demo.txt', 'w+') as f:
               f.write('file is created by Jarvis:')
          return 'created'
     except Exception as e:
          print(f'error createing file {e}')
          return 'error'

# main coding for working with jarvis
if __name__ == '__main__':
    if sptext() == 'Jarvis' or 'jarvis':
        speachtx('Yes sir! I am listning..')
        while True:
          data1 = sptext()
          if  'your name' in data1:
             name = 'my name is Jarvis'
             speachtx(name)
        
          elif 'old' in data1:
             name1 = 'I am a jarvis a voice assistant I dont have age..'
             speachtx(name1)
        
          elif 'create the file' in data1:
             ans = 'ok I am creating a file'
             speachtx(ans)

            #  checking file status here 
             file_status = create_file()
             
             if file_status == 'created':
                ans1 = 'file is ready sir!' 
                speachtx(ans1)
             elif file_status == 'exists':
                  ans2 = 'file is also created at the system level sir!'
                  speachtx(ans2)
             else:
                  ans3 = 'sorry there is an issue while create a file sir!'
                  speachtx(ans3)

            
          elif 'time' in data1:
             time = datetime.datetime.now().strftime('%I%M%p')
             speachtx(f'It is {time} in Pakistan')

          elif 'YouTube' in data1:
             reply = ('Okay sir I am opening Youtube for you!')
             speachtx(reply)
             webbrowser.open('https://youtube.com/')
        
          elif 'Google' in data1:
             reply = ('Okay sir I am opening Google for you!')
             speachtx(reply)
             webbrowser.open('https://google.com/')
        
          elif 'LinkedIn' in data1:
             reply = ('Okay sir I am opening Linkedin profile for you!')
             speachtx(reply)
             webbrowser.open('https://www.linkedin.com/in/furqanahmed-n/')
        
          elif 'joke' in data1:
             joke_1 = pyjokes.get_joke(language='en', category='all')
             speachtx(f'{joke_1} hahaha')
        
          elif 'song' in data1:
             address = 'C:/Users/Furqan Ahmed/Desktop/songs'
             list_song = os.listdir(address)
             os.startfile(os.path.join(address, list_song[1]))
        
          elif 'remove' in data1:
             ans = 'okay sir I am going to delete the file that I created befor'
             speachtx(ans)
             os.remove('C:/Users/Furqan Ahmed/Desktop/python-50 projects/Jarvis-voice/demo.txt')
          elif 'exit' in data1:
             speachtx('okay sir I am going to stop my self Thank you..')
             break
    else:
        print('thanks')