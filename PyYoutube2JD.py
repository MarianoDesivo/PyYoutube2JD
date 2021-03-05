import myjdapi
import time
import pyautogui

#connect to JDownloader

jd=myjdapi.Myjdapi()
jd.set_app_key("EXAMPLE")


pw='' #Password
mail= '' #User
device = '' #Write your device name, for example: 'JDownloader@MARIANO'

jd.connect(mail,pw)
device=jd.get_device(device) 
print('Connected')

lincs=myjdapi.myjdapi.Linkgrabber(device) #Linkgrabber object

fecha = time.ctime().replace(':',' ') #Date. I use it to name folders so I can track dates
downloads=device.downloads.query_links() #List of dictionaries of JD Downloads tab

##This function will get all the video links from a youtube account
def Obtenerlinks(url,youtuber):
       
   
    folder = r'C:\Users\MARIANO\\Downloads\Jdownloader\\'+ youtuber + '\\' + fecha #Name the folder you want to store files, I used Date as I said previously
    
    lincs.add_links([{
                          "autostart": False,
                          "links": url, #Youtube account link (see examples below)
                          "packageName": youtuber, #Name you want to call it, it will be used for the folder name
                          "extractPassword": None,
                          "priority": "DEFAULT",
                          "downloadPassword": None,
                          "destinationFolder": folder, 
                          "overwritePackagizerRules": True
                      }])
    #JD will show a pop-up window to ask if you want to get all the links
    pyautogui.click(626,408,1,0,'primary',3) #Try to click it with PyAutoGui
    pyautogui.press('enter') #Press enter if not clicked in the right place (click command is still useful to select JD's window and press enter correctly, you may want to correct coordinates)
    

#Start collecting links from this 3 Youtube accounts
Obtenerlinks('https://www.youtube.com/c/CiudadanoZ1984/videos','Ciudadano Z')
Obtenerlinks('https://www.youtube.com/c/mercurialdark1097/videos','Mercurialdark 10')
Obtenerlinks('https://www.youtube.com/c/ElViajeDelHorror/videos','DarkSoulHorror')
    
print('collecting...')
while(lincs.is_collecting()): #Wait while collecting links
    pass

linkList = lincs.query_links() #List of dictionaries with all links collected in Linkgrabber tab (you may want to clean it before collecting)
audios=[] #list of audio files
packageids=[]
linkids=[]
downloadfiles = [] #List of filenames in JD Downloads tab. It will be used to compare with Linkgrabber links, so you don't download files that you already have

for dic in downloads:
	downloadfiles.append(dic['name']) #Get filenames in JD Downloads tab

files=[] #List of files in Linkgrabber

for dic in linkList:
	files.append(dic['name']) #Get filenames in JD Linkgrabber tab

for dic in linkList:
    file = dic['name'] #Single filename in Linkgrabber link
    if file.endswith('aac') or file.endswith('m4a') or file.endswith('ogg'): #if file is an audiofile...
        if file not in downloadfiles: #if file is it not already downloaded
            audios.append(file) #Add it to audiofile list, to be downloaded
            packageids.append(dic.get('packageUUID')) #Package ID of the audio file
            linkids.append(dic.get('uuid')) #Link ID of the audio file
            



#Using package and link IDs of the files, you can add them to download list
lincs.move_to_downloadlist(linkids,packageids)


