# Use official Python image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]

# docker ps, docker images
# docker build -t my-streamlit-app . or docker build -t python_app .
# docker run -p 8501:8501 my-streamlit-app or docker run python_app:latest
# map the ports of local host and docker container - docker run -dp 127.0.0.1:8501:8501 python_app:latest
# To run the app, navigate to http://localhost:8501 in your web browser