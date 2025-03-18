class LLMResponse:
    def __init__(self, text: str, model: str = None, usage: dict = None):
        self.text = text
        self.model = model
        self.usage = usage
