#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import sys

model_name = sys.argv[1]
prompts = sys.argv[2:]


# In[ ]:


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


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


import time

result = ""

for i, prompt in enumerate(prompts):
    t = time.time()
    response = generate_response(prompt)

    print(f"Prompt {i}: {prompt}", end="\n\n")
    print(f"Response {i}: {response}", end="\n\n")
    print(f"Time taken: {time.time() - t:.2f}s", end="\n\n\n")

    result += f"=== Prompt ===\n{prompt}\n\n"
    result += f"=== Response ===\n{response}\n\n\n"


# In[ ]:

output_file = "/srv/response.txt"
print(f"Output file: {output_file}")

with open(output_file, "w") as f:
    f.write(result)
