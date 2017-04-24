import sys
import argparse
import os
import subprocess


def main():
    #--------------------------------------------------------------------------------------------------------
    #fill args
    try:
        m = argparse.ArgumentParser(description = "Trackmix", epilog = "Good listening!")
        m.add_argument('--source',     '-s', type=str,  required = True,  help = 'Source')
        m.add_argument('--destination','-d', type=str,  default  = None,  help = 'Output')
        m.add_argument('--count',      '-c', type=int,  default  = None,  help = 'How many files should i cut?')
        m.add_argument('--frame',      '-f', type=int,  default  = 10,    help = 'How long(sec)?')
        m.add_argument('--log',        '-l', action = 'store_true',       help = 'Should i log it?')
        m.add_argument('--extended',   '-e', action = 'store_true',       help = 'Little fade in/out')
    except:
        print('Input correct argument... ')
        
    source = m.parse_args().source
    destination = m.parse_args().destination
    if destination == None:
        destination = source
    count = m.parse_args().count
    frame = m.parse_args().frame
    
    
    #Log
    log = m.parse_args().log
    if log == True:
        log = ' -i '
        log = str(log)
    else:
        log = ' '
        log = str(log)
    
    

    fade = m.parse_args().extended
    justForFade = frame - 2
    justForFade = str(justForFade)
    if fade == True:        
        fadeStr = ' -ss 00:00:00 -t 00:00:'+str(frame)+'.00 -af \"afade=t=in:ss=0:d=2,afade=t=out:st='+justForFade+':d=2"\' -y '
        fadeStr = str(fadeStr)
    else:
        fadeStr = ''
        fadeStr = str(fadeStr)
    
    
    
    #Test source
    if os.path.exists(source) == True:
        #Path exist?
        files = os.listdir(source)
        fileName = os.listdir(source)
        
        files = [os.path.join(source, file) for file in files]
        files = [file for file in files if os.path.isfile(file)] #files only in list
        for i in range(len(files)):
            files[i] = '"'+files[i]+'"'
            #fileName[i] = '"'+fileName[i]+'"'
        pathToFfmeg = os.path.join(sys.path[0], r'ffmpeg-20170401-23ae3cc-win64-static\bin\ffmpeg.exe')#Path to ffmeg
        
     #--------------------------------------------------------------------------------------------------------
     #Start side process 'ffmpeg.exe' with params
		#CountParam = 1
        if count != None:
            for i in count:
                subprocess.call(pathToFfmeg+log+files[i]+' -acodec copy -ss 00:00:00 -t 00:00:'+str(frame)+'.00'+' "'+destination+'\\'+fileName[i]+'"',shell = True)
                if fade == True:
                    subprocess.call(pathToFfmeg+log+files[i]+fadeStr+'"'+destination+'\\'+fileName[i]+'"',shell = True)                   
        else:
            for i in range(len(files)):
                subprocess.call(pathToFfmeg+log+files[i]+' -acodec copy -ss 00:00:00 -t 00:00:'+str(frame)+'.00'+' "'+destination+'\\'+fileName[i]+'"',shell = True)
                if fade == True:
                    subprocess.call(pathToFfmeg+log+files[i]+fadeStr+'"'+destination+'\\'+fileName[i]+'"',shell = True)
    else:
        print('Wrong path!')
    
  
if __name__ == '__main__':
    main()