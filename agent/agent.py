from llm import extract_structure, fix_dsl
from dsl import to_dsl

class Agent:
    def __init__(self, executor):
        self.executor = executor

    def run(self, text):
        data = extract_structure(text)
        dsl = to_dsl(data)

        for i in range(3):  # максимум 3 попытки
            try:
                print(f"Попытка {i+1}")
                self.executor.run(dsl)
                return "OK"
            except Exception as e:
                print("Ошибка:", e)
                dsl = fix_dsl(dsl, str(e))

        return "FAILED"
		