from selenium import webdriver
import time
import json
import os
class auto_study:
    def __init__(self):

        '''
        course = {'腾讯课堂的课程名':'课程时间'}
        课程时间 = '分 时 * * 周'

        '''
        self.driver = self.get_driver()
        courses = {'管理英语1班': ['25 1 * * 3 ', ''],
                   '全球价值链量化研究-1-余心玎': '25 18 * * 4',
                   '刘瑞林老师的课堂': '45 9 * * 1',
                   '国际金融学-4-蒋先玲': '45 9 * * 3',
                   '经贸研究与论文写作-2-谢红军': '45 9 * * 2',
                   '国际商务概论-1-王炜瀚': '15 3 * * 1',
                   '棒/垒球-1-李江华': '55 7 * * 3'}
    def get_driver(self):


        #随机选择代理ip地址
        # proxy = proxy_list[np.random.randint(len(proxy_list))]
        options = webdriver.ChromeOptions()
        # 设置屏幕大小
        options.add_argument('--window-size=1980,1080')
        # options.add_argument('…proxy-server=' + proxy)
        # options.add_argument('--headless')
        driver = webdriver.Chrome('/Users/prettybeach/Documents/Rangduju/Note/chromedriver')# 请自行配置浏览器驱动,建议安装在Python根目录下
        # 隐式等待三秒
        driver.implicitly_wait(3)
        # driver.login()
        return driver

    def login(self,first_time = False):
        def generate_cookies():
            loginUrl = 'https://ke.qq.com/'
            self.driver.get(loginUrl)
            self.driver.set_window_size(1024, 768)
            self.driver.find_element_by_xpath('//*[@id="js-mod-entry-index"]/a').click()
            c = input("请登陆网站，登陆网站后输入True并回车")
            if c != 'True' :
                print("登陆失败")

            # 保存cookies，以供自动登录
            dictCookies = self.driver.get_cookies()
            jsonCookies = json.dumps(dictCookies)
            with open('ketang_cookies.json', 'w') as f:
                f.write(jsonCookies)
            self.driver.get("https://ke.qq.com")
            self.driver.delete_all_cookies()

        if first_time:
            generate_cookies()
        self.driver.get('https://ke.qq.com')
        cookies_path = os.path.abspath('ketang_cookies.json')
        with open(cookies_path, 'r') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            self.driver.add_cookie({
                'domain': '.ke.qq.com',  # 此处xxx.com前，需要带点
                'httpOnly': cookie['httpOnly'],
                'name': cookie['name'],
                'path': '/',
                'secure': cookie['secure'],
                'value': cookie['value']
            })

    def study(self,course_name :str = '棒/垒球-1-李江华',course_time_by_minute :int = 90):
        '''
        进入指定的课堂
        :param course_name 课程名称
        :param course_time_by_minut
        '''
        #进入到课程表页面
        self.login(False)
        self.driver.find_element_by_xpath('//*[@id="js-intrest-select"]/div[2]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="js-mod-entry-index"]/div/a').click()
        self.driver.find_element_by_xpath('//*[@id="react-body"]/section/main/div/section/div[2]/div[2]/span').click()

        #进入某一节课

        while (True):
            try:
                self.driver.find_element_by_xpath(
                    f'//div[@class="tab-course-list clear-fix"]//p[@title="{course_name}"]').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="react-body"]/section/main/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[5]/div/a').click()
                break
            except:
                # 翻页
                try:
                    self.driver.find_element_by_xpath('//div[@class="tab-move-btn tab-next-btn"]').click()
                except:
                    print("找不到这门课程")
                    self.quit()
                    return

        time.sleep(int(course_time_by_minute)*60)
        self.quit()

    def direct_study(self,course_time_by_minute :int = 90):
        '''
        直接进入目前正在直播的课程，等待指定时长后退出浏览器
        :param course_time_by_minute: 课程时长
        :return: 
        '''
        self.login(False)
        self.driver.find_element_by_xpath('//*[@id="js-intrest-select"]/div[2]/div/a[1]').click()
        try:
            self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div/div/div/a').click()
            time.sleep(course_time_by_minute*60)
        except:
            print("目前没有正在直播的课程")
        self.quit()
 
    def quit(self):
        self.driver.quit()
