

# STEPS TO RUN THE APPLICATION

# Clone the repository

    git clone https://github.com/kunalwagh101/brainlabs.git

# Create a virtual environment

**For Linux and macOS**

 ```bash
    python3.8 -m venv venv
    source venv/bin/activate
 ```

**For Windows**
```bash
    pip install virtualenv
    python -m venv venv
    virtualenv venv
    venv/Scripts/activate
```


# Install the necessary modules
```bash
    pip install -r requirements.txt
```


# run the migration commands 
```bash
    python manage.py makemigration
    python manage.py migrate
```


# Run the application



**run server using below command**



  ```bash
    python manage.py runserver
  ```

# Open the below url on your browser

```bash
     http://127.0.0.1:8000/
```


