import os

import openai


def test_openai_completion():
    prompt = "Hello world"
    model_name = os.environ.get("OPENAI_DEFAULT_MODEL", "gpt-3.5-turbo")
    completion = openai.chat.completions.create(model=model_name, messages=[{"role": "user", "content": prompt}])
    assert completion.choices[0].finish_reason == "stop"
    print(completion.choices[0].message.content)
