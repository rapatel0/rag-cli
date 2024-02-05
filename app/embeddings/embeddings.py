# Placeholder for embedding generation logic
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("Salesforce/SFR-Embedding-Mistral")
model = AutoModel.from_pretrained("Salesforce/SFR-Embedding-Mistral")

def generate_embedding_for_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embeddings

