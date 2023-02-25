<<<<<<< HEAD
import requests
import math
import numpy as np

CONSTANTS_RADIUS_OF_EARTH = 6371000.     # meters (m)

# 注册成为开发者
# https://lbsyun.baidu.com/apiconsole/user/choose
AK = 'XyP2v28GC4Di4bYfuLVlbiRwvjTVeUzL'


def Pos2Coord(name):
    '''
        @func: 通过百度地图API将地理名称转换成经纬度
        @note: 官方文档 http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
        @output:
            lng: 经度
            lat: 纬度
            conf: 打点绝对精度（即坐标点的误差范围）
            comp: 描述地址理解程度。分值范围0-100，分值越大，服务对地址理解程度越高
            level: 能精确理解的地址类型
    '''
    url = 'http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s' % (name, AK)
    res = requests.get(url)
    if res.status_code == 200:
        val = res.json()
        if val['status'] == 0:
            retVal = {'lng': val['result']['location']['lng'], 'lat': val['result']['location']['lat'], \
                      'conf': val['result']['confidence'], 'comp': val['result']['comprehension'],
                      'level': val['result']['level']}
        else:
            retVal = None
        return retVal
    else:
        print('无法获取%s经纬度' % name)


def Coord2Pos(lng, lat, town='true'):
    '''
        @func: 通过百度地图API将经纬度转换成地理名称
        @input:
            lng: 经度
            lat: 纬度
            town: 是否获取乡镇级地理位置信息，默认获取。可选参数（true/false）
        @output:
            address:解析后的地理位置名称
            province:省份名称
            city:城市名
            district:县级行政区划名
            town: 乡镇级行政区划
            adcode: 县级行政区划编码
            town_code: 镇级行政区划编码
    '''
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?output=json&ak=%s&location=%s,%s&extensions_town=%s' % (
    AK, lat, lng, town)
    res = requests.get(url)
    if res.status_code == 200:
        val = res.json()
        if val['status'] == 0:
            val = val['result']
            retVal = {'address': val['formatted_address'], 'province': val['addressComponent']['province'], \
                      'city': val['addressComponent']['city'], 'district': val['addressComponent']['district'], \
                      'town': val['addressComponent']['town'], 'adcode': val['addressComponent']['adcode'],
                      'town_code': val['addressComponent']['town_code']}
        else:
            retVal = None
        return retVal
    else:
        print('无法获取(%s,%s)的地理信息！' % (lat, lng))


def GPStoXY(lat, lon, ref_lat, ref_lon):
    # input GPS and Reference GPS in degrees
    # output XY in meters (m) X:North Y:East
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)

    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)

    cos_d_lon = math.cos(lon_rad - ref_lon_rad)

    arg = np.clip(ref_sin_lat * sin_lat + ref_cos_lat * cos_lat * cos_d_lon, -1.0, 1.0)
    c = math.acos(arg)

    k = 1.0
    if abs(c) > 0:
        k = (c / math.sin(c))

    x = float(k * (ref_cos_lat * sin_lat - ref_sin_lat * cos_lat * cos_d_lon) * self.CONSTANTS_RADIUS_OF_EARTH)
    y = float(k * cos_lat * math.sin(lon_rad - ref_lon_rad) * self.CONSTANTS_RADIUS_OF_EARTH)

    return x, y


def XYtoGPS(x, y, ref_lat, ref_lon):
    x_rad = float(x) / self.CONSTANTS_RADIUS_OF_EARTH
    y_rad = float(y) / self.CONSTANTS_RADIUS_OF_EARTH
    c = math.sqrt(x_rad * x_rad + y_rad * y_rad)

    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)

    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)

    if abs(c) > 0:
        sin_c = math.sin(c)
        cos_c = math.cos(c)

        lat_rad = math.asin(cos_c * ref_sin_lat + (x_rad * sin_c * ref_cos_lat) / c)
        lon_rad = (ref_lon_rad + math.atan2(y_rad * sin_c, c * ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c))

        lat = math.degrees(lat_rad)
        lon = math.degrees(lon_rad)

    else:
        lat = math.degrees(ref_lat)
        lon = math.degrees(ref_lon)

    return lat, lon

if __name__ == "__main__":
    # （1）正地理编码
    # 比如获取学校的经纬度：
    val = Pos2Coord('江苏省南京市江宁区秣陵街道东南大学九龙湖校区')
    print(val)
    # {‘lng’: 118.81871976794395, ‘lat’: 31.88198449339288, ‘conf’: 80, ‘comp’: 57, ‘level’: ‘餐饮’}

    # （2）逆地理编码
    # 反过来，我们也可以根据经纬度查询地理位置信息
    val = Coord2Pos(118.81871976794395, 31.88198449339288)
    print(val)
    # {‘lng’: 118.81871976794395, ‘lat’: 31.88198449339288, ‘conf’: 80, ‘comp’: 57, ‘level’: ‘餐饮’}
=======
import requests
import math
import numpy as np

CONSTANTS_RADIUS_OF_EARTH = 6371000.     # meters (m)

# 注册成为开发者
# https://lbsyun.baidu.com/apiconsole/user/choose
AK = 'XyP2v28GC4Di4bYfuLVlbiRwvjTVeUzL'


def Pos2Coord(name):
    '''
        @func: 通过百度地图API将地理名称转换成经纬度
        @note: 官方文档 http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
        @output:
            lng: 经度
            lat: 纬度
            conf: 打点绝对精度（即坐标点的误差范围）
            comp: 描述地址理解程度。分值范围0-100，分值越大，服务对地址理解程度越高
            level: 能精确理解的地址类型
    '''
    url = 'http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s' % (name, AK)
    res = requests.get(url)
    if res.status_code == 200:
        val = res.json()
        if val['status'] == 0:
            retVal = {'lng': val['result']['location']['lng'], 'lat': val['result']['location']['lat'], \
                      'conf': val['result']['confidence'], 'comp': val['result']['comprehension'],
                      'level': val['result']['level']}
        else:
            retVal = None
        return retVal
    else:
        print('无法获取%s经纬度' % name)


def Coord2Pos(lng, lat, town='true'):
    '''
        @func: 通过百度地图API将经纬度转换成地理名称
        @input:
            lng: 经度
            lat: 纬度
            town: 是否获取乡镇级地理位置信息，默认获取。可选参数（true/false）
        @output:
            address:解析后的地理位置名称
            province:省份名称
            city:城市名
            district:县级行政区划名
            town: 乡镇级行政区划
            adcode: 县级行政区划编码
            town_code: 镇级行政区划编码
    '''
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?output=json&ak=%s&location=%s,%s&extensions_town=%s' % (
    AK, lat, lng, town)
    res = requests.get(url)
    if res.status_code == 200:
        val = res.json()
        if val['status'] == 0:
            val = val['result']
            retVal = {'address': val['formatted_address'], 'province': val['addressComponent']['province'], \
                      'city': val['addressComponent']['city'], 'district': val['addressComponent']['district'], \
                      'town': val['addressComponent']['town'], 'adcode': val['addressComponent']['adcode'],
                      'town_code': val['addressComponent']['town_code']}
        else:
            retVal = None
        return retVal
    else:
        print('无法获取(%s,%s)的地理信息！' % (lat, lng))


def GPStoXY(lat, lon, ref_lat, ref_lon):
    # input GPS and Reference GPS in degrees
    # output XY in meters (m) X:North Y:East
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)

    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)

    cos_d_lon = math.cos(lon_rad - ref_lon_rad)

    arg = np.clip(ref_sin_lat * sin_lat + ref_cos_lat * cos_lat * cos_d_lon, -1.0, 1.0)
    c = math.acos(arg)

    k = 1.0
    if abs(c) > 0:
        k = (c / math.sin(c))

    x = float(k * (ref_cos_lat * sin_lat - ref_sin_lat * cos_lat * cos_d_lon) * self.CONSTANTS_RADIUS_OF_EARTH)
    y = float(k * cos_lat * math.sin(lon_rad - ref_lon_rad) * self.CONSTANTS_RADIUS_OF_EARTH)

    return x, y


def XYtoGPS(x, y, ref_lat, ref_lon):
    x_rad = float(x) / self.CONSTANTS_RADIUS_OF_EARTH
    y_rad = float(y) / self.CONSTANTS_RADIUS_OF_EARTH
    c = math.sqrt(x_rad * x_rad + y_rad * y_rad)

    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)

    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)

    if abs(c) > 0:
        sin_c = math.sin(c)
        cos_c = math.cos(c)

        lat_rad = math.asin(cos_c * ref_sin_lat + (x_rad * sin_c * ref_cos_lat) / c)
        lon_rad = (ref_lon_rad + math.atan2(y_rad * sin_c, c * ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c))

        lat = math.degrees(lat_rad)
        lon = math.degrees(lon_rad)

    else:
        lat = math.degrees(ref_lat)
        lon = math.degrees(ref_lon)

    return lat, lon

if __name__ == "__main__":
    # （1）正地理编码
    # 比如获取学校的经纬度：
    val = Pos2Coord('江苏省南京市江宁区秣陵街道东南大学九龙湖校区')
    print(val)
    # {‘lng’: 118.81871976794395, ‘lat’: 31.88198449339288, ‘conf’: 80, ‘comp’: 57, ‘level’: ‘餐饮’}

    # （2）逆地理编码
    # 反过来，我们也可以根据经纬度查询地理位置信息
    val = Coord2Pos(118.81871976794395, 31.88198449339288)
    print(val)
    # {‘lng’: 118.81871976794395, ‘lat’: 31.88198449339288, ‘conf’: 80, ‘comp’: 57, ‘level’: ‘餐饮’}
>>>>>>> 4c0d67466d39a8ef4aee9e02ddd91a26373d2c31
