# Imagem base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos Pipfile e Pipfile.lock para o diretório de trabalho
COPY Pipfile Pipfile.lock ./

# Instala o pipenv
RUN pip install pipenv

# Instala as dependências do projeto
RUN pipenv install --system --deploy

# Copia apenas o arquivo Python principal para o diretório de trabalho
COPY app.py ./

# Comando de execução do container
CMD ["python", "app.py"]
