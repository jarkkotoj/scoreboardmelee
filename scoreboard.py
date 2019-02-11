from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def addone(var) :
    var.set(int(var.get())+1)

def subone(var) :
    var.set(int(var.get())-1)

def getdir() :
    global dirname
    aux = filedialog.askdirectory()
    if (aux is None) :
        return 0
    dirname = aux+"/"
    try :
        p1f = open(dirname+"P1.txt","r")
        p1name.set(p1f.read())
        p1f.close()
    except :
        p1f = open(dirname+"P1.txt","w+")
        p1f.write(p1name.get())
        p1f.close()

    try :
        p2f = open(dirname+"P2.txt","r")
        p2name.set(p2f.read())
        p2f.close()
    except :
        p2f = open(dirname+"P2.txt","w+")
        p2f.write(p2name.get())
        p2f.close()

    try :
        p2sf = open(dirname+"scrP2.txt","r")
        p2score.set(str(int(p2sf.read())))
        p2sf.close()
    except :
        p2sf = open(dirname+"scrP2.txt","w+")
        p2sf.write(p2score.get())
        p2sf.close()

    try :
        p1sf = open(dirname+"scrP1.txt","r")
        p1score.set(str(int(p1sf.read())))
        p1sf.close()
    except :
        p1sf = open(dirname+"scrP1.txt","w+")
        p1sf.write(p1score.get())
        p1sf.close()

    try :
        labelf = open(dirname+"label.txt","r")
        labeltxt.set(labelf.read())
        labelf.close()
    except :
        labelf = open(dirname+"label.txt","w+")
        labelf.write(labeltxt.get())
        labelf.close()

    try :
        miscf = open(dirname+"misc.txt","r")
        misctxt.set(miscf.read())
        miscf.close()
    except :
        miscf = open(dirname+"misc.txt","w+")
        miscf.write(misctxt.get())
        miscf.close()
    return 1

def updatefile() :
    if (dirname == "" or dirname == "/") :
        if (0==getdir()) :
            return 0
    p1f = open(dirname+"P1.txt","w+")
    p1f.write(p1name.get())
    p1f.close()

    p2f = open(dirname+"P2.txt","w+")
    p2f.write(p2name.get())
    p2f.close()
    
    p2sf = open(dirname+"scrP2.txt","w+")
    p2sf.write(p2score.get())
    p2sf.close()

    p1sf = open(dirname+"scrP1.txt","w+")
    p1sf.write(p1score.get())
    p1sf.close()

    labelf = open(dirname+"label.txt","w+")
    labelf.write(labeltxt.get())
    labelf.close()

    miscf = open(dirname+"misc.txt","w+")
    miscf.write(misctxt.get())
    miscf.close()

    p1icon.write(dirname+"p1icon.png", format = "png")
    p2icon.write(dirname+"p2icon.png", format = "png")
    return 1

def reset() :
    p1name.set("")
    p2name.set("")
    p1score.set("0")
    p2score.set("0")
    p1char.set("-")
    p2char.set("-")
    updatecolors(1)
    updatecolors(2)
    loadicon((colorlist[p1char.get()])[p1col.get()],1)
    loadicon((colorlist[p2char.get()])[p2col.get()],2)

def getcolors(dictitem) :
    clist = list(dictitem.keys())
    return clist

#see below for use >_>
def dummyfun(value,ind) :
    if (ind == 1) :
        p1col.set(value)
        loadicon((colorlist[p1char.get()])[value],ind)
    elif (ind ==2 ):
        p2col.set(value)
        loadicon((colorlist[p2char.get()])[value],ind)

def updatecolors(ind) : 
    if (ind==1):
        menu = col1menu.children["menu"]
        menu.delete(0,"end")
        p1col.set("neutral")
        for value in list(colorlist[p1char.get()]) :
            menu.add_command(label=value, command = lambda v=value: dummyfun(v,ind) )
        p1col.set("neutral")
    else :
        menu = col2menu.children["menu"]
        menu.delete(0,"end")
        p2col.set("neutral")
        for value in list(colorlist[p2char.get()]) :
            menu.add_command(label=value, command = lambda v=value: dummyfun(v,ind) )
        p2col.set("neutral")

def loadicon(filename,ind) :
    global p1icon
    global p2icon
    filepath=dir_path+"icons/"+filename
    if (ind==1) :
        p1icon = PhotoImage(file=filepath)
        p1iconlabel.configure( image= p1icon)
    else :
        p2icon = PhotoImage(file=filepath)
        p2iconlabel.configure(image = p2icon)

characterlist = ('-', 'Bowser','Captain Falcon', 'Donkey Kong', 'Dr. Mario', 'Falco', 'Fox', 'Ganondorf', 'Mr. Game&Watch', 'Ice Climbers', 'Jigglypuff', 'Kirby', 'Link', 'Luigi', 'Mario', 'Marth', 'Mewtwo', 'Ness', 'Peach', 'Pichu', 'Pikachu', 'Roy','Samus', 'Sheik', 'Yoshi', 'Young Link', 'Zelda')
colorlist={'-':{'neutral':'empty.png'},'Bowser':{'black':'Bowser_black.png','blue':'Bowser_blue.png','neutral':'Bowser_neutral.png','red':'Bowser_red.png'},'Captain Falcon':{'black':'CaptainFalcon_black.png','blue':'CaptainFalcon_blue.png','green':'CaptainFalcon_green.png','neutral':'CaptainFalcon_neutral.png','red':'CaptainFalcon_red.png','white':'CaptainFalcon_white.png'}, 'Donkey Kong':{'black':'DonkeyKong_black.png','blue':'DonkeyKong_blue.png','green':'DonkeyKong_green.png','neutral':'DonkeyKong_neutral.png','red':'DonkeyKong_red.png'}, 'Dr. Mario':{'black':'DrMario_black.png','blue':'DrMario_blue.png','green':'DrMario_green.png','neutral':'DrMario_neutral.png','red':'DrMario_red.png'}, 'Falco':{'blue':'Falco_blue.png','green':'Falco_green.png','neutral':'Falco_neutral.png','red':'Falco_red.png'}, 'Fox':{'blue':'Fox_blue.png','green':'Fox_green.png','neutral':'Fox_neutral.png','red':'Fox_red.png'}, 'Ganondorf':{'blue':'Ganondorf_blue.png','green':'Ganondorf_green.png','neutral':'Ganondorf_neutral.png','purple':'Ganondorf_purple.png','red':'Ganondorf_red.png'}, 'Ice Climbers':{'green':'IceClimbers_green.png','neutral':'IceClimbers_neutral.png','orange':'IceClimbers_orange.png','red':'IceClimbers_red.png'}, 'Jigglypuff':{'blue':'Jigglypuff_blue.png','crown':'Jigglypuff_crown.png','green':'Jigglypuff_green.png','neutral':'Jigglypuff_neutral.png','red':'Jigglypuff_red.png'}, 'Kirby':{'blue':'Kirby_blue.png','green':'Kirby_green.png','neutral':'Kirby_neutral.png','red':'Kirby_red.png','white':'Kirby_white.png','yellow':'Kirby_yellow.png'}, 'Link':{'black':'Link_black.png','blue':'Link_blue.png','neutral':'Link_neutral.png','red':'Link_red.png','white':'Link_white.png'}, 'Luigi':{'blue':'Luigi_blue.png','neutral':'Luigi_neutral.png','pink':'Luigi_pink.png','white':'Luigi_white.png'}, 'Mario':{'blue':'Mario_blue.png','brown':'Mario_brown.png','green':'Mario_green.png','neutral':'Mario_neutral.png','yellow':'Mario_yellow.png'}, 'Marth':{'black':'Marth_black.png','green':'Marth_green.png','neutral':'Marth_neutral.png','red':'Marth_red.png','white':'Marth_white.png'}, 'Mewtwo':{'blue':'Mewtwo_blue.png','green':'Mewtwo_green.png','neutral':'Mewtwo_neutral.png','red':'Mewtwo_red.png'}, 'Mr. Game&Watch':{'blue':'MrGameWatch_blue.png','green':'MrGameWatch_green.png','neutral':'MrGameWatch_neutral.png','red':'MrGameWatch_red.png'}, 'Ness':{'blue':'Ness_blue.png','green':'Ness_green.png','neutral':'Ness_neutral.png','yellow':'Ness_yellow.png'}, 'Peach':{'blue':'Peach_blue.png','daisy':'Peach_daisy.png','green':'Peach_green.png','neutral':'Peach_neutral.png','white':'Peach_white.png'}, 'Pichu':{'blue':'Pichu_blue.png','green':'Pichu_green.png','neutral':'Pichu_neutral.png','red':'Pichu_red.png'}, 'Pikachu':{'blue':'Pikachu_blue.png','green':'Pikachu_green.png','neutral':'Pikachu_neutral.png','red':'Pikachu_red.png'}, 'Roy':{'blue':'Roy_blue.png','green':'Roy_green.png','neutral':'Roy_neutral.png','red':'Roy_red.png','yellow':'Roy_yellow.png'}, 'Samus':{'black':'Samus_black.png','blue':'Samus_blue.png','green':'Samus_green.png','neutral':'Samus_neutral.png','red':'Samus_red.png'}, 'Sheik':{'blue':'Sheik_blue.png','green':'Sheik_green.png','neutral':'Sheik_neutral.png','red':'Sheik_red.png','white':'Sheik_white.png'}, 'Yoshi':{'blue':'Yoshi_blue.png','cyan':'Yoshi_cyan.png','neutral':'Yoshi_neutral.png','pink':'Yoshi_pink.png','red':'Yoshi_red.png','yellow':'Yoshi_yellow.png'}, 'Young Link':{'black':'YoungLink_black.png','blue':'YoungLink_blue.png','neutral':'YoungLink_neutral.png','red':'YoungLink_red.png','white':'YoungLink_white.png'}, 'Zelda':{'blue':'Zelda_blue.png','green':'Zelda_green.png','neutral':'Zelda_neutral.png','red':'Zelda_red.png','white':'Zelda_white.png'}}

dir_path = os.path.dirname(os.path.realpath(__file__)) #Directory address of scoreboard.py
if (dir_path[-1]!='/'):
    dir_path = dir_path+'/'

root = Tk()
root.title("Score Board Melee")
mainframe = ttk.Frame(root, padding="3 3 12 12")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(4,weight=4)
mainframe.columnconfigure(3,weight=1)
mainframe.columnconfigure(5,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(6,weight=1)
mainframe.columnconfigure(7,weight=1)


mainframe.rowconfigure(4,weight=1)
#root.grid_columnconfigure(4,weight=1)
#root.grid_rowconfigure(4,weight=1)
#root.grid_columnconfigure(2,weight=1)
#root.grid_columnconfigure(6,weight=1)

p1name = StringVar()
p2name = StringVar()
p1score = StringVar()
p2score = StringVar()
labeltxt = StringVar()
misctxt = StringVar()
p1icon = PhotoImage(file=dir_path+"icons/empty.png")
p2icon = PhotoImage(file=dir_path+"icons/empty.png")

p1name.set("p1")
p2name.set("p2")
p1score.set(0)
p2score.set(0)


p1n_entry = ttk.Entry(mainframe, width=12, textvariable=p1name)
p1n_entry.grid(column=1, row=1, columnspan=3, sticky=(W,E))

p2n_entry = ttk.Entry(mainframe, width=12, textvariable=p2name)
p2n_entry.grid(column=5, row=1,columnspan=3, sticky=(W,E))

btp1p=ttk.Button(mainframe, text="+", command=lambda *args: addone(p1score))
btp1p.grid(row=2, column=3)
btp1m=ttk.Button(mainframe, text="-", command=lambda *args: subone(p1score))
btp1m.grid(row=2, column=1)
ttk.Label(mainframe, textvariable=p1score).grid(row=2,column=2)

btp2p=ttk.Button(mainframe, text="+", command=lambda *args: addone(p2score))
btp2p.grid(row=2,column=7)
btp2m=ttk.Button(mainframe, text="-", command=lambda *args: subone(p2score))
btp2m.grid(row=2,column=5)
ttk.Label(mainframe, textvariable=p2score).grid(row=2,column=6)

p1char = StringVar()
p2char = StringVar()
p1char.set('-')
p2char.set('-')
p1col = StringVar()
p2col = StringVar()
p1col.set('neutral')
p2col.set('neutral')

p1iconlabel = Label(mainframe, image = p1icon)
p1iconlabel.grid(row=3, column=3,sticky=(W,E))
p2iconlabel = Label(mainframe, image = p2icon)
p2iconlabel.grid(row=3, column=7,sticky=(W,E))

col1menu=OptionMenu(mainframe, p1col, *(getcolors(colorlist[p1char.get()])), command = lambda *args : print((colorlist[p1char.get()])[p1col.get()]))
col1menu.grid(row=3, column=2,sticky=(W,E))

col2menu=OptionMenu(mainframe, p2col, *(getcolors(colorlist[p2char.get()])), command = lambda *args : loadicon((colorlist[p2char.get()])[p2col.get()],2))
col2menu.grid(row=3, column=6,sticky=(W,E))


ttk.OptionMenu(mainframe, p2char, *characterlist, command = lambda *args: updatecolors(2)).grid(row=3, column=5)
ttk.OptionMenu(mainframe, p1char, *characterlist, command = lambda *args: updatecolors(1)).grid(row=3, column=1)


ttk.Label(mainframe,text="Label").grid(row=5,column=1)
ttk.Label(mainframe,text="Misc").grid(row=6,column=1)
label_entry=ttk.Entry(mainframe, width=14, textvariable=labeltxt).grid(row=5,column=2,columnspan=2,sticky=(W,E))
misc_entry=ttk.Entry(mainframe, width=14, textvariable=misctxt).grid(row=6,column=2,columnspan=2,sticky=(W,E))

updatebutton=Button(mainframe, text="Update",command= updatefile)
updatebutton.grid(row=7, column=2, rowspan=3, columnspan=2)
updatebutton.config(height=5,width=15)
dirname=""
ttk.Button(mainframe, text="Set Directory", command = getdir).grid(row=10,column=1)
ttk.Button(mainframe, text="Reset", command = reset).grid(row=10, column=3)
#ttk.Button(mainframe, text="Reset", command = lambda *args : print(getcolors(colorlist[p1char.get()]))).grid(row=10, column=3)



#Add some padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
