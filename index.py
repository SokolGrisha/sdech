import rsa
import urllib.request
import threading


global pubf
(pubu, privu) = rsa.newkeys(1024)


def stru(txt):
    txt=str(txt).split(" ")[0]+str(txt).split(" ")[1]
    return txt


def rsu(txt):
    txt=str(txt).split(",")
    txt=txt[0]+", "+txt[1]
    return txt


def writer(serv):
    global lastmsg
    while True:
        global pubf
        msg = rsa.encrypt(input("msg:"), pubf)
        t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg)).read().decode("utf-8")
        lastmsg = msg
        print(msg)


def reader(serv):
    global lastmsg
    while True:
        while msg!=lastmsg:
            msg = urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
            global pubu
            global privu
            msg = rsa.decrypt(t, privu)
    print(msg)


print("This file is needed to connect to server!")
srv = str(input("Server:"))
cc = input("Create\Connect ? cr\co")
tred = input("Thread?")
msg = input("Your first message:")
if(cc=="cr"):
    t = urllib.request.urlopen(srv+"/creat.php?tred="+tred+"&pyb="+stru(pubu)).read().decode("utf-8")
    if(t == "Ok!"):
        print("Thread created!")
        print("Waiting for friend's connection!")
        while gey != str(pubu):
            gey = urllib.request.urlopen(srv+"/ch/"+tred+"/pyb.txt").read().decode("utf-8")
        print("Key received!")
        pubf = gey
        msg1 = rsa.encrypt(msg, pubf)
        t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg1)).read().decode("utf-8")
        print("Message sent!")
else:
    t = urllib.request.urlopen(srv+"/ch/"+tred+"/pyb.txt").read().decode("utf-8")
    pubf = t
    print("Key received!")
    t = urllib.request.urlopen(srv+"/save.php?tred="+tred+"&pyb="+stru(pubu)).read().decode("utf-8")
    if(t == "Ok!"):
        print("Key sent!")
        t = urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
        msgf = rsa.decrypt(t, privu)
        print("First message from friend:", msgf)
while msg!="/end":
        print("\nNote: /end is an end of message\n")
        lastmsg = msg
        # init threads
        t1 = threading.Thread(target=writer, args=(serv, pubf))
        t2 = threading.Thread(target=reader, args=(serv, privu))

        # start threads
        t1.start()
        t2.start()
