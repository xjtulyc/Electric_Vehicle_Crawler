import re
from urllib.request import quote

import requests
import xlsxwriter
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm


def get_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
            return None
    except:
        print('访问 http 发生错误... ')
        return None


def get_charging_pile(driver_path="/slurm_data/youcheng.li/EVCrawler/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",
                      provincce=None):
    driver = webdriver.PhantomJS(
        executable_path=driver_path
    )  # 启动浏览器
    if provincce is None:
        # 中国所有省份
        province = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建',
                    '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州',
                    '云南', '陕西', '甘肃', '青海', '北京', '天津', '上海', '重庆', '香港', '澳门',
                    '内蒙古', '广西', '西藏', '宁夏', '新疆']

    for location in tqdm(province):
        # 1.得到一个城市所有停车桩链接
        info = []
        web = r"http://www.bjev520.com/jsp/beiqi/pcmap/do/pcMap.jsp?cityName={}".format(quote(location))
        print(location, web)
        driver.get(web)  # 用浏览器打开链接，北京可以改成其他省份
        driver.implicitly_wait(5)  # 隐式等待5秒钟，智能等待网页加载
        driver.switch_to.frame('left')  # 网页是嵌套的，在一网页下面，有一个iframe，我们找到这个iframe
        soup = driver.find_elements_by_tag_name('a')  # 链接都在a标签中，我们找到a标签
        for item in soup:
            info.append(item.get_attribute('href'))  # 提取数a标签里面的href链接
        # 3.数据筛选
        j = 1
        workbook = xlsxwriter.Workbook("充电桩/{}.xlsx".format(location))
        df = workbook.add_worksheet()
        cols = ["名称", "地址", "快充数量", "慢充数量", "支付方式", "充电费", "服务费", "停车费", "开放时间"]
        for i in range(9):
            df.write(0, i, cols[i])

        for u in info:
            url = u
            # print(j)
            html = get_data(url)
            if html != None:
                soup = BeautifulSoup(html)
                Name = soup.find_all("div", {"class": "news-top"})[0]
                name = Name.find_all("p")[0].text
                Address = soup.find_all("div", {"class": "news-a"})[0]
                address = Address.find_all("p")[0].text
                try:
                    num = soup.find_all("div", {"class": "news-c"})[0].find_all("p")[0].text
                    p = re.compile('数量：(.*)个')
                    num = re.findall(p, num)[0]
                except:
                    num = "NA"
                try:
                    num2 = soup.find_all("div", {"class": "news-c"})[0].find_all("p")[1].text
                    p = re.compile('数量：(.*)个')
                    num2 = re.findall(p, num2)[0]

                except:
                    num2 = "NA"
                Pay_type = soup.find_all("div", {"class": "news-con"})[0].find_all("ul", {"class": "news-d details"})[0]
                pay_type = Pay_type.find_all("li")[0].find_all("div")[0].text
                p1 = re.compile("支付方式：")
                pay_num = Pay_type.find_all("li")[1].find_all("div")[0].text.strip()
                pay_fee = Pay_type.find_all("li")[2].find_all("div")[0].text.strip()
                pay_park = Pay_type.find_all("li")[3].find_all("div")[0].text.strip()
                time = Pay_type.find_all("li")[4].find_all("div")[0].text.strip()
                # 4.把数据存储
                if name != None:
                    df.write(j, 0, name)
                    df.write(j, 1, address)
                    df.write(j, 2, num)
                    df.write(j, 3, num2)
                    df.write(j, 4, pay_type)
                    df.write(j, 5, pay_num)
                    df.write(j, 6, pay_fee)
                    df.write(j, 7, pay_park)
                    df.write(j, 8, time)
                    j = j + 1
            else:
                j = j + 1

        workbook.close()
    print("Finished")


if __name__ == "__main__":
    driver = webdriver.PhantomJS(
        executable_path="/slurm_data/youcheng.li/EVCrawler/phantomjs-2.1.1-linux-x86_64/bin/phantomjs"
    )  # 启动浏览器
    # 中国所有省份
    province = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川',
                '贵州',
                '云南', '陕西', '甘肃', '青海', '北京', '天津', '上海', '重庆', '香港', '澳门', '内蒙古', '广西', '西藏', '宁夏', '新疆']

    for location in tqdm(province):
        # 1.得到一个城市所有停车桩链接
        info = []
        web = r"http://www.bjev520.com/jsp/beiqi/pcmap/do/pcMap.jsp?cityName={}".format(quote(location))
        print(location, web)
        driver.get(web)  # 用浏览器打开链接，北京可以改成其他省份
        driver.implicitly_wait(5)  # 隐式等待5秒钟，智能等待网页加载
        driver.switch_to.frame('left')  # 网页是嵌套的，在一网页下面，有一个iframe，我们找到这个iframe
        soup = driver.find_elements_by_tag_name('a')  # 链接都在a标签中，我们找到a标签
        for item in soup:
            info.append(item.get_attribute('href'))  # 提取数a标签里面的href链接
        # 3.数据筛选
        j = 1
        workbook = xlsxwriter.Workbook("充电桩/{}.xlsx".format(location))
        df = workbook.add_worksheet()
        cols = ["名称", "地址", "快充数量", "慢充数量", "支付方式", "充电费", "服务费", "停车费", "开放时间"]
        for i in range(9):
            df.write(0, i, cols[i])

        for u in info:
            url = u
            # print(j)
            html = get_data(url)
            if html != None:
                soup = BeautifulSoup(html)
                Name = soup.find_all("div", {"class": "news-top"})[0]
                name = Name.find_all("p")[0].text
                Address = soup.find_all("div", {"class": "news-a"})[0]
                address = Address.find_all("p")[0].text
                try:
                    num = soup.find_all("div", {"class": "news-c"})[0].find_all("p")[0].text
                    p = re.compile('数量：(.*)个')
                    num = re.findall(p, num)[0]
                except:
                    num = "NA"
                try:
                    num2 = soup.find_all("div", {"class": "news-c"})[0].find_all("p")[1].text
                    p = re.compile('数量：(.*)个')
                    num2 = re.findall(p, num2)[0]

                except:
                    num2 = "NA"
                Pay_type = soup.find_all("div", {"class": "news-con"})[0].find_all("ul", {"class": "news-d details"})[0]
                pay_type = Pay_type.find_all("li")[0].find_all("div")[0].text
                p1 = re.compile("支付方式：")
                pay_num = Pay_type.find_all("li")[1].find_all("div")[0].text.strip()
                pay_fee = Pay_type.find_all("li")[2].find_all("div")[0].text.strip()
                pay_park = Pay_type.find_all("li")[3].find_all("div")[0].text.strip()
                time = Pay_type.find_all("li")[4].find_all("div")[0].text.strip()
                # 4.把数据存储
                if name != None:
                    df.write(j, 0, name)
                    df.write(j, 1, address)
                    df.write(j, 2, num)
                    df.write(j, 3, num2)
                    df.write(j, 4, pay_type)
                    df.write(j, 5, pay_num)
                    df.write(j, 6, pay_fee)
                    df.write(j, 7, pay_park)
                    df.write(j, 8, time)
                    j = j + 1
            else:
                j = j + 1

        workbook.close()
    print("Finished")
