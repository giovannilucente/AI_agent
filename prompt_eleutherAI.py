# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# def prompt_llm(prompt, model_name="EleutherAI/gpt-neo-1.3B", max_length=300):
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#     # Load tokenizer and model
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForCausalLM.from_pretrained(model_name).to(device)  # move model to GPU if available

#     # Tokenize input prompt and move inputs to device
#     inputs = tokenizer(prompt, return_tensors="pt").to(device)

#     # Generate output tokens
#     outputs = model.generate(
#         **inputs,
#         max_length=max_length,
#         do_sample=True,
#         temperature=0.9,       # slightly more creativity
#         top_p=0.95,            # wider pool of word choices
#         repetition_penalty=1.2,  # discourages repeated phrases
#         eos_token_id=tokenizer.eos_token_id,
#         pad_token_id=tokenizer.eos_token_id,
#     )

#     # Decode tokens to string (move outputs to CPU before decoding)
#     text = tokenizer.decode(outputs[0].cpu(), skip_special_tokens=True)
#     return text

# if __name__ == "__main__":
#     prompt_text = """If A implies B and C implies A then C implies B?"""
#     response = prompt_llm(prompt_text)
#     print("Response:\n", response)