# -*- coding: utf-8 -*-
import requests 
import os
import os.path
from PIL import Image
import json
import os
import time
def IsValidImage(pathfile):
  bValid = True
  try:
    Image.open(pathfile).verify()
  except:
    bValid = False
  return bValid

def listName(rootDir):
	for lists in os.listdir(rootDir):
		path=os.path.join(rootDir,lists)
		
		time.sleep(1)
		if path==rootDir+'/.DS_Store':

			continue

		else:
			print path
			if IsValidImage(path):
				print "开始上传图片"
				# r=requests.post('http://121.40.213.47:8080/fileserver/createFileServlet?filepath=/test',files={path:open(path,'rb')})
				r=requests.post('http://192.168.60.50/file/UploadFile2.ashx',files={path:open(path,'rb')})

				# print r.text
				text = json.loads(r.text)
				# print text['ErrorCode']
				if text['ErrorCode']==0:
					print '上传成功'
					if os.path.exists(path):
	  					os.remove(path)
				else:
					print "failed"
			else:
				print "图片未完成"	
			
name = raw_input("请拖入照片文件夹,按回车键结束\n").strip()
# print name
# rootdir = "/Users/essios/Desktop/PIC/img" 
print '等待图片中...'
while 1:
	listName(name)

