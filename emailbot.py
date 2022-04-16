import email
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('somu160202@gmail.com', 'saya2563')
    email = EmailMessage()
    email['From'] = 'somu160202@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)   

email_list = {
    'Jack': 'amey160202@gmail.com',
    'somu': 'somu160202@gmail.com',
    'papa': 'amayash@gmail.com',
    'yash': 'somu16022002@gmail.com'
}

def get_email_info():
    talk('To Whom you want to send email')
    name =  get_info()
    receiver =email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject = get_info()
    talk('compose your email')
    message = get_info()

    talk('Thankyou, we are sending your email')
    send_email(receiver,subject,message)
   


    
get_email_info()   

