import requests


def prompt_open_azure_model(prompt, api_url, api_key, model_deployment, max_new_tokens=200):
    headers = {
        "Content-Type": "application/json",
        # 'Authorization':('Bearer '+ sc.AZURE_HUGGINGFACE_CONFIG[model]["api_key"]),
        "Authorization": ("Bearer " + api_key),
        # 'azureml-model-deployment': sc.AZURE_HUGGINGFACE_CONFIG[model]["azureml-model-deployment"]
        "azureml-model-deployment": model_deployment,
    }

    data = {
        "input_data": {
            "input_string": [
                {"role": "user", "content": prompt},
            ],
            "parameters": {
                "max_new_tokens": max_new_tokens,
                "do_sample": True,
                "temperature": 0.25,
                "top_p": 0.3,
                "top_k": 20,
                "num_return_sequences": 1,
                # "num_beams": 2,
                "no_repeat_ngram_size": 3,
                # "eos_token_id": tokenizer.eos_token_id,
                # "pad_token_id": tokenizer.eos_token_id,
                "return_full_text": False,
                "wait_for_model": True,
            },
        }
    }

    response = requests.post(api_url, headers=headers, json=data).json()
    # print(f"Response {response}")
    # response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response["output"]
