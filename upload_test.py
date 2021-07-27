from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'sample.txt'})
f.SetContentString('Hello')
f.Upload()
