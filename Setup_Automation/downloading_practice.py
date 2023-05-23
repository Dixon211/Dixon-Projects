import requests
import subprocess
import os

#change the download location folder here
dest_fold= r'C:\test_file'

#checks for folder location and creates it
def create_folder(dest_fold):
    if os.path.exists(dest_fold): #r here allows for forward slash in the string, it means raw
        print("file exists\n")
        pass
    else:
        os.makedirs(dest_fold)
        print('file created\n')

#downloads the program and silent installs it
def download_program(url, file_name):
    response = requests.get(url)
    file_path = os.path.join(dest_fold,file_name)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return_text = 'Successfully downloaded file\n'
    else:
        return_text = 'Failed to download file\n'
    print(return_text)

    command = f"{file_path} /silent /install"
    subprocess.call(command, shell=True)



create_folder(dest_fold)
#input for download_program ('<filepath>', '<filename.filetype>')
download_program('https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B1BBACB4A-EB3F-5FCA-F166-E0BE481B6DC2%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DJSBI%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe', "Google_Chrome.exe")
