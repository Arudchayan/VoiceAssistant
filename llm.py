from decouple import config
from transformers import pipeline

_MODEL_NAME = config('HF_MODEL', default='distilgpt2')
_generator = pipeline('text-generation', model=_MODEL_NAME)

def generate_response(prompt: str, max_length: int = 50) -> str:
    """Generate a text response using the configured HuggingFace model."""
    result = _generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text'].strip()
