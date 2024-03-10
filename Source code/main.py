import time
from getpass import getpass
import os
import requests
#Made by IDname 
#DC: IDname

print('Version 1')
print('█▀█ █▀█ █▀█ ▀▄▀ █▄█   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█   █░█ ▄█')
print('█▀▀ █▀▄ █▄█ █░█ ░█░   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄   ▀▄▀ ░█')


#Default settings
anonymity= 'elite'
ProxyRequestoutputsave = 'y'
Proxyregion = 'all'
ProxyTimeout = 100
ProxyProtocol= 'http'

#Options
print('Recommended: de, en , pl , fr , be , in , it , hr , at , se, rs , es , to , tr , all')
print('There are many more. Just use the ISO-3166-1 standard')
Proxyregion = input ('Which Region do you want to use ? (Enter to use all)')
print('')
print('Recommended: 100 Curently:',ProxyTimeout)
ProxyTimeout = input ('What should be the Proxy timeout ? Enter to use Recommended')
print('')
print('Aviable: http , socks4 , socks5')
ProxyProtocol = input('Which Protocol do you want to use ? Enter to use http')
print('Checking Aviable Proxies ...')

#Request
ProxyAviable = requests.get('https://api.proxyscrape.com/v2/?request=proxyinfo&simplified=true')
ProxyRequestURL = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol='+ProxyProtocol+'&timeout='+ProxyTimeout+'&country='+Proxyregion+'&ssl=all&anonymity='+anonymity+''
API_Data = ProxyAviable.json()
for key in API_Data:{
    print(key,":", API_Data[key])
    }
ProxyRequestoutput = requests.get(ProxyRequestURL)

#Display Results
print('Protocol:'+ProxyProtocol+' | Timeout:'+ProxyTimeout+' | Country: '+ Proxyregion +' | Anonymity: Elite' )
time.sleep(1.0)
if ProxyRequestoutput.text == '':
         print('No Proxies aviable')
         print('Try a higher Proxy Timeout')
else:
         print(ProxyRequestoutput.text)
         ProxyRequestoutputsave = input ("Do you want to save these result's to a file ? y/n")
          #Save Result
         if ProxyRequestoutputsave == 'y':
          with open("ProxyRequestoutput.txt", "w") as f: 
               f.write(ProxyRequestoutput.text)
         else:
                print('')
# Exit ASK                
ExitASK = input("Do you want to restart ? y/n")
if ExitASK == ('y'):
       os.system('cmd /k python main.py')
else:
        print('Exit in 3s')
        time.sleep(1.0)
        print('Exit in 2s')
        time.sleep(1.0)
        print('Exit in 1s')
        time.sleep(1.0)
        os.system('exit')
