FROM python:3.9
RUN pip install yt-dlp
RUN useradd -ms /bin/bash user
WORKDIR /app
COPY * ./
USER user
CMD ["chown", "user:user", "/mirror"]
CMD ["python3", "youtube.py"]
