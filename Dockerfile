FROM python:3
WORKDIR /app
RUN { \
      echo ''; \
    } > /app/requirements.txt \
 && { \
      echo ''; \
    } > /app/libs.py \
 && pip install --upgrade pip \
 && pip install -r /app/requirements.txt \
 && python /app/libs.py \
 && rm -rf /app/requirements.txt /app/libs.py