# Summarizing News Articles with Beam Search

In this project, Beam Search is used to generate a concise and coherent summary from an input text. Below is a detailed breakdown of how it has been implemented:

### 1. Overview of Beam Search

Purpose: Beam Search is a decoding algorithm used to generate text sequences from models like T5.
How it works: Instead of selecting only the single most probable token at each step (like in greedy search), Beam Search keeps track of the top-k (beam width) most probable sequences at each decoding step.
Why Beam Search? It balances efficiency and accuracy, generating better summaries compared to greedy decoding.

### 2. Where Beam Search is Implemented?
Beam Search is implemented in the beam_search.py file

#### Key Parameters Explained:
##### input_ids
* The input text is prefixed with "summarize:" (as required by T5) and tokenized into input_ids.

##### num_beams=beam_width

* This sets the beam width. For example, if beam_width=5, the algorithm considers the top 5 most probable token sequences at each decoding step.

* ##### max_length
  * The maximum length of the generated summary.
* ##### early_stopping=True
  * Stops generation when all beams have reached an end-of-sequence token.
* ##### no_repeat_ngram_size=2
  * Prevents repeating phrases of length 2 in the generated summary, reducing redundancy.
* ##### model.generate()
  * The model generates possible token sequences using Beam Search and returns the best sequence based on cumulative probabilities.
* ##### tokenizer.decode()
  * The generated token IDs are decoded back into human-readable text.

### 3. How Beam Search Works Step-by-Step in the Project?
* ##### Input Preparation:
  * The text is prefixed with "summarize:" and tokenized into input_ids.

* ##### Beam Search Decoding:
  * At each step, the model generates beam_width possible next tokens.
    
  * It selects the most probable beam_width sequences based on cumulative probabilities.
    
  * This process continues until the maximum length is reached or an end token is encountered.
    
* ##### Sequence Selection:
  
  * The sequence with the highest cumulative probability is selected as the final summary.
    
* ##### Decoding:
  
  * The selected token IDs are decoded into human-readable text.

### 4. Example Run
##### Input Example:
    AI is transforming healthcare, finance, and other industries. While it offers benefits, challenges like ethics and job displacement remain.

##### Beam Search Parameters:
    beam_width = 5
    max_length = 50

##### Output Summary:
    AI is transforming industries, offering benefits, but raising challenges like ethics and job displacement.

### 5. Advantages of Beam Search in this Project
* Better Summaries: Produces more coherent and contextually accurate summaries than greedy search.

* Control Over Quality: Beam width can be tuned to improve results.

* Reduced Repetition: The no_repeat_ngram_size avoids redundant phrases.

* Efficiency: Balances computational cost with output quality.

### Conclusion:
* Beam Width (num_beams) determines the trade-off between performance and computational cost.
* The implementation ensures clean summaries by leveraging early_stopping and no_repeat_ngram_size.
* The summarizer.py acts as the interface to integrate Beam Search logic with the overall pipeline.

## HOW TO RUN 
1. Create a txt file in data/sample_texts/example1.txt file
2. Execute the app.py
3. Output will be captured in data/output/summary1.txt