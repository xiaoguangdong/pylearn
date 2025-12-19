# Python Clean Code 原则详解

## 目录

1. [命名规范](#1-命名规范)
2. [代码组织](#2-代码组织)
3. [函数设计](#3-函数设计)
4. [类设计](#4-类设计)
5. [注释与文档](#5-注释与文档)
6. [错误处理](#6-错误处理)
7. [代码格式](#7-代码格式)
8. [性能优化](#8-性能优化)
9. [测试与可维护性](#9-测试与可维护性)
10. [常见反模式](#10-常见反模式)

---

## 1. 命名规范

### 1.1 变量和函数命名

**原则：使用有意义的名称，清晰表达意图**

```python
# ❌ 不好的命名
def calc(x, y):
    return x * y

# ✅ 好的命名
def calculate_total_price(unit_price, quantity):
    """计算总价格"""
    return unit_price * quantity
```

**命名规则：**
- 使用小写字母和下划线（snake_case）
- 变量名应该是名词：`user_name`, `total_count`
- 函数名应该是动词：`get_user()`, `calculate_total()`
- 布尔值使用 `is_`, `has_`, `can_` 前缀：`is_valid`, `has_permission`
- 避免使用单字母变量（除了循环中的 `i`, `j`, `k`）

```python
# ✅ 好的命名示例
user_name = "张三"
total_count = 100
is_active = True
has_permission = False
can_edit = True

# ❌ 不好的命名
n = "张三"  # 不清晰
cnt = 100  # 缩写不明确
flag = True  # 不知道是什么标志
```

### 1.2 常量命名

**原则：使用全大写字母和下划线**

```python
# ✅ 好的常量命名
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# ❌ 不好的命名
maxRetryCount = 3
default_timeout = 30  # 应该是常量但用了变量命名
```

### 1.3 类命名

**原则：使用驼峰命名法（PascalCase）**

```python
# ✅ 好的类命名
class UserManager:
    pass

class DatabaseConnection:
    pass

class HTTPRequestHandler:
    pass

# ❌ 不好的命名
class user_manager:  # 应该用驼峰命名
    pass

class db_conn:  # 缩写不清晰
    pass
```

### 1.4 私有成员命名

**原则：使用单下划线前缀表示受保护，双下划线前缀表示私有**

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # 公共属性
        self._transaction_history = []  # 受保护属性（约定）
        self.__pin = None  # 私有属性（名称修饰）
    
    def _validate_amount(self, amount):  # 受保护方法
        return amount > 0
    
    def __encrypt_pin(self, pin):  # 私有方法
        # 实现加密逻辑
        pass
```

---

## 2. 代码组织

### 2.1 模块结构

**标准模块结构顺序：**

```python
# 1. 模块文档字符串
"""
模块说明文档
"""

# 2. 导入标准库
import os
import sys
from datetime import datetime

# 3. 导入第三方库
import requests
import numpy as np

# 4. 导入本地模块
from .utils import helper_function
from .models import User

# 5. 常量定义
MAX_SIZE = 1000
DEFAULT_CONFIG = {}

# 6. 类和函数定义
class MyClass:
    pass

def my_function():
    pass

# 7. 主程序入口
if __name__ == "__main__":
    main()
```

### 2.2 导入规范

```python
# ✅ 好的导入方式
import os
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# ❌ 不好的导入方式
import os, sys  # 应该分开导入
from datetime import *  # 避免使用 *
```

### 2.3 包结构

```
project/
├── __init__.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── models/
│   ├── __init__.py
│   └── user.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── main.py
```

---

## 3. 函数设计

### 3.1 函数应该小而专注

**原则：一个函数只做一件事（单一职责原则）**

```python
# ❌ 不好的设计：函数做了太多事情
def process_user_data(user_data):
    # 验证数据
    if not user_data.get('name'):
        return None
    # 格式化数据
    formatted_data = user_data['name'].upper()
    # 保存到数据库
    save_to_database(formatted_data)
    # 发送邮件
    send_email(user_data['email'])
    # 记录日志
    log_action('user_processed')

# ✅ 好的设计：每个函数职责单一
def validate_user_data(user_data):
    """验证用户数据"""
    if not user_data.get('name'):
        raise ValueError("用户名不能为空")
    return True

def format_user_name(name):
    """格式化用户名"""
    return name.strip().upper()

def process_user(user_data):
    """处理用户（协调其他函数）"""
    validate_user_data(user_data)
    formatted_name = format_user_name(user_data['name'])
    save_to_database(formatted_name)
    send_notification(user_data['email'])
```

### 3.2 函数参数

**原则：参数数量应该尽量少（最多3-4个），使用对象或配置类传递多个参数**

```python
# ❌ 不好的设计：参数太多
def create_user(name, email, age, address, phone, role, status):
    pass

# ✅ 好的设计：使用数据类或字典
from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    email: str
    age: int
    address: str
    phone: str
    role: str
    status: str

def create_user(user_info: UserInfo):
    """创建用户"""
    pass

# 或者使用字典（如果结构简单）
def create_user(user_data: dict):
    """创建用户"""
    pass
```

### 3.3 避免副作用

**原则：函数应该尽量是纯函数（无副作用），或者明确副作用**

```python
# ✅ 纯函数：输入相同，输出相同，无副作用
def calculate_total(items):
    """计算总价（纯函数）"""
    return sum(item['price'] * item['quantity'] for item in items)

# ✅ 有副作用的函数：明确说明副作用
def save_user(user_data):
    """保存用户到数据库（有副作用：修改数据库）"""
    # 保存逻辑
    pass

# ❌ 不好的设计：副作用不明确
def process_data(data):
    result = data * 2
    global_variable = result  # 隐式副作用
    return result
```

### 3.4 返回值一致性

**原则：函数返回值类型应该一致**

```python
# ❌ 不好的设计：返回类型不一致
def get_user(user_id):
    if user_id is None:
        return None
    if user_id < 0:
        return False
    return {"id": user_id, "name": "张三"}

# ✅ 好的设计：返回类型一致
def get_user(user_id):
    """获取用户，如果不存在返回None"""
    if user_id is None or user_id < 0:
        return None
    return {"id": user_id, "name": "张三"}

# 或者使用Optional类型提示
from typing import Optional, Dict

def get_user(user_id: int) -> Optional[Dict]:
    """获取用户"""
    if user_id < 0:
        return None
    return {"id": user_id, "name": "张三"}
```

---

## 4. 类设计

### 4.1 单一职责原则

**原则：一个类应该只有一个改变的理由**

```python
# ❌ 不好的设计：类承担了太多职责
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # 数据库操作
        pass
    
    def send_email(self):
        # 邮件发送
        pass
    
    def validate(self):
        # 数据验证
        pass

# ✅ 好的设计：职责分离
class User:
    """用户数据模型"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserValidator:
    """用户验证器"""
    @staticmethod
    def validate(user: User) -> bool:
        return bool(user.name and user.email)

class UserRepository:
    """用户数据仓库"""
    def save(self, user: User):
        # 数据库操作
        pass

class EmailService:
    """邮件服务"""
    def send(self, user: User, message: str):
        # 邮件发送
        pass
```

### 4.2 封装

**原则：隐藏内部实现，只暴露必要的接口**

```python
# ✅ 好的封装
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # 受保护属性
        self._transaction_history = []  # 受保护属性
    
    @property
    def balance(self):
        """余额（只读）"""
        return self._balance
    
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self._balance += amount
        self._transaction_history.append(('deposit', amount))
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        self._transaction_history.append(('withdraw', amount))
    
    def get_transaction_history(self):
        """获取交易历史（只读）"""
        return self._transaction_history.copy()  # 返回副本
```

### 4.3 继承与组合

**原则：优先使用组合而非继承**

```python
# ❌ 不好的设计：过度使用继承
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class ElectricCar(Car):
    pass

# ✅ 好的设计：使用组合
class Engine:
    def start(self):
        pass

class Battery:
    def charge(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine()
        self.battery = None
    
    def start(self):
        self.engine.start()

class ElectricCar:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()
    
    def start(self):
        self.battery.charge()
        self.engine.start()
```

---

## 5. 注释与文档

### 5.1 文档字符串（Docstrings）

**原则：所有公共函数、类和模块都应该有文档字符串**

```python
def calculate_total_price(items: List[Dict], discount: float = 0.0) -> float:
    """
    计算商品总价格
    
    Args:
        items: 商品列表，每个商品包含 'price' 和 'quantity' 键
        discount: 折扣率，范围 0.0-1.0，默认为 0.0
    
    Returns:
        计算后的总价格（浮点数）
    
    Raises:
        ValueError: 当 discount 不在有效范围内时抛出
    
    Example:
        >>> items = [{'price': 10.0, 'quantity': 2}]
        >>> calculate_total_price(items, discount=0.1)
        18.0
    """
    if not 0.0 <= discount <= 1.0:
        raise ValueError("折扣率必须在 0.0 到 1.0 之间")
    
    total = sum(item['price'] * item['quantity'] for item in items)
    return total * (1 - discount)
```

### 5.2 注释原则

**原则：代码应该自解释，注释解释"为什么"而不是"是什么"**

```python
# ❌ 不好的注释：解释显而易见的代码
# 增加计数器
count = count + 1

# ✅ 好的注释：解释为什么这样做
# 使用位运算而不是除法，因为性能更好（在大量计算时）
result = value >> 1  # 等价于 value / 2

# ❌ 不好的注释
# 检查用户是否存在
if user:
    pass

# ✅ 好的注释：解释业务逻辑
# 如果用户不存在，创建新用户（业务规则：自动注册）
if not user:
    user = create_user()
```

### 5.3 类型提示

**原则：使用类型提示提高代码可读性**

```python
from typing import List, Dict, Optional, Union, Callable

def process_users(
    users: List[Dict[str, str]],
    callback: Optional[Callable[[Dict], None]] = None
) -> Dict[str, int]:
    """
    处理用户列表
    
    Args:
        users: 用户字典列表
        callback: 可选的回调函数
    
    Returns:
        包含统计信息的字典
    """
    result = {"total": len(users), "processed": 0}
    
    for user in users:
        # 处理逻辑
        if callback:
            callback(user)
        result["processed"] += 1
    
    return result
```

---

## 6. 错误处理

### 6.1 使用异常而非错误码

```python
# ❌ 不好的设计：使用错误码
def divide(a, b):
    if b == 0:
        return None, "ERROR_DIVIDE_BY_ZERO"
    return a / b, None

result, error = divide(10, 0)
if error:
    print(f"错误: {error}")

# ✅ 好的设计：使用异常
def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"错误: {e}")
```

### 6.2 具体的异常类型

```python
# ❌ 不好的设计：捕获所有异常
try:
    process_data()
except Exception:
    pass  # 不知道发生了什么错误

# ✅ 好的设计：捕获具体异常
try:
    result = int(user_input)
except ValueError:
    print("输入不是有效的整数")
except TypeError:
    print("输入类型错误")
```

### 6.3 自定义异常

```python
# ✅ 定义业务相关的异常
class InsufficientFundsError(Exception):
    """余额不足异常"""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        self.message = f"余额不足：当前余额 {balance}，需要 {amount}"
        super().__init__(self.message)

class BankAccount:
    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
```

### 6.4 异常处理最佳实践

```python
# ✅ 好的异常处理
def process_file(filename: str) -> List[str]:
    """处理文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        logger.error(f"文件不存在: {filename}")
        raise
    except PermissionError:
        logger.error(f"没有权限访问文件: {filename}")
        raise
    except Exception as e:
        logger.error(f"处理文件时发生未知错误: {e}")
        raise
```

---

## 7. 代码格式

### 7.1 PEP 8 规范

**主要规则：**

```python
# ✅ 行长度：每行不超过 79 字符（或 88/100，根据团队约定）
# 使用括号、反斜杠或字符串连接来换行
long_string = (
    "这是一个很长的字符串，"
    "需要分成多行来写，"
    "以符合 PEP 8 规范"
)

# ✅ 缩进：使用 4 个空格（不要使用 Tab）
def example():
    if True:
        print("缩进使用 4 个空格")

# ✅ 导入顺序：标准库、第三方库、本地模块
import os
import sys

import requests
import numpy as np

from .utils import helper
from .models import User

# ✅ 运算符周围空格
result = a + b  # 运算符前后有空格
result = a*b + c*d  # 优先级高的运算符可以不加空格

# ✅ 函数和类定义之间空两行
def function1():
    pass


def function2():
    pass


class MyClass:
    pass
```

### 7.2 代码格式化工具

**推荐使用：**
- `black`: 自动格式化代码
- `flake8`: 检查代码风格
- `pylint`: 代码质量检查
- `mypy`: 类型检查

```bash
# 安装工具
pip install black flake8 pylint mypy

# 格式化代码
black .

# 检查代码风格
flake8 .

# 类型检查
mypy .
```

---

## 8. 性能优化

### 8.1 避免过早优化

**原则：先让代码正确，再考虑优化**

```python
# ✅ 先写清晰的代码
def find_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

# 如果性能有问题，再优化
def find_user_optimized(users, user_id):
    # 使用字典查找（O(1) vs O(n)）
    user_dict = {user['id']: user for user in users}
    return user_dict.get(user_id)
```

### 8.2 使用生成器处理大数据

```python
# ❌ 不好的设计：一次性加载所有数据到内存
def process_large_file(filename):
    with open(filename) as f:
        lines = f.readlines()  # 可能占用大量内存
        for line in lines:
            process(line)

# ✅ 好的设计：使用生成器
def process_large_file(filename):
    with open(filename) as f:
        for line in f:  # 逐行读取
            process(line)
```

### 8.3 使用列表推导式（但不要过度）

```python
# ✅ 简单的列表推导式
squares = [x**2 for x in range(10)]

# ❌ 过度复杂的列表推导式（可读性差）
result = [x for x in [y for y in range(100) if y % 2 == 0] if x > 50]

# ✅ 复杂逻辑使用普通循环
result = []
for y in range(100):
    if y % 2 == 0 and y > 50:
        result.append(y)
```

---

## 9. 测试与可维护性

### 9.1 可测试的代码

```python
# ❌ 不好的设计：难以测试
def process_order():
    user = get_current_user()  # 依赖全局状态
    order = get_order_from_db()  # 直接访问数据库
    send_email(user.email)  # 直接发送邮件

# ✅ 好的设计：依赖注入，易于测试
def process_order(user, order_repository, email_service):
    """处理订单"""
    user = user
    order = order_repository.get_order()
    email_service.send(user.email, "订单确认")
```

### 9.2 单元测试示例

```python
import unittest
from unittest.mock import Mock

class TestOrderProcessor(unittest.TestCase):
    def test_process_order(self):
        # 准备测试数据
        user = Mock(email="test@example.com")
        order_repo = Mock()
        order_repo.get_order.return_value = {"id": 1, "total": 100}
        email_service = Mock()
        
        # 执行测试
        process_order(user, order_repo, email_service)
        
        # 验证结果
        email_service.send.assert_called_once()
```

### 9.3 代码可维护性

**原则：**
- 保持函数简短（通常不超过 20-30 行）
- 减少嵌套层级（通常不超过 3 层）
- 使用早期返回减少嵌套

```python
# ❌ 不好的设计：嵌套过深
def process_user(user):
    if user:
        if user.is_active:
            if user.has_permission:
                if user.balance > 0:
                    return "处理成功"
                else:
                    return "余额不足"
            else:
                return "没有权限"
        else:
            return "用户未激活"
    else:
        return "用户不存在"

# ✅ 好的设计：早期返回
def process_user(user):
    """处理用户"""
    if not user:
        return "用户不存在"
    
    if not user.is_active:
        return "用户未激活"
    
    if not user.has_permission:
        return "没有权限"
    
    if user.balance <= 0:
        return "余额不足"
    
    return "处理成功"
```

---

## 10. 常见反模式

### 10.1 魔法数字和字符串

```python
# ❌ 不好的设计：使用魔法数字
if status == 1:
    process()
elif status == 2:
    cancel()

# ✅ 好的设计：使用常量
STATUS_ACTIVE = 1
STATUS_CANCELLED = 2

if status == STATUS_ACTIVE:
    process()
elif status == STATUS_CANCELLED:
    cancel()
```

### 10.2 深层嵌套

```python
# ❌ 不好的设计：嵌套过深
for user in users:
    if user.is_active:
        for order in user.orders:
            if order.status == 'pending':
                for item in order.items:
                    if item.price > 100:
                        process(item)

# ✅ 好的设计：使用早期返回和生成器
def get_expensive_pending_items(users):
    """获取待处理的昂贵商品"""
    for user in users:
        if not user.is_active:
            continue
        for order in user.orders:
            if order.status != 'pending':
                continue
            for item in order.items:
                if item.price > 100:
                    yield item

for item in get_expensive_pending_items(users):
    process(item)
```

### 10.3 重复代码（DRY原则）

```python
# ❌ 不好的设计：重复代码
def validate_user(user):
    if not user.name:
        return False
    if not user.email:
        return False
    if not user.phone:
        return False
    return True

def validate_order(order):
    if not order.user_id:
        return False
    if not order.total:
        return False
    if not order.items:
        return False
    return True

# ✅ 好的设计：提取公共逻辑
def validate_required_fields(obj, required_fields):
    """验证必需字段"""
    for field in required_fields:
        if not getattr(obj, field, None):
            return False
    return True

def validate_user(user):
    return validate_required_fields(user, ['name', 'email', 'phone'])

def validate_order(order):
    return validate_required_fields(order, ['user_id', 'total', 'items'])
```

### 10.4 过度使用全局变量

```python
# ❌ 不好的设计：过度使用全局变量
config = {}
user_data = {}
cache = {}

def init():
    global config, user_data, cache
    config = load_config()
    user_data = load_user_data()
    cache = {}

def process():
    global config, user_data, cache
    # 使用全局变量
    pass

# ✅ 好的设计：使用类或配置对象
class Application:
    def __init__(self):
        self.config = load_config()
        self.user_data = load_user_data()
        self.cache = {}
    
    def process(self):
        # 使用实例变量
        pass
```

---

## 总结

### Clean Code 核心原则

1. **可读性优先**：代码是写给人看的，机器只是顺便执行
2. **单一职责**：每个函数、类只做一件事
3. **DRY原则**：不要重复自己（Don't Repeat Yourself）
4. **KISS原则**：保持简单（Keep It Simple, Stupid）
5. **SOLID原则**：面向对象设计的五大原则
6. **测试驱动**：编写可测试的代码
7. **持续重构**：代码是演进的，不是一次写成的

### 实践建议

1. **代码审查**：定期进行代码审查，互相学习
2. **使用工具**：使用 linter、formatter 等工具保持代码质量
3. **学习优秀代码**：阅读开源项目的代码，学习最佳实践
4. **重构**：不要害怕重构，持续改进代码质量
5. **文档**：保持文档与代码同步更新

### 推荐阅读

- PEP 8: Python 代码风格指南
- 《Clean Code》by Robert C. Martin
- 《The Pragmatic Programmer》by Andrew Hunt
- 《Refactoring》by Martin Fowler

---

**记住：编写 Clean Code 是一个持续的过程，需要不断学习和实践！**

