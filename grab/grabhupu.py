from website.BasePage import *
from selenium.webdriver.common.by import By
from website.startend import *
from function.write import *
from function.timetran import *

class hupu(Page):
    url = ''
    sec_loc = (By.XPATH,'//*[@id="J_content"]/section[1]/a')
    status = "已结束"

    linkPath = r'H:/python/BBB/file/4.txt'
    local = r"H:/python/BBB/file/"
    armFiles = r'H:/try project/NBAway/browser-homepage/page/live-test.html'

    def dealhupu(self):
        lists = self.find_elements(*self.sec_loc)
        writeIn = Write()
        writeIn.write_clear(self.linkPath)
        writeIn.write_clear(self.armFiles)
        for list in lists:
            gameStatus = list.find_element_by_class_name('match-status-txt').text
            if gameStatus == self.status:
                gameHreff = list.get_attribute("href")
                gameHref = gameHreff.replace('playbyplay','boxscore')
                gameName_home = list.find_element_by_class_name('home-team').text
                gameName_away = list.find_element_by_class_name('away-team').text
                gameScore = list.find_element_by_tag_name('strong').text
                gameResult = "<a href='"+ gameHref + "'>"+ gameName_away +gameScore+ gameName_home + '</a>'+'\n'
                writeIn.write_in(gameResult,self.linkPath)
        writeIn.together(self.local, self.armFiles)

    def run_hupu(self):
        self.open()
        self.dealhupu()

class huputest(StartEnd):
    print("start test hupu page")
    def test1(self):
        test = hupu(self.driver)
        test.run_hupu()