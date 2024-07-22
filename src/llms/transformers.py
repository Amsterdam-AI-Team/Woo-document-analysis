# import transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def get_model(model_name):
    # TODO: extend
    if model_name == "mistral":
        model_id = "mistralai/Mistral-7B-Instruct-v0.1"
        kwargs = {
            "torch_dtype": torch.bfloat16,
            "device_map": "auto",
        }
        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_id, **kwargs
        )
        tokenizer = AutoTokenizer.from_pretrained(model_id, **kwargs)
    else:
        raise ValueError("only mistral known for now")

    return model, tokenizer


def prompt_open_model(prompt, model, tokenizer, max_tokens=200):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda:0")
    attention_mask = torch.ones(input_ids.shape).to("cuda:0")

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=input_ids.shape[1] + max_tokens,
        do_sample=True,
        temperature=0.6,
        top_p=0.65,
        # top_k=25,
        num_return_sequences=1,
        # num_beams=2,
        no_repeat_ngram_size=3,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
    )

    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response
