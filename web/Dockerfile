FROM python:3.8-slim
RUN pip install flask requests
RUN useradd -ms /bin/bash user
WORKDIR /app
COPY * /app
USER user
CMD ["chown","user:user","/mirror","/json"]
CMD ["python3", "web.py"]
