import aiml
import os
sessionId = 12345


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std_startup.xml", commands = "LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")

sessionData = kernel.getSessionData(sessionId)


occupation=0
path = 'E:\FII\Anul 3\Inteligenta Artificiala\Laborator 1\PyBot\users.txt'


while True:
    message = raw_input("\nYou: ")
    #to implement in aiml
    if message == "Bye":
        print ("Anon: Bye" )
        exit()
    elif message == "save":
        kernel.bootstrap(learnFiles="std_startup.xml", commands="LOAD AIML B")
        kernel.saveBrain("bot_brain.brn")
     elif message == "hello":
        bot_response = kernel.respond(message, sessionId)
        print ("Anon: " + bot_response)
    else:
        bot_response = kernel.respond(message, sessionId)
        username = kernel.getPredicate("username", sessionId)
        if username =="":
            bot_response = kernel.respond("name not given", sessionId)
            print ("Anon: " + bot_response)
        else:
            bot_response = kernel.respond(message, sessionId)
            age = kernel.getPredicate("age", sessionId)
            if age =="":
                bot_response1 = kernel.respond("age not given", sessionId)
                print ("Anon: " + bot_response + ' '+bot_response1)
            else:
                bot_response2 = kernel.respond(message, sessionId)
                occupation = kernel.getPredicate("occupation", sessionId)
                if occupation == "":
                     bot_response3 = kernel.respond("occupation not given", sessionId)
                     print ("Anon: " + bot_response2+ ' '+ bot_response3)
                else:
                     bot_response4 = kernel.respond(message, sessionId)
                     print ("Anon: " + bot_response4)


        # occupation = kernel.getPredicate("occupation", sessionId)
        # if occupation != 0:
        #     username = kernel.getPredicate("username", sessionId)
        #     age = kernel.getPredicate("age", sessionId)
        #     with open(path, 'a') as file:
        #         file.write(username+' '+age+' '+occupation+'\n')