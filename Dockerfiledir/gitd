FROM python:3.8
RUN pip install requests
RUN apt-get update && apt-get install -y httrack
RUN useradd -ms /bin/bash user
WORKDIR /app
COPY * ./
USER user
CMD ["chown","user:user","/mirror"]
CMD ["chown","user:user","/json"]
CMD ["python3", "git.py"]
