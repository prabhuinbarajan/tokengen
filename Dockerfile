FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["-m" , "tokengen.token_generator_app"]
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
