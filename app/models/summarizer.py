# summerizer
from transformers import pipeline

class Summarizer:
    def __init__(self, model="facebook/bart-large-cnn"):
        self.device = "cuda"
        self.model = pipeline("summarization", model)
    
    def txt2img(self, ARTICLE:str):
        # summarize
        prompt = self.model(ARTICLE, max_length=10, min_length=3, do_sample=False)[0].get('summary_text')
        
        return prompt