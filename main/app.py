from vosk import Model, KaldiRecognizer
import pyaudio
from utils.sentimentAnalysis import getPerspectiveScore, getGPTScore
from utils.webcam import webcamController
import threading
from utils.textMessage import sendEmergencySMS


model = Model(model_name = "vosk-model-small-en-us-0.15")

text_sent = False
score_history = [0, 0, 0]   # tracks last 5 responses
response_history = ['', '', '']

recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)

                    
webcamcontroller = webcamController()
webcam_thread = threading.Thread(target=webcamcontroller.run)
webcam_thread.start()



if __name__ == '__main__':
    try:
        while True:
            data = stream.read(2048, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                text = text[14:-3]
                if text != '':
                    print("Transcribed Text: " + text)
                    response_history.pop(0)
                    response_history.append(text)
                    score_history.pop(0)
                    #score_history.append(getPerspectiveScore(text))
                    score_history.append(getGPTScore(text))
                    average_score = sum(score_history)/len(score_history)
                    print("Toxicity Level: " + str(average_score))
                    if (average_score > 0.5 and webcamcontroller.streaming == False):
                        print("***************\nSTARTING WEBCAM\n***************")
                        webcamcontroller.start()
                        if not text_sent:
                            sendEmergencySMS()
                            text_sent = True
                    elif (average_score < 0.25 and webcamcontroller.streaming == True):
                        print("***************\nSTOPPING WEBCAM\n***************")
                        webcamcontroller.stop()
    except Exception as e:
        print(str(e))

    
