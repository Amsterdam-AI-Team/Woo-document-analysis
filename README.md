# RAG for open.amsterdam

By experimenting with AI technologies with significant potential impact on the City of Amsterdam, we learn about their capabilities, potential value, performance, and side effects. ​
Recently, we researched the use of **Retrieval Augmented Generation within the municipal context**, and more specifically, for **answering citizens' questions on the [open.amsterdam](https://open.amsterdam/) website**. 
This repository contains the corresponding code.

## Woo Background

The Open Government Act (Wet Open Overheid, WOO) requires governmental organizations to disclose information actively.
Documents published by the City of Amsterdam can currently be found on 
[https://open.amsterdam/](https://open.amsterdam/),
[https://amsterdam.raadsinformatie.nl/](https://amsterdam.raadsinformatie.nl/)
and [https://openresearch.amsterdam/](https://openresearch.amsterdam/).

While information is now publicly available, searching and interpreting the corresponding documents can be a challenging task for citizens.
We researched how Retrieval Augmented Generation (RAG) can help us **increase transparency, inclusivity, user-friendliness and efficiency** by allowing citizens to ask questions about publicly available documents in natural language.​

The **final report** for the project can be found **on openresearch** in [English](https://openresearch.amsterdam/en/page/110995/rag-for-open.amsterdam%E2%80%8B) and [Dutch](https://openresearch.amsterdam/nl/page/110995/rag-for-open.amsterdam%E2%80%8B).


## Folder Structure

* [`data`](./data): Sample data for demo purposes
* [`notebooks`](./notebooks): contains examples of the RAG pipeline using [`llama-index`](./notebooks/llama_index.ipynb/), [`langchain`](./notebooks/langchain.ipynb/) and [`transformers`](./notebooks/transformers.ipynb/), as well as a comparisong of [`chunking strategies`](./notebooks/chunking.ipynb/)
* [`src`](./src): some LLM helpers

## Installation 

1) Clone this repository:

```bash
git clone https://github.com/Amsterdam-AI-Team/Woo-document-analysis.git
```


The code has been tested with Python 3.9 on Linux. 


## Contributing

Feel free to help out! [Open an issue](https://github.com/Amsterdam-AI-Team/Woo-document-analysis/issues), submit a [PR](https://github.com/Amsterdam-AI-Team/Woo-document-analysis/pulls) or [contact us](https://amsterdamintelligence.com/contact/).

## Acknowledgements

This repository was created by [Amsterdam Intelligence](https://amsterdamintelligence.com/) for the [open.amsterdam](https://open.amsterdam/) and the City of Amsterdam.

## License 

This project is licensed under the terms of the European Union Public License 1.2 (EUPL-1.2).
