FROM python:3.9
ADD ./ generator.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python3" "./generator.py"]