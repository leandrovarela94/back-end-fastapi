# Imagem base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos Pipfile e Pipfile.lock para o diretório de trabalho
COPY Pipfile Pipfile.lock /app/

# Instala o pipenv
RUN pip install pipenv

# Instala as dependências do projeto
RUN pipenv install --system --deploy

# Copia o restante dos arquivos do projeto para o diretório de trabalho
COPY . /app

# Comando de execução do container
CMD ["python", "app.py"]

