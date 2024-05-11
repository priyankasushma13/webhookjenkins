#To deploy the flask application we will use offcial pythonimage.
FROM python:3.9
# next, we will set the working directory in the container
WORKDIR /app 
# next will install flask or any other dependency using pip
RUN pip install Flask
# next week next week will copy app.PY into working directory
COPY . /app
CMD ["python","app.py"]
