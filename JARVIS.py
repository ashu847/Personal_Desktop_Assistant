import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os
import random
from math import sin,pi
import matplotlib.pyplot as plt
import numpy as np
import calendar
from sys import exit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0],id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 5:
        speak('Good morning ')
    elif 5 < hour < 12:
        speak('Good morning')
    elif 12 <= hour < 17:
        speak('Good afternoon')
    elif 17 <= hour < 20:
        speak('Good evening')
    else:
        speak('Good evening')

    speak('I am Desktop assistant . Please tell me how may I help you')

def takecommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")



    except Exception as e:
        #print(e)
        print('Say that again please....')
        return 'none'
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()


        if 'wikipedia' in query:
            try:
                speak('Searching wikipedia....')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak('according to wikipedia')
                print(results)
                speak(results)
            except exception as e:
                print(e)
                speak('i did not get what you say')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'play song' in query:
            speak('playing song')
            music_dir = 'D:\\songs'
            song = os.listdir(music_dir)
            print(song)
            x = random.randint(1,4)
            os.startfile(os.path.join(music_dir, song[x]))

        elif 'play chak de india' in query:
            music_dir = 'D:\\songs'
            song = os.listdir(music_dir)
            i = 0
            while i < 4:
                if 'Chak_De_India_Bestwap.in.mp3' == song[i]:
                    os.startfile(os.path.join(music_dir, song[i]))
                i += 1

        elif 'play video' in query:
            speak('playing video')
            music_dir = 'D:\\movies'
            video = os.listdir(music_dir)
            print(video)
            x = random.randint(1,6)
            os.startfile(os.path.join(music_dir, video[x]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir the time is. ")
            speak(strtime)

        elif 'microwind' in query:
            speak('opening microwind')
            codepath = "D:\microwind\Microwind3.exe"
            os.startfile(codepath)

        elif 'email to ashu' in query:
            try:
                speak('what should i say?')
                content = takecommand()
                to="ashumittal847@gmail.com"
                sendEmail(to,content)
                speak('email has been sent!')

            except exception as e:
                print(e)
                speak('i m not able to send this email')

        elif 'calendar' in query:
            speak('opening the calendar')
            print(calendar.month(2020, 11))


        elif 'random sequence' in query:

            def binary(symbol, sym_len):

                # symbol: no. of symbols to be generated
                # sym_len : symbol duration or no. of samples in one symbol
                # generate random numbers (between 1 and 0)

                rand_n = np.random.rand(symbol)
                rand_n[np.where(rand_n >= 0.5)] = 1
                rand_n[np.where(rand_n < 0.5)] = 0
                sig = np.zeros(int(symbol * sym_len))

                # generate symbols

                id_1 = np.where(rand_n == 1)

                for i in id_1[0]:
                    temp = int(i * sym_len)
                    sig[temp:temp + sym_len] = 1
                return sig


            Fs = 100
            Fc = 10
            T = 1
            t = np.arange(0, T, 1.0 / Fs)
            x = np.sin(2 * pi * Fc * t)

            # Generate random binary signal

            Td = 0.1  # bit duration
            samples = int(Td * Fs)  # samples in one bit
            sym = int(np.floor(np.size(t) / samples))
            sig = binary(sym, samples)

            plt.figure()
            plt.plot(sig)
            plt.title('Random binary signal')
            plt.xlabel('samples')
            plt.ylabel('Amplitude')
            plt.grid()
            plt.show()




        elif 'a s k' in query:

            def binary(symbol, sym_len):

                # symbol: no. of symbols to be generated
                #sym_len : symbol duration or no. of samples in one symbol
                # generate random numbers (between 1 and 0)

                rand_n = np.random.rand(symbol)
                rand_n[np.where(rand_n >= 0.5)] = 1
                rand_n[np.where(rand_n < 0.5)] = 0
                sig = np.zeros(int(symbol * sym_len))

                # generate symbols
                id_1 = np.where(rand_n == 1)

                for i in id_1[0]:
                    temp = int(i * sym_len)
                    sig[temp:temp + sym_len] = 1

                return sig


            # carrier information

            Fs = 100  # sampling frequency
            Fc = 10  # carrier frequency
            T = 1  # nsimulation time (sec)
            t = np.arange(0, T, 1.0 / Fs)

            # carrier wave
            x = np.sin(2 * pi * Fc * t)

            # Generate random binary signal
            Td = 0.1  # bit duration
            samples = int(Td * Fs)  # samples in one bit
            sym = int(np.floor(np.size(t) / samples))
            sig = binary(sym, samples)

            # plot
            plt.subplot(2, 1, 1)
            plt.plot(t, sig)
            plt.title('Random binary signal')
            plt.xlabel('Time(s)')
            plt.ylabel('Amplitude')
            plt.grid()

            # Generate ASK
            ask = x * sig

            plt.subplot(2, 1, 2)
            plt.plot(t, ask)
            plt.title('Amplitude shift keying')
            plt.xlabel('Time(s)')
            plt.ylabel('Amplitude')
            plt.grid()
            plt.tight_layout()
            plt.show()





        elif 'fsk' in query:
            def binary(symbol, sym_len):
                # symbol: no. of sumbols to be generated
                # sym_len : symbol duration or no. of samples in one symbol
                # generate random numbers (between 1 and 0)
                rand_n = np.random.rand(symbol)
                rand_n[np.where(rand_n >= 0.5)] = 1
                rand_n[np.where(rand_n < 0.5)] = 0

                sig = np.zeros(int(symbol * sym_len))

                # generate symbols
                id_1 = np.where(rand_n == 1)

                for i in id_1[0]:
                    temp = int(i * sym_len)
                    sig[temp:temp + sym_len] = 1

                return sig


            # carrier information
            Fs = 1000  # sampling frequency
            Fc = 100  # carrier frequency
            T = 1  # nsimulation time (sec)
            t = np.arange(0, T, 1.0 / Fs)

            # carrier wave
            x = np.sin(2 * pi * Fc * t)

            # Generate random binary signal
            Td = 0.1  # bit duration
            samples = int(Td * Fs)  # samples in one bit
            sym = int(np.floor(np.size(t) / samples))

            sig = binary(sym, samples)

            # plot
            plt.subplot(2, 1, 1)
            plt.plot(t, sig)
            plt.title('Random binary signal')
            plt.xlabel('Time(s)')
            plt.ylabel('Amplitude')
            plt.grid()

            # Generate FSK
            f=Fc+sig*Fc/2
            fsk=np.sin(2*pi*f*t)
            plt.subplot(2, 1, 2)
            plt.plot(t, fsk)
            plt.title('Frequency shift keying')
            plt.xlabel('Time(s)')
            plt.ylabel('Amplitude')
            plt.grid()
            plt.tight_layout()
            plt.show()

        elif 'psk' in query:
            def PSK(fc, data):
                N = 100 * fc
                tiv = 1 / N
                t = 0
                s = []
                while (t < len(data)):
                    s = s + [data[int(t)] * sin(2 * pi * fc * t)]
                    t = t + tiv
                return s

            plt.plot(PSK(1, [1,-1,1,1,-1,1]))
            plt.show()

        elif 'shutdown' in query:
            speak('Assistant is shutting down')
            exit()