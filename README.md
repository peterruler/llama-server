# Llama LLM webapp
 - download and install miniconda from website: https://docs.anaconda.com/miniconda/

# install torch environment
- `conda create -y --name torch python=3.11.8`
- `conda activate torch`

# install pip dependencies (on M1 Mac)
- `pip install -r requirements.txt`
-  in shell download the model initially: `python install.py`

# run server
- `conda activate torch`
- `python app.py`

# install manually (optional)
- `conda install pytorch torchvision torchaudio -c pytorch-nightly`
- `pip install Flask==2.0.3`
- `pip install Flask-WTF==0.15.1`
- `pip install Werkzeug==2.0.3`
- `pip install --upgrade --quiet  huggingface_hub`
- `pip install mlx==0.17.3`
- `pip install mlx-lm==0.18.2`
- `pip install transformers==4.44.2`
- `pip install langchain-community==0.0.34`
- `pip install langchain-core==0.1.46`
- `pip install langchain-text-splitters==0.0.1`
