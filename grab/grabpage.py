from website.BasePage import *
from selenium.webdriver.common.by import By
from website.startend import *
from function.write import *
from function.timetran import *

class grabpage(Page):
    url = ''
    status = "已结束"
    gameType_NBA = 'NBA'
    gameType_CBA = 'CBA'
    hupu = "https://m.hupu.com/nba/game"
    ttzb = "https://www.tiantianzhibo.com/lanqiuzhibo/"
    key_NBA = 'NBA &nbsp;&nbsp;&nbsp;'
    key_CBA = 'CBA &nbsp;&nbsp;&nbsp;'

    noneLink = '#'
    filePath = r'H:/python/BBB/file/'
    file_hupu = r'4.txt'
    file_tt_NBA = r'2.txt'
    sonFile_tt_NBA = r'page/'
    file_tt_CBA = r'6.txt'
    armHtmlLocal = r'H:/try project/NBAway/browser-homepage/'
    armFiles = r'H:/try project/NBAway/browser-homepage/page/live.html'
    armFile = r'page/live.html'
    armSonFiles = r'page/live/'
    armSonFile = r'live/'
    sonLocal = filePath + sonFile_tt_NBA
    armSonPath = filePath+armSonFiles
    armSonHtmlLocal = armHtmlLocal+armSonFiles
    list1 = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']
    list2 = ['a.txt','test','b.txt']

    sec_loc = (By.XPATH, '//*[@id="J_content"]/section[1]/a')
    test_loc = (By.XPATH, "/html/body/div[2]/div[3]/div[2]/*")
    NBA_loc = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/ul')

    def dealhupu(self):
        lists = self.find_elements(*self.sec_loc)
        writeIn = Write()
        for list in lists:
            gameStatus = list.find_element_by_class_name('match-status-txt').text
            if gameStatus == self.status:
                gameHreff = list.get_attribute("href")
                gameHref = gameHreff.replace('playbyplay','boxscore')
                gameName_home = list.find_element_by_class_name('home-team').text
                gameName_away = list.find_element_by_class_name('away-team').text
                gameScore = list.find_element_by_tag_name('strong').text
                gameResult = "<a href='"+ gameHref + "'>"+ gameName_away+ '&nbsp;&nbsp;'+gameScore+ '&nbsp;&nbsp;'+ gameName_home + '</a>'+'\n'
                writeIn.write_in(gameResult,self.filePath,self.file_hupu)

#gameType取比赛类型
#filePath抽取到数据的父目录
#file生成的数据文件
#sonFile子目录
    def dealttzb(self,gameType,filePath,file,sonFile):
        #定位到NBA，然后
        lists=self.find_elements(*self.test_loc)
        writeIn = Write()
        nTime = Trantime()
        k  = 1
        for list in lists:
            #print("%s" %list.text)
            if nTime.ttime() in list.text:
                break
            if nTime.ctime() in list.text:
                continue
            elif nTime.ytime() in list.text:
                continue
            else:
                game = list.find_element_by_class_name('t3').text
                #print("111%s" %game)
                if gameType == game:
                    times = list.find_element_by_class_name('t1').text
                    name = list.find_element_by_class_name('t4').text
                    link = list.find_element_by_class_name('t5')
                    linkA = link.find_elements_by_tag_name('a')
                    result = "<a href='" + self.armSonFile +gameType+ str(k) + r'.html' + "'>" + times + '&nbsp;&nbsp;&nbsp;' + name + '</a>' + '\n'
                    writeIn.write_in(result, filePath, file)

                    for ii in range(len(linkA)):
                        liveHref = linkA[ii].get_attribute("href")
                        liveTxt = linkA[ii].text
                        result = "<a href='" + liveHref + "'>" + liveTxt + '</a>' + '\n'
                        son = sonFile + gameType+str(k) +r'.txt'
                        writeIn.write_in(result, filePath, son)
                    armSon = filePath +self.armSonFiles +gameType+ str(k) + r'.html'
                    open(armSon, 'w')
                    k +=1

    #lists是目标html的数据抽取文件列表
    #local是抽取数据的位置
    #armTxtLocal生成的数据位置
    #armFilePath是目标子页面的路径
    #armSonHtmlLocal生成的HTML展示路径
    #逻辑：执行网页操作的时候，生成了每场比赛的txt，并为了后面整合统计，txt同级子目录下生成统计文件，方便后面处理个数
    #先对子页面目标文件夹进行了清空操作，临时TXT，临时统计文件都做了清空，每执行一类比赛网页爬取，需删除所有临时文件。
    def togetherson(self,gameType,lists,local,armTxtLocal,armFilePath,armSonHtmlLocal):
        for l in range(len(os.listdir(armFilePath))):
            armFile=armSonHtmlLocal +gameType+str(l+1)+ r'.html'
            for i in lists:
                if i =='test':
                    i = gameType+str(l+1)+r'.txt'
                    j = armTxtLocal + i
                else:
                    j = local + i
                with open(armFile, 'a', encoding='UTF-8') as f:
                    f.write(open(j, 'r', encoding='UTF-8').read() + '\n')

    def run_hupu(self):

        writes = Write()
        writes.write_clear(self.filePath, self.file_tt_NBA)
        writes.write_clear(self.filePath, self.file_tt_CBA)
        writes.write_clear(self.filePath, self.file_hupu)
        writes.write_clear(self.armHtmlLocal,self.armFile)
        writes.write_remove1(self.filePath,self.armSonFiles)
        writes.write_remove1(self.filePath, self.sonFile_tt_NBA)
        writes.write_remove1(self.armHtmlLocal, self.armSonFiles)
        '''页面处理'''
        self.open(self.hupu)
        self.dealhupu()
        self.open(self.ttzb)
        self.dealttzb(self.gameType_NBA, self.filePath, self.file_tt_NBA, self.sonFile_tt_NBA)
        self.togetherson(self.gameType_NBA,self.list2, self.filePath, self.sonLocal, self.armSonPath, self.armSonHtmlLocal)
        #清除刚刚生成的临时文件BBB下的和目标展示目录下的
        writes.write_remove1(self.filePath, self.armSonFiles)
        self.dealttzb(self.gameType_CBA, self.filePath, self.file_tt_CBA, self.sonFile_tt_NBA)
        self.togetherson(self.gameType_CBA, self.list2, self.filePath, self.sonLocal, self.armSonPath,self.armSonHtmlLocal)
        '''写入文件'''
        writes.together(self.list1, self.filePath, self.armFiles)
        writes.timeChange(self.armFiles,self.key_NBA)
        writes.timeChange(self.armFiles, self.key_CBA)


class test(StartEnd):
    print("start test  page")
    def test1(self):
        test = grabpage(self.driver)
        test.run_hupu()