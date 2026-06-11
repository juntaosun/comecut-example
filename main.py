# ======================================================
# 这是一个 ComeCut 使用的 python 扩展插件示例项目
# ======================================================

class ExamplePlugin:
    
    CATEGORY = "other/example"   # 大类/子类, 例如: audio/asr 或者 audio/tts
    NAME = "示例插件项目"         # 您的插件名称, 显示在插件列表中
    VERSION = "0.0.1"            # 插件版本号, 例如: "1.2.0"
    AUTHOR = "ComeCut"           # 您的插件作者, 作者名称
    GITHUB = None                # 例如: "https://github.com/user/repo"
    
    # 定义输入参数类型
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_name": ("STRING", {"default": "ComeCut 测试"}),
                "count": ("INT", {"default": 1, "min": 1, "max": 10})
            }
        }

    # 定义返回值和类型
    RETURN_TYPES = ("STRING",)

    # 扩展被调用的方法 -- 包括约定的输入参数
    def run(self, user_name, count, **kwargs):
        
        # 处理您的数据
        result = f"你好 {user_name}! 这是来自 Python 插件的消息。重复次数: {count}"
        
        # 返回您的结果
        return result

