# -*- coding: utf-8 -*-
"""
第二阶段：大模型开发必备库
演示NumPy、Pandas、requests、aiohttp、asyncio和环境管理
"""


def demo_numpy():
    """演示NumPy基础"""
    print("=" * 50)
    print("NumPy演示")
    print("=" * 50)
    
    try:
        import numpy as np  # type: ignore
        
        # 创建数组
        arr1 = np.array([1, 2, 3, 4, 5])
        print(f"一维数组: {arr1}")
        
        arr2 = np.array([[1, 2, 3], [4, 5, 6]])
        print(f"二维数组:\n{arr2}")
        
        # 数组运算
        print(f"\n数组运算:")
        print(f"arr1 * 2 = {arr1 * 2}")
        print(f"arr1 + 10 = {arr1 + 10}")
        
        # 数组统计
        print(f"\n数组统计:")
        print(f"平均值: {arr1.mean()}")
        print(f"最大值: {arr1.max()}")
        print(f"最小值: {arr1.min()}")
        print(f"标准差: {arr1.std()}")
        
        # 生成数组
        zeros = np.zeros((3, 3))
        ones = np.ones((2, 2))
        range_arr = np.arange(0, 10, 2)
        
        print(f"\n生成数组:")
        print(f"零数组:\n{zeros}")
        print(f"一数组:\n{ones}")
        print(f"范围数组: {range_arr}")
        
    except ImportError:
        print("提示: 需要安装numpy库")
        print("安装命令: pip install numpy")
    
    print()


def demo_pandas():
    """演示Pandas基础"""
    print("=" * 50)
    print("Pandas演示")
    print("=" * 50)
    
    try:
        import pandas as pd  # type: ignore
        
        # 创建Series
        data = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}
        series = pd.Series(data)
        print(f"Series:\n{series}")
        
        # 创建DataFrame
        df = pd.DataFrame({
            "姓名": ["张三", "李四", "王五", "赵六"],
            "年龄": [20, 21, 19, 22],
            "成绩": [85, 92, 78, 88]
        })
        print(f"\nDataFrame:\n{df}")
        
        # DataFrame操作
        print(f"\nDataFrame操作:")
        print(f"前3行:\n{df.head(3)}")
        print(f"描述统计:\n{df.describe()}")
        print(f"筛选成绩>80:\n{df[df['成绩'] > 80]}")
        
        # 读取CSV（示例）
        print(f"\nDataFrame基本信息:")
        print(f"形状: {df.shape}")
        print(f"列名: {df.columns.tolist()}")
        print(f"数据类型:\n{df.dtypes}")
        
    except ImportError:
        print("提示: 需要安装pandas库")
        print("安装命令: pip install pandas")
    
    print()


def demo_requests():
    """演示requests库（HTTP请求）"""
    print("=" * 50)
    print("requests库演示")
    print("=" * 50)
    
    try:
        import requests
        
        # GET请求示例
        print("GET请求示例:")
        print("  response = requests.get('https://api.github.com')")
        print("  print(response.status_code)")
        print("  print(response.json())")
        
        # POST请求示例
        print("\nPOST请求示例:")
        print("  data = {'key': 'value'}")
        print("  response = requests.post('https://httpbin.org/post', json=data)")
        print("  print(response.json())")
        
        # 实际请求（使用公共API）
        try:
            response = requests.get("https://httpbin.org/get", timeout=5)
            print(f"\n实际请求状态码: {response.status_code}")
            print(f"响应头: {dict(list(response.headers.items())[:3])}")
        except Exception as e:
            print(f"网络请求失败（这是正常的，可能需要网络连接）: {e}")
        
    except ImportError:
        print("提示: 需要安装requests库")
        print("安装命令: pip install requests")
    
    print()


def demo_asyncio():
    """演示asyncio基础（异步编程）"""
    print("=" * 50)
    print("asyncio基础演示")
    print("=" * 50)
    
    import asyncio
    
    async def fetch_data(name, delay):
        """模拟异步获取数据"""
        print(f"  开始获取 {name} 的数据...")
        await asyncio.sleep(delay)  # 模拟IO操作
        print(f"  {name} 的数据获取完成")
        return f"{name}的数据"
    
    async def main():
        """主异步函数"""
        print("顺序执行:")
        result1 = await fetch_data("用户", 1)
        result2 = await fetch_data("订单", 1)
        
        print("\n并发执行:")
        results = await asyncio.gather(
            fetch_data("用户", 1),
            fetch_data("订单", 1),
            fetch_data("商品", 1)
        )
        print(f"所有结果: {results}")
    
    # 运行异步函数
    print("异步编程示例:")
    asyncio.run(main())
    
    print()


def demo_aiohttp():
    """演示aiohttp（异步HTTP请求）"""
    print("=" * 50)
    print("aiohttp演示")
    print("=" * 50)
    
    try:
        import aiohttp
        
        async def fetch_url(session, url):
            """异步获取URL内容"""
            async with session.get(url) as response:
                return await response.text()
        
        async def main():
            async with aiohttp.ClientSession() as session:
                # 并发请求多个URL
                urls = [
                    "https://httpbin.org/get",
                    "https://httpbin.org/json"
                ]
                print("异步HTTP请求示例:")
                print("  async with aiohttp.ClientSession() as session:")
                print("      async with session.get(url) as response:")
                print("          data = await response.json()")
        
        # 注意：这里不实际运行，因为需要网络连接
        print("aiohttp使用示例（需要网络连接）:")
        print("  安装: pip install aiohttp")
        print("  用于异步HTTP请求，适合高并发场景")
        
    except ImportError:
        print("提示: 需要安装aiohttp库")
        print("安装命令: pip install aiohttp")
    
    print()


def demo_environment_management():
    """演示环境管理"""
    print("=" * 50)
    print("环境管理演示")
    print("=" * 50)
    
    print("虚拟环境管理:")
    print("\n1. virtualenv:")
    print("  创建: python -m venv venv")
    print("  激活 (Windows): venv\\Scripts\\activate")
    print("  激活 (Linux/Mac): source venv/bin/activate")
    print("  停用: deactivate")
    
    print("\n2. conda:")
    print("  创建: conda create -n myenv python=3.9")
    print("  激活: conda activate myenv")
    print("  停用: conda deactivate")
    print("  安装包: conda install package_name")
    
    print("\n3. pip:")
    print("  安装: pip install package_name")
    print("  卸载: pip uninstall package_name")
    print("  列出: pip list")
    print("  导出: pip freeze > requirements.txt")
    print("  安装依赖: pip install -r requirements.txt")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_numpy()
    demo_pandas()
    demo_requests()
    demo_asyncio()
    demo_aiohttp()
    demo_environment_management()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

