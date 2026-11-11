# Learning Plan: Python for AI

## Core Python still to cover
- [ ] Lists, tuples, sets, and slicing
- [ ] List and dict comprehensions, generators
- [ ] Functions: `*args`, `**kwargs`, type hints, decorators
- [ ] Classes and dataclasses
- [ ] Error handling with try/except
- [ ] File I/O: JSON, CSV, JSONL
- [ ] Modules, virtual environments, pip
- [ ] async/await (LLM API calls are often async)

## Data libraries
- [ ] numpy: arrays and vector math (embeddings, similarity)
- [ ] pandas: loading and cleaning datasets
- [ ] matplotlib: charts (you already have `weather_chart.png`)

## Working with APIs
- [ ] requests or httpx for HTTP calls
- [ ] Environment variables and `.env` files for API keys (never put keys in code)
- [ ] Retries, rate limits, and timeouts

## AI-specific tools
- [ ] An LLM SDK (OpenAI, Anthropic, or Bedrock via boto3)
- [ ] Tokenization (tiktoken) and embeddings
- [ ] pydantic for validating structured model output
- [ ] Prompting, RAG basics, and tool calling
- [ ] Vector stores (FAISS, Chroma)
- [ ] Hugging Face transformers for local models
- [ ] scikit-learn for classic ML (train/test split, metrics)

## Suggested order
1. Finish the core Python items above (lists, functions, classes, files, errors).
2. numpy and pandas.
3. Call an LLM API with requests, then with an SDK.
4. Embeddings, then a small RAG project.
5. Optionally scikit-learn and transformers.
