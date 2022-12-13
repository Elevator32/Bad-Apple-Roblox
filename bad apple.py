from PIL import Image
from time import sleep
import os
import re

frames = os.walk('./robloxcrashing')

modulescriptbeggining = ('local module = {')
modulescriptend = ('aaa\n}\nreturn module')

framedata = r'./FrameData'
currentnum = 1
currenttable = []
currenttablenum = 1

frame1 = Image.open('png2745.png')

def Return_VidInfo(Frame):
    frameData = list(Frame.getdata())
    return frameData
def makeTextFolder(frame, inputfortxt):
    tabletext = str(inputfortxt)
    file = open('./FrameData/'+str(frame)+'.txt', 'a')
    file = open('./FrameData/'+str(frame)+'.txt', 'r+')
    
    for num, framecodes in enumerate(inputfortxt):
        file.write('\n;'+str(num+1)+': = ')
        file.write(''+str(framecodes)+',')
    notreadlol = open('./FrameData/'+str(frame)+'.txt', 'r+')
    read = file.read()
    read = re.sub(', }', '}', read)
    file.write(read+modulescriptend)
    print('File Not fully converted... Please wait before closing.')
    return os.path.realpath(file.name)
def turntobinary(appletable):
    newtab = []
    for color in appletable:
        if color == (255,255,255):
            newtab.insert(1)
        if color == (0,0,0):
            newtab.insert(0)
        else:
            print(color)
    print(newtab)
    return newtab
def turntoluatable(file, filenumname):
    with open(file, 'r+') as f:
        text = f.read()
        text = re.sub('\(', '{', text)
        text = re.sub('\)', '}', text)
        text = re.sub('\[', '{', text)
        text = re.sub('\]', '}', text)
        text = re.sub('}{', '},{', text)
        text = re.sub(', }', '}', text)
        text = re.sub(',aaa', '', text)
        text = re.sub(';', '[', text)
        text = re.sub(':', ']', text)
        text = re.sub(',aaa', '', text)
        #text = f.seek(0)
        luatext = open('./luadata/'+str(filenumname)+'.txt', 'w')
        luatext.write(modulescriptbeggining+text)
        print('Finished Processing File! Safe To Exit Program!')
def getnum(number):
    num = str(number)
    if number < 10:
        return '0000'+num
    if number < 100 and number > 9:
        return "000"+num
    if number < 1000 and number > 99:
        return "00"+num
    if number < 10000 and number > 999:
        return "0"+num
    if number < 100000 and number > 9999:
        return number

frameTable = list(frame1.getdata())



for path, directories, frames1 in frames:
    if frames1:
        for num, framestrfail in enumerate(frames1):
            print('Frame'+str(num))
            nummy = int(((num+1)*4)+1)
            newnum = getnum(nummy)
            if nummy < 10421:
                print(newnum)
                framestr = 'png'+str(newnum)+'.png'
                frame = Image.open('./robloxcrashing/'+framestr)
                data = Return_VidInfo(frame)
                currenttable.insert(currenttablenum, data)
                currenttablenum += 1
                sleep(0.1)
                if num == currentnum*123123123123123123123:
                    currentnum += 1
                    textfile = makeTextFolder(num, currenttable)
                    currenttable = []
                    # print(open(textfile, 'r'))
                    turntoluatable(textfile, num)
            else:
                 break
        currentnum += 1
        textfile = makeTextFolder(num, currenttable)
        currenttable = []
        # print(open(textfile, 'r'))
        turntoluatable(textfile, num)
        print('all frames have been converted.')