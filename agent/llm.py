from openai import OpenAI
import json

client = OpenAI()

def extract_structure(text: str):
    response = client.chat.completions.create(
        model="gpt-5.3",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
Ты — системный архитектор.

Извлеки:
- system
- components
- external_systems
- interactions

Верни JSON.
"""
            },
            {"role": "user", "content": text[:12000]}
        ]
    )
    return json.loads(response.choices[0].message.content)


def fix_dsl(dsl, error):
    response = client.chat.completions.create(
        model="gpt-5.3",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Исправь DSL модели"
            },
            {
                "role": "user",
                "content": f"""
DSL:
{json.dumps(dsl, ensure_ascii=False)}

Ошибка:
{error}

Исправь и верни JSON.
"""
            }
        ]
    )

    return json.loads(response.choices[0].message.content)
