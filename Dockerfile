#
FROM python:3.10-slim

#
WORKDIR /code

#
COPY requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python3 -m pip install --upgrade setuptools
#
COPY ./main.py /code/

ENV PORT 8000

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

# docker build -t fast .
# docker run -p 8000:8000 -t fast
