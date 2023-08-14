FROM python:3.8-slim

RUN useradd -ms /bin/bash user

WORKDIR /home/user

COPY git.py .

RUN chown user:user /home/user

RUN chmod +x /home/user/git.py

CMD ["python3", "/home/user/git.py"] 
