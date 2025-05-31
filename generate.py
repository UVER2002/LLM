from models.model_loader import load_model
from rag_engine import retrieve_context
from transformers import pipeline

model, tokenizer = load_model()
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def ask_nain(user_input):
    context = retrieve_context(user_input)
    prompt = f"""
Tu es le nain du Donjon de Naheulbeuk. Tu es colérique, vulgaire, drôle, toujours prêt à te battre. Tu détestes les elfes et tu adores la bière.

[Contexte] :
{context}

[Utilisateur] : {user_input}
[Nain] :
"""
    output = generator(prompt, max_new_tokens=100, do_sample=True, temperature=0.8)
    return output[0]["generated_text"].split("[Nain] :")[-1].strip()
