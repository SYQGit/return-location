
# coding: utf-8

# In[1]:


#encoding=utf8  #编码

import json
import requests

#基于百度地图API下的经纬度信息来解析地理位置信息
def getLocation(lat,lng):
    ak = "去百度申请开发者接口"
    url = 'http://api.map.baidu.com/geocoder/v2/?location=' + lat + ',' + lng + '&output=json&pois=1&ak=' + ak
    r = requests.get(url)  # json格式的返回数据
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    r = r.json()
    res = json.dumps(r)
    return json.loads(res)

#json序列化解析数据(lat:纬度，lng:经度)
def jsonFormat(lat,lng):
    str = getLocation(lat,lng)
    dictjson = {}#声明一个字典
    #get()获取json里面的数据
    jsonResult = str.get('result')
    address = jsonResult.get('addressComponent')
    #省
    province = address.get('province')
    #城市
    city = address.get('city')
    #县级
    district = address.get('district')
    #乡镇
    town = address.get('town')
    #街道
    street = address.get('street')
    #门牌号
    street_number = address.get('street_number')
    #把获取到的值，添加到字典里
    dictjson['province'] = province
    dictjson['city'] = city
    dictjson['district'] = district
    dictjson['town'] = town
    dictjson['street'] = street
    dictjson['street_number'] = street_number
    return dictjson.values()

if __name__ == '__main__':
    for value in jsonFormat("26.360001","118.562601"):
        print(f'{value}',end='')

