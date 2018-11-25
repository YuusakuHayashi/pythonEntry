from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': 'TheBible.txt'})
f.SetContentString('賢い人に与えよ。彼はさらに賢くなる')
f.Upload()
