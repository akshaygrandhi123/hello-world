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
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker build -t my-streamlit-app .
# docker run -p 8501:8501 my-streamlit-app
# To run the app, navigate to http://localhost:8501 in your web browser