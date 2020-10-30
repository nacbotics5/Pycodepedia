import shutil

file_path = "/storage/emulated/0/qpython/"
file_dest = "/storage/emulated/0/qpython/"

#SHUTIL.COPYFILE
#shutil.copyfile(file_path+"files.txt",file_dest+"/copyfile/test.txt")


#SHUTIL.COPY
#using filename instead of directory
shutil.copy(file_path+'files.txt',file_dest+'copy/destination.txt')

#Using directory instead of filename
shutil.copy(file_path+'files.txt',file_dest+'copy/')



#SHUTIL.COPY2
#Using directory instead of filename
shutil.copy2(file_path+'files.txt',file_dest+'copy2/')

#using filename instead of directory
shutil.copy2(file_path+'files.txt', file_dest+'copy2/newfile.txt')


