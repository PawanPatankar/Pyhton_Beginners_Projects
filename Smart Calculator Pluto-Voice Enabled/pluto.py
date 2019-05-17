import pyttsx3;
import sys
sys.path.append('/my/')
import my
from my.mathy import *

engine=pyttsx3.init();
engine.setProperty('rate',160)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

engine.say(responses[0])
print(responses[0])

engine.say(responses[1])
print(responses[1])
engine.runAndWait();


while True:
    print()
    engine.say("What is Your Question Sir:")
    engine.runAndWait();
    text=input("What is Your Question Sir : ")
    engine.say(f"{text}")
    engine.runAndWait();



    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])

                print (f"The Answer is {r}")
                engine.say(f"The Answer is {r}")
                engine.runAndWait();
            except:
                print("Something is wrong Please try again")
                engine.say("Something is wrong Please try again")
                engine.runAndWait();
                
            finally:
                break
        elif word.upper() in command.keys():
             command[word.upper()]()
             break

    else:
        sorry()
        engine.say("Sorry this is beyond my ability")
        engine.runAndWait();

