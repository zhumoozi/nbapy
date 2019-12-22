from datetime import date, timedelta
class Trantime():
    '''明天'''
    def ttime(self):
        tomorrow = date.today() + timedelta(days=1)
        newTime = tomorrow.strftime("%Y-%m*%d/")
        yNow=newTime.replace('-','年')
        mNow=yNow.replace('*', '月')
        now=mNow.replace('/', '日')
        #print('%s' %now)
        return now

    '''昨天'''
    def ytime(self):
        tomorrow = date.today() + timedelta(days=-1)
        newTime = tomorrow.strftime("%Y-%m*%d/")
        yNow=newTime.replace('-','年')
        mNow=yNow.replace('*', '月')
        now=mNow.replace('/', '日')
        #print('%s' %now)
        return now
    '''当前时间'''
    def ctime(self):
        tomorrow = date.today()
        newTime = tomorrow.strftime("%Y-%m*%d/")
        yNow = newTime.replace('-', '年')
        mNow = yNow.replace('*', '月')
        cNow = mNow.replace('/', '日')
        #print('%s' %cNow)
        return cNow
'''
if __name__ == '__main__':
    a=Trantime()
    a.ttime()
    a.ctime()
    a.ytime()
'''
