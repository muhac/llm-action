#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")


# In[ ]:


def generate_response(prompt, max_length=100):
    """
    Generate text response using the DeepSeek model

    Args:
        prompt (str): Input text to generate from
        max_length (int): Maximum length of generated text

    Returns:
        str: Generated text response
    """
    try:
        # Encode the input text
        inputs = tokenizer(prompt, return_tensors="pt", padding=True)

        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                inputs["input_ids"],
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
            )

        # Decode the generated text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return None


# In[ ]:


prompt = "Hello, how are you?"
response = generate_response(prompt)
print(f"Prompt: {prompt}")
print(f"Response: {response}")


# In[ ]:
