# LLM in GitHub Actions

This repository contains the code to run LLMs for inference in GitHub Actions.

`Qwen/Qwen2.5-3B-Instruct` is recommended for the best performance and speed. If you want to use a reasoning model, `Qwen/Qwen3-1.7B` is a good starting point, as larger models are slower at thinking.

For latest models, checkout [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/?params=-1%2C6&official=true). Newer versions of vllm and transformers may support more models.

The largest size of the model that can be run in GitHub Actions is `6B`. `7B` models are too large to run in the current environment.
The limit is due to [the memory constraints](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#standard-github-hosted-runners-for-public-repositories) of the GitHub Actions environment.

In extreme cases, you may run quantized `8B` (even `14B`) models to support advanced reasoning tasks. But the time will be extremely long and the workflow may be unstable.
