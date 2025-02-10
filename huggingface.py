#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys

model_name = sys.argv[1]
prompt = sys.argv[2]

if len(sys.argv) > 3:
    output_file = sys.argv[3]
else:
    output_file = "response.txt"

output_file = os.path.join("/srv", output_file)


# In[ ]:


print(f"Model: {model_name}")
print(f"Prompt: {prompt}")


# In[ ]:


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)


# In[ ]:


def generate_response(prompt, max_length=256):
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


response = generate_response(prompt)

print(f"Response: {response}")
print(f"Output file: {output_file}")


# In[ ]:


with open(output_file, "w") as f:
    f.write(response)
