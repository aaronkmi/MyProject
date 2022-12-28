
import PySimpleGUI as sg
import clipboard as CB
import os
import re
import json
import configparser

#config------------------
config = configparser.ConfigParser()
config['CON']={}
#초기값을 넣는 부분-한번만 할수 없을까??

config['CON']['engine_path']='D:\celestino_celestino-pc6_7188'
with open('config.ini','w',encoding='utf-8') as configfile:
    config.write(configfile)

config.read('config.ini', encoding='utf-8')
foldername = config['CON']['engine_path'] + '\LLL\LLL\Content\DataTable'
#-------------------------
text=''
text01=''
   
tablelist=[]
filepathlist=[]
dic={}
for (path, dir, files) in os.walk(foldername):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.json':
            tablelist.append(filename)
            dic[filename] = (path +"\\"+ filename)
print(f'ALL: {dic}\n')

dickeys=dic.keys()
totallist=''
jsonstring=''
jsonstringAll={}
for dict_data in dickeys:
    file_path = (dic[dict_data])
    filepathlist.append(file_path)
for file_path in filepathlist:    
    with open(file_path, 'r', encoding ='utf-8-sig') as json_file:
        json_data = json.load(json_file)
        jsonstring = str(json_data)
        print(type(jsonstring))
        print(file_path)
        jsonstringAll[file_path]=jsonstring

sg.theme()
layout = [[sg.Text('VfxAssetName',key='-InputID-',size=(80,1))],
          [sg.Text('jsonName',key='-InputID2-',size=(200,1))],
          [sg.Button("search")]
]
window = sg.Window('vfx asset find',layout)

countval=0
result_val=[]

while True:
    event, values = window.read()
   
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == "search" :
        print(jsonstringAll)
        text = CB.paste()
        text01=text.strip("Particlesystem")
        text01=text01.strip("NiagaraSystem")
        text01=text01.strip("MaterialInstanceConstant")
        text01=text01.strip("/'")
        window['-InputID-'].update(text01)
        for Allkey in jsonstringAll.keys():
            solutionM = re.search(text01, jsonstringAll[Allkey])
            print(f'serch:{solutionM}\n')
            if solutionM:
                print(f'존재함: {Allkey}')
                totallist = Allkey
                countval=countval+1
                result_val.append(Allkey)
                continue
                #break
            else:
                continue
        #-결과값 출력/초기화------------------------
        if result_val :
            window['-InputID2-'].update(result_val)
        else:
            window['-InputID2-'].update("No Result")
        print(result_val)
        result_val=[]              
        #------------------------------------------
       
        #break

window.close()

