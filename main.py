import pyttsx3      # pip install pyttsx3
import PyPDF2       # pip install PyPDF2

# first add the pdf book in same folder of python project
book = open('ms-17.pdf','rb')  # select book and mention rb means read book


pdfreader = PyPDF2.PdfFileReader(book) # here it will start recognizing the text

pages = pdfreader.numPages  # here you will get no of pages

print(pages)


speaker = pyttsx3.init()        # initiate python text-to-speech

voices = speaker.getProperty('voices') # get all voices

speaker.setProperty('voice',voices[1].id)
            # set voice by passing 0, 1
            # 0 is for female voice
            # 1 is for male voice

speaker.setProperty('rate',140)  # set the speech rate here by passing value


for num in range(7,pages):  # for loop to iterate from the page you want to the end of book

    page = pdfreader.getPage(num) # here it takes the page which you want to listen

    text = page.extractText() # here it extracts text content from that page

    speaker.say(text) # here your audio book will begin


speaker.runAndWait()