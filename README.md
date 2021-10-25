# Sample streamlit UI

## Local development env

```bash
conda create --name streamlit python=3.8
conda activate streamlit
pip install -r requirements.txt
streamlit run app/app.py 
```

## Docker development env: UI

```bash
docker build -t ui_template:latest .
docker run -p 80:8501 ui_template:latest
```

