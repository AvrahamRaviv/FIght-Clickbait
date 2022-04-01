import trafilatura
from transformers import pipeline
# Reading the context from URL and convert into string
context = trafilatura.extract(trafilatura.fetch_url("YOUR URL HERE"))
# Note: The specified maximum sequence length for this model is 1024.
# The function pipeline() can get more parameters, for example:
# summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")
summarizer = pipeline("summarization")
# The function summarizer() can get more parameters, for example:
# summarizer(context, max_length=130, min_length=60)
print(summarizer(context))
