import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 210)

volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level

engine.say("I will speak this text")
engine.say('My current speaking rate is ' + str(rate))
engine.stop()


engine.runAndWait()