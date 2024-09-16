# Encrypted File Upload Service

This is a Django-based file upload service that accepts a file, encrypts it, and stores it either in the file system or Amazon S3.

## Project Structure

- `app/app/`: Contains the Django configuration files.
- `app/fs/`: Manages file storage in either the local file system or Amazon S3.
- `app/logic/core/`: Contains the core encryption logic and file-system lower order functions.
- `app/logic/handlers/`: Contains the business logic for handling file uploads.
- `app/routers/`: Handles the routing for file upload views.
- `app/manage.py`: Main entry point to start the Django server.
- `app/configs` : Used to read server env parameters
- `file_system` : Is a folder used to store encrypted file locally

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/TngPrag/secure_file_storage.git
   cd secure_file_storage/

2. Create a python virtual environment to avoid dependency conflict and activate it
   
   sudo python3 -m venv myenv
   
   source myenv/bin/activate

3. Install requirements/dependencies
   
   sudo pip install -r requirements.txt

4. Start the server
   
   python3 app/manage.py runserver