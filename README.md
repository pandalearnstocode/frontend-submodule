# Sample streamlit UI

## Local development env

```
conda create --name streamlit python=3.8
conda activate streamlit
streamlit run app/app.py 
```

## Docker development env: UI

```
docker build -t ui_template:latest .
docker run -p 80:8501 ui_template:latest
```

