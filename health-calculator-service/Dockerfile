FROM python:3.12-alpine

ENV DEBUG=False
ENV PORT=80

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE $PORT

RUN adduser -D flask

USER flask

ENTRYPOINT ["python"]
CMD ["app.py"]