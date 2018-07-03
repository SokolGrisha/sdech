import rsa
import urllib.request
## end import and start def
def stru(txt):
        txt=str(txt).split(",")[0].split("PublicKey(")[1]
        return txt
def rsu(txt):
        txt=rsa.PublicKey(int(txt),65537)
        return txt
#def writer(srv):
#        global lastmsg
#        while True:
#                import rsa
#                global pubf
#                msg = rsa.encrypt(input("msg:"), pubf)
#                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg)).read().decode("utf-8")
#                lastmsg=msg
#                print(msg)
#def reader(srv):
#        global lastmsg
#        while True:
#                while msg!=lastmsg:
#                        msg=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
#                        import rsa
#                        global pubu
#                        global privu
#                        msg = rsa.decrypt(t, privu)
#        print(msg)
## end def and start code
global pubf #PublicKey you freind
(pubu, privu) = rsa.newkeys(512)#create keys
print("Здраствуйте! Это sdech.py! Он нужен для соедниния с сервером, надеюсь у вас есть сервер на котром уже готово!")
srv=str(input("Сервер"))#Server
cc=input("Create\Connect ? cr\co")
tred=input("Tred?")#chat
if(cc=="cr"):
        t = urllib.request.urlopen(srv+"/creat.php?tred="+tred+"&pub="+stru(pubu)).read().decode("utf-8")
        if(t=="Ok!"):
                print("Тред создан!")
                print("Ждем подключение друга!")
                wait=stru(pubu)
                while(wait==stru(pubu)):
                        wait=urllib.request.urlopen(srv+"/ch/"+tred+"/pub.txt").read().decode("utf-8")
                print("Ключ получен!")
                pubf=rsa.PublicKey(int(wait),65537)
                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(rsa.encrypt("PubHave".encode(), pubf))).read().decode("utf-8")
                print("Сообщили другу, что все ок!")
else:
        t = urllib.request.urlopen(srv+"/ch/"+tred+"/pub.txt").read().decode("utf-8")
        pubf=rsa.PublicKey(int(t),65537)
        print("Ключ получен!")
        t = urllib.request.urlopen(srv+"/save.php?tred="+tred+"&pub="+stru(pubu)).read().decode("utf-8")
        if(t=="Ok!"):
                print("Ключ отправлен!")
                i=0;
                msgf="Start!"
                while msgf!="PubHave":
                        try:
                                t = urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
                        except:
                                if i%100:
                                        print("Ждем подключение!")
                        try:
                                msgf=rsa.decrypt(t.encode(), privu)
                        except:
                                msgf=msgf
                        i+=1
                print("Ключ доставлен")

print("")
print("Памятка: /end окнчание разговора")
print("")

lm=t;
msg="Start!!"
while msg!="/end":
        msgf=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
        try:
                msgf= rsa.decrypt(msgf.encode(), privu)
                print(msgf)
        except:
                msg=msg
        msg = rsa.encrypt(input("msg").encode(), pubf)
        t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg)).read().decode("utf-8")
