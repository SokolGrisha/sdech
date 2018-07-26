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
noname=input('Название канала?')
srv=input("Сервер где будет хранится канал?\n")
getcon=urllib.request.urlopen(srv+"/ch/"+noname+"/lenta.txt").read().decode("utf-8")
wp=urllib.request.urlopen(srv+"/ch/"+noname+"/key.txt").read().decode("utf-8")
wp=wp.split("(")[1].split(")")[0].split(", ")
for i in range(len(wp)):
    wp[i]=int(wp[i])
repri=rsa.PrivateKey(wp[0],wp[1],wp[2],wp[3],wp[4])
getcon=st2by(getcon)
getcon=getcon.split(b"-sdech-")
ans=""
for i in range(len(getcon)):
    try:
        print(rsa.decrypt(getcon[i],repri).decode()+"\n")
    except:
        print("Информация потерена, надеемся что это не пост, а резделитель")
print(ans)
