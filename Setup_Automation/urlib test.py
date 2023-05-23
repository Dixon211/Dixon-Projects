import urllib.request
import os

url = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B800B74EF-7795-F0AA-85FC-9E54435DD80B%7D%26lang%3Den%26browser%3D5%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DRXQR%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'
file_name = 'Google_Chrome.exe'

urllib.request.urlretrieve(url, file_name)