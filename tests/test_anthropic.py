import os
import sys

import anthropic


def test_claude():
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model="claude-3-opus-20240229", max_tokens=1024, messages=[{"role": "user", "content": "Hello, Claude"}]
    )
    print(message.content)
    print(sys.argv)
