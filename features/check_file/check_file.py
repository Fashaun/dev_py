#!/usr/bin/python
# 不論輸入到 os.path.isfile() 的是檔案還是連結檔, 它也會回傳 TRUE. 
import os
file_path = "/var/www/html/test.html"
 
if ( os.path.isfile(file_path)):
    print("File exists!")
else:
    print("File not found!")
