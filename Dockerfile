# 1. Python
# 2. app.py , demo.py, requirements.txt
# 3. install packages
# 4. streamlit run app.py

FROM python:3

WORKDIR C:/Users/MY PC/Downloads/Trash/hello-world            # Set the working directory in the container

COPY requirements.txt ./        # Copy the requirements file to the container
RUN pip install --no-cache-dir -r requirements.txt    # Install the required packages

COPY . .                        # Copy all files in the current directory to the container

CMD ["streamlit", "run", "app.py"]   # Command to run the Streamlit app
