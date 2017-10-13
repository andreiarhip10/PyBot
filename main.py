import aiml
import os
sessionId = 12345


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "basic_chat.aiml")
    kernel.saveBrain("bot_brain.brn")

sessionData = kernel.getSessionData(sessionId)


occupation=0
path = "E:\FII\Anul 3\Inteligenta Artificiala\Laborator 1\PyBot\users.txt"
username=""
ok=0
exists=0
rem_count=0

while True:
    message = raw_input("\nYou: ")
    #to implement in aiml
    if message == "Bye":
        print ("Anon: Bye" )
        exit()
    elif message == "save":
        kernel.bootstrap(learnFiles="basic_chat.aiml")
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
                     if occupation!="" and ok==0:
                         import csv
                         with open(path) as inf:
                             reader = csv.reader(inf, delimiter=" ")
                             for line in reader:
                                if username==line[0] and age==line[1] and occupation==line[2]:
                                    exists=1;
                         inf.close();
                         if exists==0:
                             with open(path, 'a') as file:
                                file.write(username + ' ' + age + ' ' + occupation + '\n')
                             ok = 1
                         else:
                             if rem_count == 0:
                                 print("Anon: Have we talked before?")
                                 rem_count = 1


    #if ok==1:
        #kernel.bootstrap(learnFiles="std_startup.xml", commands="LOAD AIML B")
        #kernel.saveBrain("bot_brain.brn")

