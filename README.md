# Llama LLM webservice

# install pip dependencies
- `conda create -y --name torch python=3.11.8`
- `conda activate torch`

# build
- `pip install -r requirements.txt`
-  in shell: `python install.py`


# install manually (optional)
- `conda install pytorch torchvision torchaudio -c pytorch-nightly`
- `pip install Flask Flask-WTF`
- `pip install werkzeug`
- `pip install "sympy==1.13.1,<1.13.3"`
- `pip install mlx-lm`
- `pip install --upgrade --quiet  mlx-lm transformers huggingface_hub`
- `pip install langchain_community`

# run server
- `conda activate torch`
- `python app.py`