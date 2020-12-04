import os
# os.mkdir("./dir01")
# os.getcwd() #: 현재위치
# os.chdir(./dir01) #: 디렉토리이동
# os.chdir(os.getcwd()+'/dir01')
print(os.getcwd())
# os.rmdir('dirname') #: 디렉토리삭제
# os.mkdir("./dir02")
# os.rmdir("./dir02") 

# os.path.exists(file_name) #: file 또는 directory 유무
print(os.path.exists('./test/hellow.py'))
# os.remove(file_name) #:파일삭제
os.remove('hellow.py')
