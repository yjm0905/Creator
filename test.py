import os
import logging
from datetime import datetime
from openai import OpenAI

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'api_calls_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

logger.info("初始化OpenAI客户端...")
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key="sk-05324fe54e7c479bb7c2a950f63c25a7",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

logger.info("发送API请求...")
try:
    completion = client.chat.completions.create(
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你是谁？"},
        ]
    )
    response_json = completion.model_dump_json()
    logger.info(f"API请求成功，响应长度: {len(response_json)}")
    print(response_json)
except Exception as e:
    logger.error(f"API请求失败: {str(e)}", exc_info=True)
