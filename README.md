# Llama LLM webservice
 - download and install miniconda from website: https://docs.anaconda.com/miniconda/

# install torch environment
- `conda create -y --name torch python=3.11.8`
- `conda activate torch`

# install pip dependencies
- `pip install -r requirements.txt`
-  in shell download the model initially: `python install.py`

# run server
- `conda activate torch`
- `python app.py`

# install manually (optional)
- `conda install pytorch torchvision torchaudio -c pytorch-nightly`
- `pip install Flask Flask-WTF`
- `pip install werkzeug`
- `pip install "sympy==1.13.1,<1.13.3"`
- `pip install mlx-lm`
- `pip install --upgrade --quiet  mlx-lm transformers huggingface_hub`
- `pip install langchain_community`