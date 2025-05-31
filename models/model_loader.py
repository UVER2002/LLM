from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import bitsandbytes

from config import MODEL_ID

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, device_map="auto", load_in_4bit=True
    )
    return model, tokenizer
