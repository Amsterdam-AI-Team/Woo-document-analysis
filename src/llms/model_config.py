from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

KNOWN_EMBED_MODELS = ["bert", "robbert", "me5", "me5-instruct", "cohere", "ada"]


def get_embed_model_info(model_name):
    if model_name == "ada":
        raise NotImplementedError("ada WIP")
        # chunk_size = 8191
        # chunk_size = 1024 # -> way too slow
        # chunk_size = 4096
        # tokenizer = tiktoken.get_encoding("cl100k_base").encode
        chunk_size = 512

    elif model_name == "bert":
        model_id = "jegormeister/bert-base-dutch-cased-snli"
        chunk_size = 512

    elif model_name == "robbert":
        model_id = "NetherlandsForensicInstitute/robbert-2022-dutch-sentence-transformers"
        chunk_size = 128

    elif model_name == "cohere":
        model_id = "Cohere/Cohere-embed-multilingual-v3.0"
        chunk_size = 512

    elif model_name == "me5":
        model_id = "intfloat/multilingual-e5-large"
        chunk_size = 512

    elif model_name == "me5-instruct":
        model_id = "intfloat/multilingual-e5-large-instruct"
        chunk_size = 512

    else:
        raise ValueError(
            f"Unknown model {model_name}. Known models: ada, bert, robbert, cohere, me5"
        )

    # tokenizer = tiktoken.get_encoding("cl100k_base").encode

    # return model, tokenizer, chunk_size
    return model_id, chunk_size


def get_embed_model(model_name):
    model_id, chunk_size = get_embed_model_info(model_name)
    model = SentenceTransformer(model_id)
    return model, chunk_size


def get_embed_tokenizer(model_name):
    model_id, chunk_size = get_embed_model_info(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return tokenizer, chunk_size
