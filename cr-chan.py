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
(pubu, pri) = rsa.newkeys(512)
noname=input('Название канала?')
srv=input("Сервер где будет хранится канал?")
pas=input("Пароль?")
fmsg=input("Первое сообщение?\n:")
pse=input("Псевданим?")
#Chan create at t:me
#-------------------
# msg
#___________________
#t:me auth
#-------------------
tc=time.ctime(time.time()).split(" ")[3]
msg="Chan create at "+time.ctime(time.time())+"/n-------------------/n "+fmsg+"/n___________________/n"+tc+" "+pse+"/n"
msg=msg.split("/n")
for i in range(len(msg)):
    msg[i]=rsa.encrypt(msg[i].encode(),pubu)
amsg=b''
for i in range(len(msg)):
    if(i!=len(msg)-1):
        amsg+=msg[i]+b"-sdech-"
    else:
        amsg+=msg[i]
res=requests.get(srv+"crchan.php", params={'name': noname, 'pas': pas, 'msg':by2st(amsg),'pri': pri})
f = open(noname+'_chan.txt', 'w')
f.write(str(pubu))
print("Публичный ключ сохранен! (не волнуйтесь если он потеряется, он сохрянень для вашей подстраховки)"+noname+'_chan.txt')
f.close()
print("Спасибо, все сохранено!")
