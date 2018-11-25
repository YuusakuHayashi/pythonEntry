from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth(gauth)

drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()
for f in file_list:
    print(f['title'], f['id'])
