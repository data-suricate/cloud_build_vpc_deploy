FROM python:3.9-slim
WORKDIR /app
# Copy the requirements file to the container
COPY requirement.txt .
# Install the Python dependencies
RUN pip install -r requirement.txt
# Copy the Flask application code to the container
COPY . .
# Expose the port on which the Flask API will run
EXPOSE 8080



# Set the environment variables, if needed
ENV MODULE_NAME=main
ENV VARIABLE_NAME=app
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get autoremove -y
RUN apt-get clean


CMD ["fastapi", "run", "main.py", "--port", "8080"]
