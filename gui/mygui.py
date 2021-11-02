from tkinter import*
from pytube import YouTube


root = Tk()

root.geometry="500 x 304"
root.config(bg='#856ff8')
root.minsize(500,500)
root.maxsize(500,300)
root.title("Youtube downloader")
root.iconbitmap(r'icon.ico')




Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold',bg='blue').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold',bg='yellow').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link,bg="grey").place(x = 32, y = 90)  

add='C:\Downloads'
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(add)
    Label(root, text = 'Downloded !!', font = 'arial 20').place(x= 180 , y = 210) 
    Label(root, text = 'Your download is saved at C:\Downloads' , font = 'arial 20').place(x= 0 , y = 210) 


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 4, command = Downloader).place(x=180 ,y = 150)




Label(root,text='copyright:RupeshIndustries',bg='#856ff8').place(x=160,y=300)


root.mainloop()