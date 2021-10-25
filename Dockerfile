FROM python:3.9-slim-buster as builder
ENV PIP_NO_CACHE_DIR=1
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt-get clean
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /requirements.txt && \
    rm -rf /root/.cache/pip


FROM python:3.9-slim-buster
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
RUN mkdir -p /root/.streamlit
EXPOSE 8501
WORKDIR /app
COPY /app /app
# RUN cp config.toml ~/.streamlit/config.toml
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py","--server.enableWebsocketCompression=false"]