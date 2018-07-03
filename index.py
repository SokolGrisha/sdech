def stru(txt):
        txt=str(txt).split(" ")[0]+str(txt).split(" ")[1]
        return txt
def rsu(txt):
        txt=str(txt).split(",")
        txt=txt[0]+", "+txt[1]
        return txt
import rsa
import urllib.request
global pubf
(pubu, privu) = rsa.newkeys(512)
print("Здраствуйте! Это sdech.py! Он нужен для соедниния с сервером, надеюсь у вас есть сервер на котром уже готово!")
srv=str(input("Сервер"))
cc=input("Create\Connect ? cr\co")
tred=input("Tred?")
msg=input("Ваше первое сообщение:")
if(cc=="cr"):
        t = urllib.request.urlopen(srv+"/creat.php?tred="+tred+"&pyb="+stru(pubu)).read().decode("utf-8")
        if(t=="Ok!"):
                print("Тред создан!")
                print("Ждем подключение друга!")
                while(gey!=str(pubu)):
                        gey=urllib.request.urlopen(srv+"/ch/"+tred+"/pyb.txt").read().decode("utf-8")
                print("Ключ получен!")
                pubf=gey
                msg1= rsa.encrypt(msg, pubf)
                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg1)).read().decode("utf-8")
                print("Сообщение отправлено!")
else:
        t = urllib.request.urlopen(srv+"/ch/"+tred+"/pyb.txt").read().decode("utf-8")
        pubf=t
        print("Ключ получен!")
        t = urllib.request.urlopen(srv+"/save.php?tred="+tred+"&pyb="+stru(pubu)).read().decode("utf-8")
        if(t=="Ok!"):
                print("Ключ отправлен!")
                t = urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
                msgf=rsa.decrypt(t, privu)
                print("Первое сообщение друга:"+msgf)
while msg!="/end":
        print("")
        print("Памятка: /end окнчание разговора")
        print("")
        lastmsg=msg
        import threading
        def writer(serv):
                global lastmsg
                while True:
                        import rsa
                        global pubf
                        msg = rsa.encrypt(input("msg:"), pubf)
                        t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+str(msg)).read().decode("utf-8")
                        lastmsg=msg
                        print(msg)
        def reader(serv):
                global lastmsg
                while True:
                        while msg!=lastmsg:
                                msg=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
                                import rsa
                                global pubu
                                global privu
                                msg = rsa.decrypt(t, privu)
                print(msg)
        # init threads
        t1 = threading.Thread(target=writer, args=(serv, pubf))
        t2 = threading.Thread(target=reader, args=(serv, privu))

        # start threads
        t1.start()
        t2.start()
