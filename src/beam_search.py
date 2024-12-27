import torch

def summarize_with_beam_search(model, tokenizer, text, beam_width, max_length):
    input_text = "summarize: " + text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True)

    summary_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_beams=beam_width,
        early_stopping=True,
        no_repeat_ngram_size=2
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
