from transformers import T5Tokenizer, T5ForConditionalGeneration
from .config import MODEL_NAME

def load_model():
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
    return tokenizer, model
