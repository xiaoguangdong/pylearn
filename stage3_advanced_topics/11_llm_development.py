# -*- coding: utf-8 -*-
"""
第三阶段：大模型开发实践
演示API调用模式、提示工程、数据处理管道和简单应用搭建
"""

from typing import List, Dict, Any, Optional


def demo_api_call_pattern():
    """演示API调用模式（OpenAI, Claude等）"""
    print("=" * 50)
    print("API调用模式演示")
    print("=" * 50)
    
    # 模拟API调用类
    class LLMClient:
        """大语言模型客户端基类"""
        
        def __init__(self, api_key: str, base_url: str):
            self.api_key = api_key
            self.base_url = base_url
        
        def chat_completion(self, messages: List[Dict], **kwargs) -> Dict:
            """聊天完成接口"""
            # 这里是模拟实现，实际需要调用真实API
            print(f"  调用API: {self.base_url}")
            print(f"  消息数量: {len(messages)}")
            return {
                "choices": [{
                    "message": {
                        "content": "这是模拟的API响应"
                    }
                }]
            }
    
    # OpenAI风格API调用
    class OpenAIClient(LLMClient):
        """OpenAI风格客户端"""
        
        def __init__(self, api_key: str):
            super().__init__(api_key, "https://api.openai.com/v1")
        
        def chat(self, messages: List[Dict], model: str = "gpt-3.5-turbo") -> str:
            """聊天接口"""
            response = self.chat_completion(messages, model=model)
            return response["choices"][0]["message"]["content"]
    
    # 使用示例
    print("OpenAI风格API调用:")
    client = OpenAIClient("your-api-key")
    messages = [
        {"role": "system", "content": "你是一个有用的助手"},
        {"role": "user", "content": "你好！"}
    ]
    response = client.chat(messages)
    print(f"  响应: {response}\n")
    
    # 异步API调用示例
    print("异步API调用示例:")
    print("  import asyncio")
    print("  import aiohttp")
    print("")
    print("  async def async_chat(session, messages):")
    print("      async with session.post(url, json={'messages': messages}) as resp:")
    print("          return await resp.json()")
    
    print()


def demo_prompt_engineering():
    """演示提示工程模板编写"""
    print("=" * 50)
    print("提示工程模板演示")
    print("=" * 50)
    
    # 提示模板类
    class PromptTemplate:
        """提示模板"""
        
        def __init__(self, template: str):
            self.template = template
        
        def format(self, **kwargs) -> str:
            """格式化提示"""
            return self.template.format(**kwargs)
    
    # 1. 基础提示模板
    basic_template = PromptTemplate(
        "请回答以下问题：{question}"
    )
    print("基础提示模板:")
    print(f"  {basic_template.format(question='Python是什么？')}\n")
    
    # 2. 角色扮演模板
    role_template = PromptTemplate(
        "你是一个专业的{role}。请以{role}的身份回答以下问题：{question}"
    )
    print("角色扮演模板:")
    print(f"  {role_template.format(role='Python开发工程师', question='如何优化代码性能？')}\n")
    
    # 3. 少样本学习模板
    few_shot_template = PromptTemplate(
        """以下是几个示例：

示例1：
输入：{example1_input}
输出：{example1_output}

示例2：
输入：{example2_input}
输出：{example2_output}

现在请根据以上示例，回答：
输入：{question}
输出："""
    )
    print("少样本学习模板:")
    formatted = few_shot_template.format(
        example1_input='翻译：Hello',
        example1_output='你好',
        example2_input='翻译：Goodbye',
        example2_output='再见',
        question='翻译：Thank you'
    )
    print(f"  {formatted}\n")
    
    # 4. 思维链模板
    chain_of_thought_template = PromptTemplate(
        """请逐步思考并回答以下问题：

问题：{question}

请按以下步骤思考：
1. 理解问题
2. 分析关键点
3. 给出答案
4. 验证答案

开始回答："""
    )
    print("思维链模板:")
    print(f"  {chain_of_thought_template.format(question='如何学习Python？')}\n")
    
    # 5. 提示工程最佳实践
    print("提示工程最佳实践:")
    print("  - 明确任务和目标")
    print("  - 提供上下文信息")
    print("  - 使用示例（少样本学习）")
    print("  - 指定输出格式")
    print("  - 迭代优化提示")
    
    print()


def demo_data_processing_pipeline():
    """演示数据处理管道构建"""
    print("=" * 50)
    print("数据处理管道演示")
    print("=" * 50)
    
    # 数据处理管道类
    class DataPipeline:
        """数据处理管道"""
        
        def __init__(self):
            self.steps = []
        
        def add_step(self, func, name: Optional[str] = None):
            """添加处理步骤"""
            self.steps.append({
                "func": func,
                "name": name or func.__name__
            })
            return self
        
        def process(self, data: Any) -> Any:
            """执行管道处理"""
            result = data
            for step in self.steps:
                print(f"  执行步骤: {step['name']}")
                result = step["func"](result)
            return result
    
    # 定义处理函数
    def clean_text(text: str) -> str:
        """清理文本"""
        return text.strip().lower()
    
    def remove_punctuation(text: str) -> str:
        """移除标点"""
        import string
        return text.translate(str.maketrans("", "", string.punctuation))
    
    def split_words(text: str) -> List[str]:
        """分词"""
        return text.split()
    
    def filter_words(words: List[str], min_length: int = 3) -> List[str]:
        """过滤短词"""
        return [w for w in words if len(w) >= min_length]
    
    # 构建管道
    pipeline = DataPipeline()
    pipeline.add_step(clean_text, "清理文本")
    pipeline.add_step(remove_punctuation, "移除标点")
    pipeline.add_step(split_words, "分词")
    pipeline.add_step(filter_words, "过滤短词")
    
    # 处理数据
    raw_text = "  Hello, World! This is a test.  "
    print(f"原始文本: '{raw_text}'")
    result = pipeline.process(raw_text)
    print(f"处理结果: {result}\n")
    
    # 批量处理
    print("批量处理:")
    texts = [
        "  Python is great!  ",
        "  Machine Learning is fun.  ",
        "  Data Science rocks!  "
    ]
    
    for text in texts:
        result = pipeline.process(text)
        print(f"  '{text}' -> {result}")
    
    print()


def demo_simple_llm_app():
    """演示简单的大模型应用搭建"""
    print("=" * 50)
    print("简单大模型应用演示")
    print("=" * 50)
    
    # 简单的问答应用
    class SimpleQAApp:
        """简单的问答应用"""
        
        def __init__(self):
            self.history = []
        
        def ask(self, question: str) -> str:
            """提问"""
            # 模拟API调用
            response = f"这是对'{question}'的回答（模拟）"
            
            # 保存历史
            self.history.append({
                "question": question,
                "answer": response
            })
            
            return response
        
        def get_history(self) -> List[Dict]:
            """获取历史记录"""
            return self.history
        
        def clear_history(self):
            """清空历史"""
            self.history = []
    
    # 使用应用
    app = SimpleQAApp()
    
    print("问答应用示例:")
    q1 = "Python是什么？"
    a1 = app.ask(q1)
    print(f"  问题: {q1}")
    print(f"  回答: {a1}\n")
    
    q2 = "如何学习Python？"
    a2 = app.ask(q2)
    print(f"  问题: {q2}")
    print(f"  回答: {a2}\n")
    
    print("历史记录:")
    for i, record in enumerate(app.get_history(), 1):
        print(f"  {i}. Q: {record['question']}")
        print(f"     A: {record['answer']}")
    
    print()
    
    # 应用架构建议
    print("大模型应用架构建议:")
    print("  1. 客户端层：用户界面（CLI/Web/API）")
    print("  2. 业务逻辑层：提示管理、历史管理、上下文处理")
    print("  3. 服务层：API调用、错误处理、重试机制")
    print("  4. 数据层：历史存储、配置管理、缓存")
    print("  5. 工具层：数据处理、格式化、验证")
    
    print()


def demo_best_practices():
    """演示最佳实践"""
    print("=" * 50)
    print("大模型开发最佳实践")
    print("=" * 50)
    
    print("1. API调用:")
    print("  - 使用重试机制处理网络错误")
    print("  - 设置合理的超时时间")
    print("  - 实现速率限制")
    print("  - 记录API调用日志")
    
    print("\n2. 提示工程:")
    print("  - 使用模板管理提示")
    print("  - 版本控制提示模板")
    print("  - A/B测试不同提示")
    print("  - 收集和分析提示效果")
    
    print("\n3. 错误处理:")
    print("  - 捕获API异常")
    print("  - 实现降级策略")
    print("  - 提供用户友好的错误信息")
    print("  - 记录错误日志")
    
    print("\n4. 性能优化:")
    print("  - 使用异步调用提高并发")
    print("  - 实现响应缓存")
    print("  - 批量处理请求")
    print("  - 监控API使用情况")
    
    print("\n5. 安全考虑:")
    print("  - 保护API密钥")
    print("  - 验证用户输入")
    print("  - 防止提示注入")
    print("  - 限制API调用频率")
    
    print()


if __name__ == "__main__":
    # 运行所有演示
    demo_api_call_pattern()
    demo_prompt_engineering()
    demo_data_processing_pipeline()
    demo_simple_llm_app()
    demo_best_practices()
    
    print("=" * 50)
    print("演示完成！")
    print("=" * 50)

