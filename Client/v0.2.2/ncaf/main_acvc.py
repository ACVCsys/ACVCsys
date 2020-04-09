print("----------ACVAsys----------")
print("v.0.2.2")
print("[PLD]start import")
print("[PLD]loading filecmp")
import filecmp
print("[PLD] done")
print("[PLD]loading os")
import os
print("[PLD] done")
print("[PLD]loading wber")
import webbrowser
print("[PLD] done")
print("[PLD]loading tkinter.messagebox")
import tkinter.messagebox
print("[PLD] done")
print("[PLD]loading tkinter_moudles")
from tkinter import *
print("[PLD] done")
print("[PLD]loading urllib3")
import urllib3
print("[PLD] done")
print("[INFO]import over")
url1 = 'https://acvcsys.github.io/ACVCsys/README.md'
http = urllib3.PoolManager()
response = http.request('GET', url1)
print("[INFO]Pulling menu")
with open('newpulled.md', 'wb') as f:
    f.write(response.data)
print("[INFO]CMP now")
filenew_bol = filecmp.cmp("./newpulled.md","./pulled.md")
if(filenew_bol == 1 ) :
	print("[INFO]No new update")
	srcFile = './newpulled.md'
	dstFile = './pulled.md'
	os.remove("./pulled.md")
	print("[INFO]Delete file success")
	os.rename(srcFile,dstFile)
	print("[INFO]rename file success")

	
else:
	print("[ALERT] New update!")
	tkinter.messagebox.showinfo("ACVA System","检测到更新!")
	webbrowser.open("https://acvcsys.github.io/ACVCsys/")
	srcFile = './newpulled.md'
	dstFile = './pulled.md'
	os.remove("./pulled.md")
	print("[INFO]Delete file success")
	os.rename(srcFile,dstFile)
	print("[INFO]Rename file success")


url2 = 'https://acvcsys.github.io/ACVCsys/breaking0.acvam'
http = urllib3.PoolManager()
response = http.request('GET', url2)
print("[INFO]Pulling breaking")
with open('newpulled_breaking.acvam', 'wb') as f:
    f.write(response.data)
print("[INFO]CMP now")
filenew_bol = filecmp.cmp("./newpulled_breaking.acvam","./null_breaking.acvam")
if(filenew_bol == 1 ) :
	print("[INFO]No new breaking")
	print("[INFO]Exiting")
	
else:
	print("[INFO]BREAKING deced")
	os.remove("./new_breaking.txt")
	print("[INFO]Delete file success")
	srcFile = './newpulled_breaking.acvam'
	dstFile = './new_breaking.txt'
	os.rename(srcFile,dstFile)
	print("[INFO]Rename file success")
	print("[INFO]Starting pull humanish-files")
	url3 = 'https://acvcsys.github.io/ACVCsys/brkhumv0'
	http = urllib3.PoolManager()
	response = http.request('GET', url3)
	print("[INFO]Pulling brkhumv")
	with open('brkhumv.txt', 'wb') as f:
    		f.write(response.data)
	print("[INFO]Starting cmp")
	print("[INFO]CMP now")
	filenew_bol = filecmp.cmp("./brkhumv.txt","./pulled_brkhumv.txt")
	if (filenew_bol == 1):
		print("[INFO]No new update - breaking")
		srcFile = './brkhumv.txt'
		dstFile = './pulled_brkhumv.txt'
		os.remove("./pulled_brkhumv.txt")
		print("[INFO]Delete file success")
		os.rename(srcFile,dstFile)
		print("[INFO]rename file success")
		print("[INFO]Exiting")
	else :
		print("[ALERT]New update! - breaking")
		tkinter.messagebox.showwarning("ACVA System","检测到突发短讯更新!")
		srcFile = './brkhumv.txt'
		dstFile = './pulled_brkhumv.txt'
		os.remove("./pulled_brkhumv.txt")
		print("[INFO]Delete file success")
		os.rename(srcFile,dstFile)
		print("[INFO]Rename file success")
		print("[INFO]Starting Notepad")
		os.system("notepad pulled_brkhumv.txt")
		print("[INFO]Exiting")
print("----------ACVAsys----------")
	

