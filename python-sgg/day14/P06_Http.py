"""
    该案例演示了通过发送http请求，获取一言网信息
"""
import requests

# 一言网的 API 地址
url = 'https://international.v1.hitokoto.cn'

# 请求参数，指定返回中文内容，这里使用默认的所有类型
params = {
    'c': 'a',  # 可以根据需要修改类型，a 代表动画，b 代表漫画等
    'encode': 'json'
}

try:
    print(f"正在发送 GET 请求到: {url}，参数: {params}")
    response = requests.get(url, params=params)
    status_code = response.status_code
    if status_code == 200:
        print(f"请求成功！状态码: {status_code}")
        data = response.json()
        hitokoto = data['hitokoto']
        from_who = data['from_who'] if data['from_who'] else '未知'
        print(f"随机名言: {hitokoto} - {from_who}")
    elif status_code == 404:
        print(f"请求的资源未找到！状态码: {status_code}")
    elif status_code == 500:
        print(f"服务器内部错误！状态码: {status_code}")
    else:
        print(f"发生未知错误，状态码: {status_code}")
except requests.RequestException as e:
    print(f"请求过程中出现错误: {e}")
