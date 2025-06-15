FROM python:3.11.9
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python", "main.py"]