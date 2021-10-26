from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import requests
import time

#动车系列：D1：商务座， D2：一等座，D3：二等座，D4：无座
#普通火车：K1：软卧，K2：硬卧，K3：硬座，K4：无座

class TrainSpider(object):
    homepage_url="https://www.recreation.gov/"
    login_url="https://www.recreation.gov/&ul=zh-tw&de=UTF-8&dt=Recreation.gov - Camping, Cabins, RVs, Permits, Passes & More&sd=24-bit&sr=1024x1366&vp=1024x1366&je=0&ec=Global Navigation&ea=Link - Log in&el=Open Log in Modal&_u=SACAAEABAAAAAC~&jid=&gjid=&cid=1672939579.1631383298&tid=UA-112750441-5&_gid=1813384824.1632932375&gtm=2wg9r05PH9PJ3&z=835580740"
    rocky_timed_pass_url="https://www.recreation.gov/timed-entry/10086910/ticket/10086911"
    driver = webdriver.Chrome(executable_path='C://Users/gaycl/Downloads/chromedriver.exe')
    email = "huanpingsu123178@gmail.com"
    password = "QQQzzz0000" 
    date="10/11/2021"
    timed_entry="1600"
    #executable_path路径是driver的纯英文路径
    # personal_url='https://www.recreation.gov/&ul=zh-tw&de=UTF-8&dt=Recreation.gov - Camping, Cabins, RVs, Permits, Passes & More&sd=24-bit&sr=1024x1366&vp=1024x1366&je=0&ec=Global Navigation&ea=Link - Log in&el=Open Log in Modal&_u=SACAAEABAAAAAC~&jid=&gjid=&cid=1672939579.1631383298&tid=UA-112750441-5&_gid=1813384824.1632932375&gtm=2wg9r05PH9PJ3&z=835580740'
    # search_ticket_url='https://kyfw.12306.cn/otn/leftTicket/init?'
    # confirm_passenger_url="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    def __init__(self):
        """
        参数说明
        :param from_station: 起始站
        :param to_station: 终点站
        :param train_data: 出发日期
        :param trains: 车次，以字典形式传入eg：{“Z2”：["M"]}
        :param passengers: 以列表形式传递乘车人信息
        ：student：是否抢学生票

        """
    #     self.from_station=from_station
    #     self.to_station=to_station
    #     self.train_data=train_data
    #     self.station_code=self.get_station_code()
    #     self.trains=trains
    #     self.passengers=passengers
    #     self.student=student
    #     self.select_train_info= {}
    #     self.selected_number=None        

    # def get_station_code(self):
    #     station_codes = {}
    #     with open("stations.csv", 'r', encoding='utf-8') as f:
    #         reader = csv.DictReader(f)
    #         for line in reader:
    #             name = line["name"]
    #             code = line["code"]
    #             station_codes[name] = code
    #     return station_codes
    def home(self):
        self.driver.get(self.homepage_url)
        time.sleep(2)
        print('Home Page launch successfully')
        print('==============================')

    def login(self):
        self.driver.find_element_by_id("ga-global-nav-log-in-link").click()
        time.sleep(2)
        self.driver.find_element_by_id("email").send_keys(self.email)
        time.sleep(2)
        self.driver.find_element_by_id("rec-acct-sign-in-password").send_keys(self.password)
        time.sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/form/button").click()

        motion = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/form/button"))

        motion.click()
        # self.driver.get(self.login_url)
        # WebDriverWait(self.driver,1000).until(
        #     EC.url_contains(self.personal_url)#判断是否进入到了个人页面
        # )
        print('login successfully')
    def rockyMounPage(self):
        self.driver.get(self.rocky_timed_pass_url)
        time.sleep(2)
        # //*[@id="tourCalendarWithKey"]
        # //*[@id="page-content"]/main/div[2]/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div/div/label[3]/span/div/div/div[2]
        # motion = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath())
        self.driver.find_element_by_xpath('//*[@id="tourCalendarWithKey"]').send_keys(self.date)
        time.sleep(5)
        # self.driver.find_element_by_id("use-id-22-6").send_keys(self.timed_entry)
        motion = WebDriverWait(self.driver,5).until(lambda x: x.find_element_by_xpath('//*[@id="use-id-16-6"]'))
        time.sleep(5)
        motion.click()
        # motion = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(By.XPATH,'//*[@id="use-id-22-6"]'))
        # motion.send_keys(self.timed_entry)
        time.sleep(2)
        print('date and time selected')
        # response = requests("https://www.recreation.gov/api/timedentry/reservation")
        # print(response)

        




    # def search_ticket(self):
    #     self.driver.get(self.search_ticket_url)
    #     #起始站设置
    #     from_station_input=self.driver.find_element_by_id("fromStation")
    #     from_station_code=self.station_code[self.from_station]
    #     self.driver.execute_script("arguments[0].value='%s'"%from_station_code,from_station_input)
    #     #终点站设置
    #     to_station_input=self.driver.find_element_by_id("toStation")
    #     to_station_code =self.station_code[self.to_station]
    #     self.driver.execute_script("arguments[0].value='%s'"%to_station_code,to_station_input)
    #     #时间设置
    #     train_data_input=self.driver.find_element_by_id("train_date")
    #     self.driver.execute_script("arguments[0].value='%s'" % self.train_data, train_data_input)

    #     #执行查询
    #     search_button=self.driver.find_element_by_id("query_ticket")
    #     search_button.click()
    #     #解析车次信息
    #     WebDriverWait(self.driver,1000).until(
    #         EC.presence_of_element_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
    #     )
    #     train_trs=self.driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
    #     had_searched=False
    #     for train_tr in train_trs:
    #         train_info=train_tr.text.replace('\n',' ').split(' ')
    #         train_id=train_info[0]
    #         if train_id in self.trains:
    #             seat_types=self.trains[train_id]
    #             # 9：商务座，M：一等座，O：二等座，3：硬卧，4：软卧，1：硬座
    #             for seat_type in seat_types:
    #                 if seat_type=='D1':#商务座
    #                     select_type="9"
    #                     count=train_info[7]
    #                     if count.isdigit() or count=='有':
    #                         # order_btn=train_tr.find_elements_by_xpath(".//a[@class='btn72']")
    #                         # order_btn.click()
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="D2":#一等座
    #                     select_type = "M"
    #                     count = train_info[8]
    #                     if count.isdigit() or count == '有':
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="D3":#二等座
    #                     select_type = "O"
    #                     count = train_info[9]
    #                     if count.isdigit() or count == '有':
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="D4" or seat_type=='K4':#无座
    #                     count = train_info[16]
    #                     if count.isdigit() or count == '有':
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="K1":#软卧
    #                     select_type = "4"
    #                     count = train_info[11]
    #                     if count.isdigit() or count == '有':
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="K2":#硬卧
    #                     select_type = "3"
    #                     count = train_info[13]
    #                     if count.isdigit() or count == '有':
    #                         had_searched=True
    #                         break
    #                 elif seat_type=="K3":#硬座
    #                     select_type = "1"
    #                     count = train_info[15]
    #                     if count.isdigit() or count == '有':
    #                         had_searched = True
    #                         break
    #             if had_searched:
    #                 self.selected_number = train_id
    #                 self.select_train_info[train_id]=select_type
    #                 order_btn = train_tr.find_element_by_xpath(".//a[@class='btn72']")
    #                 order_btn.click()
    #                 break
    # def confirm_passengers(self):
    #     WebDriverWait(self.driver,1000).until(
    #         EC.url_contains(self.confirm_passenger_url)
    #     )
    #     # 先等待一下乘客标签显示出来了
    #     WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.XPATH, "//ul[@id='normal_passenger_id']/li/label"))
    #     )
    #     #确认乘车人
    #     passengers=self.driver.find_elements_by_xpath("//ul[@id='normal_passenger_id']/li/label")
    #     for passenger in passengers:
    #         name=passenger.text
    #         if name in self.passengers:
    #             passenger.click()
    #             if self.student:
    #                 # WebDriverWait(self.driver, 1000).until(
    #                 #     EC.text_to_be_present_in_element(("id","dialog_xsertcj_msg"),u'您是要购买学生票吗（凭购票时所使用的有效身份证件原件和附有学生火车票优惠卡的有效学生证原件换票乘车，详见购买学生票有关规定。如不符合相关规定，请点击“取消”。）？')
    #                 # )
    #                 confirm=self.driver.find_element_by_id("dialog_xsertcj_ok")
    #                 confirm.click()
    #             else:
    #                 confirm = self.driver.find_element_by_id("dialog_xsertcj_cancel")
    #                 confirm.click()

    #     #确认席别
    #     seat_select=Select(self.driver.find_element_by_id("seatType_1"))
    #     seat_types=self.select_train_info[self.selected_number]
    #     for seat_type in seat_types:
    #         try:
    #             seat_select.select_by_value(seat_type)
    #         except NoSuchElementException:
    #             continue
    #         else:
    #             break
    #     submit_but=self.driver.find_element_by_id("submitOrder_id")
    #     submit_but.click()
    #     # 判断模态对话框出现并且确认按钮可以点击了
    #     WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "dhtmlx_window_active"))
    #     )
    #     WebDriverWait(self.driver, 1000).until(
    #         EC.element_to_be_clickable((By.ID, "qr_submit_id"))
    #     )
    #     submit_btn = self.driver.find_element_by_id("qr_submit_id")
    #     while submit_btn:
    #         try:
    #             submit_btn.click()
    #             submit_btn = self.driver.find_element_by_id("qr_submit_id")
    #         except ElementNotVisibleException:
    #             break
    #     print("恭喜！%s车次%s抢票成功！" % (self.selected_number, self.seat_type))


    def run(self):
            self.home()
            #登录
            self.login()
            self.rockyMounPage()
            # #查询车票
            # self.search_ticket()
            # #确认乘客和车次
            # self.confirm_passengers()


def main():
    spider=TrainSpider()
    spider.run()


if __name__=='__main__':
    main()
