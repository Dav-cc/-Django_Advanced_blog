# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE = 1
# ENV PYTHONNONBUFFRED = 1

# WORKDIR /app

# COPY requirements.txt /app/

# RUN pip3 install -r requirements.txt

# COPY ./core /app/

# CMD [ "python3" , "manage.py" , "runserver", "0.0.0.0:8000" ]