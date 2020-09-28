from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES
import speech_recognition as sr
import pyttsx3

root = Tk()
width = 1080
height = 500
root.geometry(f'{width}x{height}')
# Resizing Window - Prohibited
root.resizable(0,0)
root.title("Language Translator")
root.config(bg = "light cyan")

Label(root, text = "LANGUAGE TRANSLATOR",font = ('Comic Sans MS', 22, 'bold'), bg = "light cyan").pack()
Label(root,text ="Project By Paraj Shah", font = ('Comic Sans MS', 14, 'bold'), width = '20',bg = "light cyan").pack(side = 'bottom')

# Input Widget
Label(root,text ="Enter Text", font = 'arial 14 bold',bg = "light cyan").place(x = 200,y = 60)
Input_text = Text(root,font = 'arial 10', height = 18, wrap = WORD, padx = 5, pady = 5, width = 60)
Input_text.place(x = 30,y = 100)

# Output Widget
Label(root,text ="Output", font = 'arial 14 bold',bg = "light cyan").place(x = 780,y = 60)
Output_text = Text(root,font = 'arial 10', height = 18, wrap = WORD, padx = 5, pady = 5, width = 60)
Output_text.place(x = 600 , y = 100)

language = list(LANGUAGES.values())

# Input language selector
src_lang = ttk.Combobox(root, values = language, width = 22)
src_lang.place(x = 30,y = 60)
src_lang.set('english')

# Output language selector
dest_lang = ttk.Combobox(root, values = language, width = 22)
dest_lang.place(x = 600,y = 60)
dest_lang.set('Choose language')

def voice_translate():
    speak("Speak Now!")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        voice_text = r.recognize_google(audio)
        print("Recognised Text: ",voice_text)
        
        Input_text.delete(1.0, END)
        Input_text.insert(END, voice_text)
        
        translator = Translator()
        translated = translator.translate(text = Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def reverse():
    global src_lang,dest_lang
    print("Source Lang:",src_lang.get(),"\nDestination Lang:", dest_lang.get())
    src = src_lang.get()
    dest = dest_lang.get()
    src_lang.set(f'{dest}')
    dest_lang.set(f'{src}')

def translate():
    translator = Translator()
    translated = translator.translate(text = Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = translate , bg = 'sky blue1')
trans_btn.place(x = 300, y = 420)

voice_trans_btn = Button(root, text = 'Voice Translate',font = 'arial 12 bold',pady = 5,command = voice_translate, bg = 'sky blue1')
voice_trans_btn.place(x = 650, y = 420)

reverse_btn = Button(root, text = 'Reverse Languages',font = 'arial 12 bold',pady = 5,command = reverse, bg = 'sky blue1')
reverse_btn.place(x = 445, y = 420)

root.mainloop()
