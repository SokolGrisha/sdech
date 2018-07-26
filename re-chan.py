import rsa
import urllib.request
import requests
import time

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
def stri(txt):
    enter=txt.split("PrivateKey(")[1].split(")")[0].split(", ")
    for i in range(len(enter)):
        enter[i]=int(enter[i])
    return enter
#InfOfChan
noname=input('Название канала?')
srv=input("Сервер где хранится канал?")
pas=input("Пароль?")
fmsg=input("Cообщение?\n:")
pse=input("Псевданим?")
wait=urllib.request.urlopen(srv+"/ch/"+noname+"/key.txt").read().decode("utf-8").split("(")[1].split(", ")[0]
pubu=rsa.PublicKey(int(wait),65537)
#Chan create at t:me
#-------------------
# msg
#___________________
#t:me auth
#-------------------
tc=time.ctime(time.time()).split(" ")[3]
msg="/n-------------------/n "+fmsg+" /n___________________/n "+tc+" "+pse+"/n"
msg=msg.split(" ")
for i in range(len(msg)):
    msg[i]=rsa.encrypt(msg[i].encode(),pubu)
amsg=b''
for i in range(len(msg)):
    if(i!=len(msg)-1):
        amsg+=msg[i]+b"-sdech-"
    elif(i==0):
        amsg+=b"-sdech-"
    else:
        amsg+=msg[i]
res=requests.get(srv+"rechan.php", params={'name': noname, 'pas': pas, 'msg':urllib.request.urlopen(srv+"ch/"+noname+"/lenta.txt").read().decode("utf-8")+","+by2st(amsg)})
print("Спасибо, все сохранено!")
