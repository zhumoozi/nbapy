from  time import sleep

class Page():

    def __init__(self,driver):
        self.driver = driver
        #self.base_url = "https://www.tiantianzhibo.com/lanqiuzhibo/"
        #self.base_url = ""
        self.timeout = 20

    def open(self,url):
       # url_ = self.base_url+url
        print ('Test page is:%s' %url)
        self.driver.maximize_window()
        self.driver.get(url)
        assert self.driver.current_url == url, 'Did ont land %s' %url

#    def open(self):
#        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def fine_xpath(self,xpath_):
        return self.driver.find_element_by_xpath(xpath_)

