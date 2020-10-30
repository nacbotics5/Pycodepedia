import os,time
import shutil

path = ["/storage/emulated/0/"] #list of filepaths to crawl
escape = ["Android"] #list of folders to ignore

pathx = "/storage/emulated/0/Movies/"        

def prepare_paths(paths):
    for path in paths:
        for  root,dirs,files in os.walk(path):
            dirs = [i for i in dirs if not i.startswith(".")]
            dirs = [i for i in dirs if i not in escape]
            dirs = [path+"/%s/"%i for i in dirs]
            return(dirs)


def file_finder(paths,filetype=[".mp4",".avi",".mkv",".3gp"]):
    result = []
    for path in prepare_paths(paths):
        for root,dirs,files in os.walk(path):
            for name in files:
                if any([i for i in filetype if i in name]):
                    filename = f"{root}/{name}"
                    filesize = round(os.path.getsize(filename)/(1024*1024),0)
                    result.append((filename,filesize))
                else:pass
    return(result)

files = sorted(file_finder(path,filetype=["."]),key=lambda t: t[1],reverse=True)
print(len(files))

for i in files[3:10]:
    print(i)


for file in files[:5]:#copy and paste the top five Large files
    shutil.copy2(file[0],pathx)

