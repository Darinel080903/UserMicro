FROM continuumio/miniconda3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "your-env-name", "/bin/bash", "-c"]

COPY . /code/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]