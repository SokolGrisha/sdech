import rsa
import urllib.request
import threading
## end import and start def
def stru(txt):
        txt=str(txt).split(",")[0].split("PublicKey(")[1]
        return txt
def rsu(txt):
        txt=rsa.PublicKey(int(txt),65537)
        return txt
def writer(srv):
        global lastmsg
        while True:
                import rsa
                global pubf
                msg = rsa.encrypt(input("msg:"), pubf)
                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg)).read().decode("utf-8")
                lastmsg=msg
                print(msg)
def reader(srv):
        global lastmsg
        while True:
                while msg!=lastmsg:
                        msg=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
                        import rsa
                        global pubu
                        global privu
                        msg = rsa.decrypt(t, privu)
        print(msg)
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
                pubf=wait
                msg1= rsa.encrypt("PubHave".encode(), pubf)
                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg1)).read().decode("utf-8")
                print("Сообщили другу, что все ок!")
else:
        t = urllib.request.urlopen(srv+"/ch/"+tred+"/pub.txt").read().decode("utf-8")
        pubf=rsa.PublickKey(int(t),65537)
        print("Ключ получен!")
        t = urllib.request.urlopen(srv+"/save.php?tred="+tred+"&pub="+stru(pubu)).read().decode("utf-8")
        if(t=="Ok!"):
                print("Ключ отправлен!")
                t = urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
                msgf=rsa.decrypt(t, privu).decode()
                if(msgf=="PubHave"):
                	print("Ключ доставлен")
# init threads
t1 = threading.Thread(target=writer, args=(srv, pubf))
t2 = threading.Thread(target=reader, args=(srv, privu))

print("")
print("Памятка: /end окнчание разговора")
print("")

# start threads
t1.start()
t2.start()

msg="Start!!"
while msg!="/end":
        lastmsg=msg
