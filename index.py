import rsa
import urllib.request
import requests

## end import and start def
def by2st(byt):
    ar=[]
    for i in range(len(byt)):
        ar.append(byt[i])
    ans=''
    for i in range(len(ar)):
        if(i!=len(ar)-1):
            ans+=str(ar[i])+","
        else:
            ans+=str(ar[i])
    return ans
def st2by(st):
    st=st.split(',')
    for i in range(len(st)):
        st[i]=int(st[i])
    return bytes(st)
def ed(srv,tred,msg):
    msg=by2st(msg)
    results = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+msg).read().decode("utf-8")
def cr(srv,tred,pub):
    results = requests.get(srv+"creat.php", params={'tred': tred, 'pub': str(pub)})
def stru(txt):
        txt=str(txt).split(",")[0].split("PublicKey(")[1]
        return txt
def rsu(txt):
        txt=rsa.PublicKey(int(txt),65537)
        return txt
## end def
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
                t = urllib.request.urlopen(srv+"/edit.php?tred="+tred+"&msg="+by2st(rsa.encrypt("PubHave".encode(), pubf))).read().decode("utf-8")
                print("Сообщили другу, что все ок!")
                nin=0
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
                                msgf=rsa.decrypt(st2by(t), privu).decode()
                        except:
                                msgf=msgf
                        i+=1
                print("Ключ доставлен")
        nin=1

print("")
print("Памятка: /end окнчание разговора, пустое сообщения - пререзагрузка(проверка на новые сообщения)")
print("")
if(nin==1):
    msgfr=msgf
    inp=msgfr
else:
    msgfr=""
    inp=msgfr
while True:
    try:
        inp=rsa.decrypt(st2by(inp), privu).decode()
        if(inp!=msgfr):
            print("f: "+inp)
    except:
        inp=inp
    my=input("msg:")
    if(my!=""):
        msgfr=my
        inp=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
        ed(srv,tred,rsa.encrypt(my.encode(),pubf))
    else:
        inp=urllib.request.urlopen(srv+"/ch/"+tred+"/msg.txt").read().decode("utf-8")
