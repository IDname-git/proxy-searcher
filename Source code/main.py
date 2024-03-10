import time
from getpass import getpass
import os
import requests
#Made by IDname 
#DC: IDname

print('Version 1.1 Made by IDname')
print('█▀█ █▀█ █▀█ ▀▄▀ █▄█   █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀ █▀█   █░█ ▄█')
print('█▀▀ █▀▄ █▄█ █░█ ░█░   ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄ █▀▄   ▀▄▀ ░█')


#Default settings
ProxyAnonymity= 'elite'
ProxyRequestoutputsave = 'y'
Proxyregion = 'all'
ProxyTimeout = 100
ProxyProtocol= 'http'
inputxt ='>>>'
ExitASK = 'y'
#Options
print('Recommended: de, en , pl , fr , be , in , it , hr , at , se, rs , es , to , tr , all')
print('There are many more. Just use the ISO-3166-1 standard')
print('Which Region do you want to use ? Enter to use all')
Proxyregion = input (inputxt)
if Proxyregion =='':
       Proxyregion='all'
print('')
print('Recommended: 100 Curently:',ProxyTimeout)
print('What should be the Proxy timeout ? Enter to use 100 (Recommended)')
ProxyTimeout = input (inputxt)
if ProxyTimeout == '':
       ProxyTimeout = '100'
print('')
print('Aviable: http , socks4 , socks5')
print('Which Protocol do you want to use ? Enter to use http')
ProxyProtocol = input(inputxt)
if ProxyProtocol =='':
       ProxyProtocol = 'http'
print('')
print('Aviable: elite , anonymous , transparent or all')
print('Which Anonymity do you want to use ? Enter for elite (Recommended)')
ProxyAnonymity = input(inputxt)
if ProxyAnonymity == '':
       ProxyAnonymity ='elite'
print('')
print('Checking Aviable Proxies ...')

#Request
ProxyAviable = requests.get('https://api.proxyscrape.com/v2/?request=proxyinfo&simplified=true')
ProxyRequestURL = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol='+ProxyProtocol+'&timeout='+ProxyTimeout+'&country='+Proxyregion+'&ssl=all&anonymity='+ProxyAnonymity+''
API_Data = ProxyAviable.json()
for key in API_Data:{
    print(key,":", API_Data[key])
    }
ProxyRequestoutput = requests.get(ProxyRequestURL)

#Display Results
print('Protocol:'+ProxyProtocol+' | Timeout:'+ProxyTimeout+' | Country: '+ Proxyregion +' | Anonymity: '+ProxyAnonymity+'' )
time.sleep(1.5)
if ProxyRequestoutput.text == '':
         print('No Proxies aviable or Wrong input')
         print('Try a higher Proxy Timeout')
else:
         print(ProxyRequestoutput.text)
         ProxyRequestoutputsave = input ("Do you want to save these result's to a file ? y/n")
          #Save Result
         if ProxyRequestoutputsave == 'y':
          with open("Proxyresult.txt", "w") as f: 
               f.write(ProxyRequestoutput.text)
         else:
                print('')

print('To exit hit three times Enter')
ExitASK = input("3")
ExitASK = input("2")
ExitASK = input("1")                     
