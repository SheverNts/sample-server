FROM python:slim-bullseye
EXPOSE 80
COPY app/*.py ./
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python3", "app.py" ]