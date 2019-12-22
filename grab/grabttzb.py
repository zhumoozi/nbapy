from website.BasePage import *
from selenium.webdriver.common.by import By
from website.startend import *
from function.write import *
from function.timetran import *

class locweb(Page):
    url = ''
    gameType = 'NBA'
    live = "体育直播"
    noneLink = '#'
    linkPath = r'H:/python/BBB/file/2.txt'
    local = r"H:/python/BBB/file/"
    armFiles = r'H:/try project/NBAway/browser-homepage/page/live-test.html'

    test_loc = (By.XPATH,"/html/body/div[2]/div[3]/div[2]/*")
    NBA_loc = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/ul')

    def NBA(self):
        #定位到NBA，然后
        lists=self.find_elements(*self.test_loc)
        writeIn = Write()
        writeIn.write_clear(self.linkPath)
        writeIn.write_clear(self.armFiles)
        nTime = Trantime()
        for list in lists:
            #print("%s" %list.text)
            if nTime.ttime() in list.text:
                break
            if nTime.ctime() in list.text:
                continue
            else:
                game = list.find_element_by_class_name('t3').text
                #print("111%s" %game)
                if self.gameType == game:
                    times = list.find_element_by_class_name('t1').text
                    name = list.find_element_by_class_name('t4').text
                    link = list.find_element_by_class_name('t5')

                    if self.live in link.text:
                        liveLink = link.find_elements_by_tag_name('a')[0]
                        result = "<a href='" + liveLink.get_attribute("href") + "'>" + times + '&nbsp;&nbsp;&nbsp;' + name + '</a>' + '\n'
                        writeIn.write_in(result,self.linkPath)
                        #  print("%s %s %s" % (times, name, liveLink.get_attribute("href")))
                    else:
                        writeIn.write_in(times, name, self.noneLink,self.linkPath)
        writeIn.together(self.local,self.armFiles)

    def loc_action(self):
        self.open()
        self.NBA()


class loctest(StartEnd):
    def test1(self):
        print("start test")
        po=locweb(self.driver)
        po.loc_action()