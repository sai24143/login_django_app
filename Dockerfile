# Step 1: Use the official Python image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set up the working directory
WORKDIR /app

# Step 4: Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Step 5: Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the Django project files
COPY . /app/

# Step 7: Expose the port
EXPOSE 8000


# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["python", "manage.py", "runserver" "0.0.0.0:8000"]