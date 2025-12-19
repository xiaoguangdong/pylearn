# Python 学习计划 - Demo代码库

这是一个按照学习计划组织的Python学习demo代码库，包含从基础到高级的完整示例代码。

## 📁 项目结构

```
pylearn/
├── stage1_basics/              # 第一阶段：Python核心基础
│   ├── 01_environment_and_syntax.py      # 环境配置与基础语法
│   ├── 02_data_structures_and_control.py # 数据结构与流程控制
│   └── 03_functions_and_modules.py       # 函数与模块
│
├── stage2_advanced/            # 第二阶段：面向大模型开发的核心技能
│   ├── 04_oop.py                        # 面向对象编程
│   ├── 05_file_operations.py            # 文件操作与数据序列化
│   ├── 06_exception_handling.py         # 异常处理与调试
│   └── 07_essential_libraries.py        # 大模型开发必备库
│
├── stage3_advanced_topics/     # 第三阶段：高级主题与实战
│   ├── 08_decorators_and_context.py     # 装饰器与上下文管理器
│   ├── 09_generators_and_iterators.py   # 生成器与迭代器
│   ├── 10_multithreading_multiprocessing.py # 多线程与多进程
│   └── 11_llm_development.py            # 大模型开发实践
│
├── docs/                       # 文档目录
│   └── clean_code_principles.md # Python Clean Code 原则详解
├── requirements.txt            # 项目依赖
├── 学习计划.md                 # 学习计划文档
└── README.md                   # 本文件
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行Demo

每个demo文件都可以独立运行：

```bash
# 运行基础语法demo
python stage1_basics/01_environment_and_syntax.py

# 运行OOP demo
python stage2_advanced/04_oop.py

# 运行装饰器demo
python stage3_advanced_topics/08_decorators_and_context.py
```

## 📚 学习路径

### 第一阶段：Python核心基础（4-6小时）

1. **环境配置与基础语法** (`01_environment_and_syntax.py`)
   - 变量与数据类型
   - 基本运算符与表达式
   - 代码规范

2. **数据结构与流程控制** (`02_data_structures_and_control.py`)
   - 列表、元组、字典、集合
   - 条件语句和循环
   - 列表推导式

3. **函数与模块** (`03_functions_and_modules.py`)
   - 函数定义与调用
   - 参数传递（*args, **kwargs）
   - Lambda表达式
   - 模块导入

### 第二阶段：面向大模型开发的核心技能（6-8小时）

4. **面向对象编程** (`04_oop.py`)
   - 类与对象
   - 继承与多态
   - 特殊方法
   - 属性装饰器

5. **文件操作与数据序列化** (`05_file_operations.py`)
   - 文件读写
   - JSON、YAML处理
   - CSV、Excel处理
   - pathlib路径管理

6. **异常处理与调试** (`06_exception_handling.py`)
   - try-except-finally
   - 自定义异常
   - 调试技巧

7. **大模型开发必备库** (`07_essential_libraries.py`)
   - NumPy、Pandas
   - requests、aiohttp
   - asyncio异步编程
   - 环境管理

### 第三阶段：高级主题与实战（4-6小时）

8. **装饰器与上下文管理器** (`08_decorators_and_context.py`)
   - 函数装饰器
   - 类装饰器
   - with语句

9. **生成器与迭代器** (`09_generators_and_iterators.py`)
   - 迭代器协议
   - 生成器函数
   - 生成器表达式

10. **多线程与多进程** (`10_multithreading_multiprocessing.py`)
    - 并发与并行
    - threading模块
    - multiprocessing模块

11. **大模型开发实践** (`11_llm_development.py`)
    - API调用模式
    - 提示工程
    - 数据处理管道
    - 简单应用搭建

## 💡 使用建议

1. **按顺序学习**：建议按照阶段顺序学习，每个阶段的内容都建立在前一阶段的基础上。

2. **动手实践**：不要只看代码，尝试修改和运行，理解每个概念的实际应用。

3. **扩展练习**：在理解demo的基础上，尝试编写自己的代码来解决实际问题。

4. **查阅文档**：遇到不理解的地方，查阅Python官方文档或相关库的文档。

## 📝 注意事项

- 部分demo需要安装额外的库（如openpyxl、pyyaml等），请根据`requirements.txt`安装
- 某些网络相关的demo（如requests、aiohttp）可能需要网络连接
- 大模型开发相关的demo是模拟实现，实际使用时需要配置真实的API密钥

## 🔧 依赖说明

主要依赖包：
- `numpy`: 数值计算
- `pandas`: 数据处理
- `requests`: HTTP请求
- `aiohttp`: 异步HTTP请求
- `openpyxl`: Excel文件处理
- `pyyaml`: YAML文件处理

## 📖 学习资源

参考 `学习计划.md` 文件中的学习资源推荐部分。

## 📚 代码规范

本项目遵循 Python Clean Code 原则，详细说明请参考：
- [Python Clean Code 原则详解](docs/clean_code_principles.md)

该文档包含：
- 命名规范
- 代码组织
- 函数和类设计
- 注释与文档
- 错误处理
- 代码格式（PEP 8）
- 性能优化
- 测试与可维护性
- 常见反模式

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可证

本项目仅用于学习目的。

