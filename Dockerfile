# To deploy the flask application we will use official python Image
# Includes OS as well

FROM python:3.9

# Next we will set the working directory

WORKDIR /app

# Next we will install Flask aor any other Dependency using PIP

RUN pip install Flask

# NExt we will copy APP.py into the working directory i.e /app

COPY . /app

# NExt we will specify the command to run the flask application

CMD ["python","app.py"]

