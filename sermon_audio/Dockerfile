FROM --platform=linux/arm64 python:3.12

WORKDIR /src

COPY ./requirements.txt /src/
COPY ./src/__init__.py /src/
COPY ./src/google_drive.py /src/
COPY ./src/process_services_gsheet.py /src/
COPY ./src/upload_services_to_sa.py /src/

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["python", "process_services_gsheet.py"]