from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"  # Replace with the desired model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save the model and tokenizer
model.save_pretrained("/home/pat/AI/model")
tokenizer.save_pretrained("/home/pat/AI/model")
