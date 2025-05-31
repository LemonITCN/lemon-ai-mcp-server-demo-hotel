class PromptService:

    def get_system_prompt(self):
        """
        获取系统提示词
        :return: 提示词字符串
        """
        file_path = "prompt/system-prompt.md"

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
