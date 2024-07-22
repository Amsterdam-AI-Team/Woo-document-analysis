"""Module to handle openai calls"""
from openai import AzureOpenAI


def get_client(API_KEY, RESOURCE_ENDPOINT):
    client = AzureOpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=API_KEY,
        api_version="2023-05-15",
        azure_endpoint=RESOURCE_ENDPOINT,
    )
    return client


def prompt_gpt(client, prompt, context=None, system=None, max_tokens=200):
    conversation = []

    if system:
        conversation.append({"role": "system", "content": system})

    if context:
        conversation.append({"role": "system", "content": context})

    conversation.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=conversation,
        max_tokens=max_tokens,
        temperature=0.25,
        top_p=0.3,
        # top_k=20,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )

    finish_reason = response.choices[0].finish_reason
    if finish_reason != "stop":
        print(finish_reason)

    return response.choices[0].message.content
