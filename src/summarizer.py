from .model import load_model
from .beam_search import summarize_with_beam_search
from .config import BEAM_WIDTH, MAX_LENGTH

def summarize(text):
    tokenizer, model = load_model()
    return summarize_with_beam_search(model, tokenizer, text, BEAM_WIDTH, MAX_LENGTH)
