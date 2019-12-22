from datetime import date
import os
class Write():
    def write_in(self,result,linkPath,file):
    #    result = times +' '+ names +' '+links +'\n'
    #    result = "<a href='"+ links + "'>"+ times +'&nbsp;&nbsp;&nbsp;'+ names + '</a>'+'\n'
        path = linkPath +file
        f = open(path,'a',encoding='UTF-8')
        f.write(result)
        f.close()

    def write_clear(self,linkPath,file=''):
        path = linkPath + file
        f = open(path, 'a', encoding='UTF-8')
        f.seek(0)
        f.truncate()

    def write_remove(self,linkPath,sonPath = ''):
        path_data = linkPath+sonPath
        for i in os.listdir(path_data):
            file_data = path_data + "\\" + i
            if os.path.isfile(file_data) == True:
                os.remove(file_data)

    def write_remove1(self,linkPath,sonPath = ''):
        path_data = linkPath+sonPath
        filelist = os.listdir(path_data)
        for f in filelist:
            filepath = os.path.join(path_data, f)  # 将文件名映射成绝对路劲
            if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
                os.remove(filepath)

    def together(self,lists,local,armfile):
        for i in lists:
            j = local + i
            with open(armfile, 'a', encoding='UTF-8') as f:
                f.write(open(j, 'r', encoding='UTF-8').read() + '\n')

    def timeChange(self,files,keywords):
        tomorrow = date.today()
        Time = tomorrow.strftime("%Y-%m-%d")
        f = open(files, 'r', encoding='UTF-8')
        content = f.read()
        post = content.find(keywords)
      #  print(len(keywords))
        if post != -1:
            content = content[:post + len(keywords)] + Time + content[post + len(keywords):]
            file = open(files, 'w',encoding='UTF-8')
            file.write(content)
        f.close()
'''
if __name__=='__main__':
   # linkPath = r'H:/python/BBB/file/2.txt'
   # local = r"H:/python/BBB/file/"
   # armFiles = r'H:/python/BBB/live.html'
    a= ''
    linkPath_tt_NBA = r'H:/python/BBB/file/'
    files = r'2.txt'
    test = Write()
    test.write_in(a,linkPath_tt_NBA,files)

'''