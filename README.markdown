# HumanChain AI Safety Incident Log API

This is a RESTful API service for logging and managing hypothetical AI safety incidents, built as a take-home assignment for HumanChain's Backend Intern position. The service allows users to create, retrieve, and delete AI safety incident records stored in a MySQL database, adhering to REST principles with proper request/response handling, input validation, and error handling.

## Project Overview
- **Language**: Python 3.9+
- **Framework**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Features**:
  - CRUD operations for AI safety incidents via RESTful API endpoints.
  - Input validation for creating incidents (e.g., required fields, valid severity levels).
  - Error handling with appropriate HTTP status codes and messages.
  - Initial data population with sample incidents.
  - JSON request/response handling for all endpoints.

## File Structure
The project directory contains the following files:
- `app.py`: The main Flask application with API endpoint implementations.
- `models.py`: SQLAlchemy model definition for the `Incident` table.
- `requirements.txt`: Python dependencies required for the project.
- `init_db.py`: Script to initialize the database and populate sample incidents.
- `schema.sql`: SQL script to create the `humanchain` database in MySQL.
- `README.md`: This file, providing setup and usage instructions.

## Prerequisites
Before setting up the project, ensure you have the following installed:
- **Python 3.9 or higher**: Download from [python.org](https://www.python.org/downloads/) or install via a package manager (e.g., `brew install python` on macOS, `sudo apt-get install python3` on Ubuntu).
- **MySQL Server**: Install MySQL Community Server:
  - Windows: Use MySQL Installer from [mysql.com](https://dev.mysql.com/downloads/installer/).
  - macOS: `brew install mysql`.
  - Linux: `sudo apt-get install mysql-server` (Ubuntu) or equivalent for your distribution.
- **pip**: Python package manager (included with Python).
- **curl**: For testing API endpoints (optional, can use Postman or similar tools).
- **Git** (optional): If cloning from a repository.
- A code editor like **VSCode** is recommended for editing files.

## Setup Instructions

### 1. Obtain the Project
- **Option 1: Zip File**
  - Extract the provided `humanchain-ai-safety.zip` file to a directory (e.g., `~/humanchain-ai-safety`).
- **Option 2: Git Repository**
  - Clone the repository (if provided):
    ```bash
    git clone <repository-url>
    cd humanchain-ai-safety
    ```

### 2. Set Up MySQL
The project uses MySQL as the database. Follow these steps to configure it:

1. **Start MySQL Server**:
   - Ensure MySQL is running:
     - Windows: Start the MySQL service via Services or MySQL Installer.
     - macOS: `brew services start mysql`.
     - Linux: `sudo service mysql start`.
   - Verify MySQL is running:
     ```bash
     mysqladmin -u root -p status
     ```
     Enter your MySQL root password when prompted.

2. **Create the Database**:
   - Log in to MySQL as the root user:
     ```bash
     mysql -u root -p
     ```
     Enter your root password.
   - Run the `schema.sql` script to create the `humanchain` database:
     ```sql
     SOURCE /path/to/humanchain-ai-safety/schema.sql;
     ```
     Alternatively, copy-paste the contents of `schema.sql`:
     ```sql
     CREATE DATABASE IF NOT EXISTS humanchain;
     USE humanchain;
     ```
   - Verify the database exists:
     ```sql
     SHOW DATABASES;
     ```
     You should see `humanchain` in the list. Exit MySQL with `EXIT;`.

3. **Note on MySQL Credentials**:
   - The project assumes the MySQL root user with password `root`. If your root password is different, update the `SQLALCHEMY_DATABASE_URI` in `app.py` (see Step 4).
   - Optionally, create a dedicated MySQL user (uncomment and adjust the user creation commands in `schema.sql`).

### 3. Install Python Dependencies
1. Navigate to the project directory:
   ```bash
   cd /path/to/humanchain-ai-safety
   ```
2. Create a virtual environment (recommended to isolate dependencies):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   You should see `(venv)` in your terminal prompt.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   This installs Flask, Flask-SQLAlchemy, and PyMySQL as specified in `requirements.txt`.

### 4. Configure Database Connection
The database connection is configured in `app.py` via the `SQLALCHEMY_DATABASE_URI`. The default URI is:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/humanchain'
```
- **Username/Password**: `root:root` assumes the MySQL root user with password `root`. If your root password is different (e.g., `mypassword`), edit `app.py`:
  ```python
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@127.0.0.1:3306/humanchain'
  ```
- **Host/Port**: `127.0.0.1:3306` assumes MySQL is running on localhost with the default port. Update if your setup differs.
- **Database**: `humanchain` must match the database created in Step 2.

Open `app.py` in VSCode and update the URI if needed.

### 5. Initialize the Database
Run the `init_db.py` script to create the `incidents` table and populate it with sample data:
```bash
python init_db.py
```
- This script creates the table defined in `models.py` and adds three sample incidents:
  - "Unexpected AI Behavior" (Medium severity)
  - "Data Leakage" (High severity)
  - "Minor Processing Delay" (Low severity)
- If the database already contains incidents, the script skips population to avoid duplicates.
- Expected output:
  ```
  Database initialized with sample incidents.
  ```
- If you encounter errors:
  - `Access denied`: Check the username/password in the URI.
  - `Unknown database 'humanchain'`: Ensure the database was created (Step 2).
  - `Can't connect to MySQL server`: Verify MySQL is running on `127.0.0.1:3306`.

### 6. Run the Application
Start the Flask development server:
```bash
python app.py
```
- The API will be available at `http://localhost:5000`.
- You should see output indicating the server is running:
  ```
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```
- Keep the terminal open while testing the API.

## API Endpoints
The API provides four endpoints for managing AI safety incidents. All endpoints expect and return JSON where applicable. Below are the details and example `curl` commands for testing.

### 1. GET /incidents
Retrieve all incidents stored in the database.
- **Method**: GET
- **URL**: `http://localhost:5000/incidents`
- **Response**: 200 OK with a JSON array of incident objects.
- **Example**:
  ```bash
  curl http://localhost:5000/incidents
  ```
  ```json
  [
      {
          "id": 1,
          "title": "Unexpected AI Behavior",
          "description": "AI model generated inappropriate content during testing.",
          "severity": "Medium",
          "reported_at": "2025-04-26T12:00:00.000000"
      },
      {
          "id": 2,
          "title": "Data Leakage",
          "description": "Sensitive user data was exposed due to misconfiguration.",
          "severity": "High",
          "reported_at": "2025-04-26T12:00:00.000000"
      },
      {
          "id": 3,
          "title": "Minor Processing Delay",
          "description": "AI inference took longer than expected under heavy load.",
          "severity": "Low",
          "reported_at": "2025-04-26T12:00:00.000000"
      }
  ]
  ```

### 2. POST /incidents
Log a new incident to the database.
- **Method**: POST
- **URL**: `http://localhost:5000/incidents`
- **Request Body**: JSON object with `title`, `description`, and `severity` (must be "Low", "Medium", or "High").
  ```json
  {
      "title": "New Incident",
      "description": "Detailed description here.",
      "severity": "Medium"
  }
  ```
- **Response**:
  - 201 Created with the created incident (including auto-generated `id` and `reported_at`).
  - 400 Bad Request if validation fails (e.g., missing fields, invalid severity).
- **Example**:
  ```bash
  curl -X POST http://localhost:5000/incidents \
       -H "Content-Type: application/json" \
       -d '{"title":"New Incident","description":"Detailed description here.","severity":"Medium"}'
  ```
  ```json
  {
      "id": 4,
      "title": "New Incident",
      "description": "Detailed description here.",
      "severity": "Medium",
      "reported_at": "2025-04-26T12:05:00.000000"
  }
  ```
- **Error Example** (invalid severity):
  ```bash
  curl -X POST http://localhost:5000/incidents \
       -H "Content-Type: application/json" \
       -d '{"title":"Invalid","description":"Test","severity":"Critical"}'
  ```
  ```json
  {"error": "Severity must be one of ['Low', 'Medium', 'High']"}
  ```

### 3. GET /incidents/{id}
Retrieve a specific incident by its ID.
- **Method**: GET
- **URL**: `http://localhost:5000/incidents/1`
- **Response**:
  - 200 OK with the incident details.
  - 404 Not Found if the ID doesn't exist.
- **Example**:
  ```bash
  curl http://localhost:5000/incidents/1
  ```
  ```json
  {
      "id": 1,
      "title": "Unexpected AI Behavior",
      "description": "AI model generated inappropriate content during testing.",
      "severity": "Medium",
      "reported_at": "2025-04-26T12:00:00.000000"
  }
  ```
- **Error Example** (non-existent ID):
  ```bash
  curl http://localhost:5000/incidents/999
  ```
  ```json
  {"error": "Incident not found"}
  ```

### 4. DELETE /incidents/{id}
Delete an incident by its ID.
- **Method**: DELETE
- **URL**: `http://localhost:5000/incidents/1`
- **Response**:
  - 200 OK with a confirmation message.
  - 404 Not Found if the ID doesn't exist.
- **Example**:
  ```bash
  curl -X DELETE http://localhost:5000/incidents/1
  ```
  ```json
  {"message": "Deleted successfully"}
  ```
- **Error Example** (non-existent ID):
  ```bash
  curl -X DELETE http://localhost:5000/incidents/999
  ```
  ```json
  {"error": "Incident not found"}
  ```

## Testing the API
To test the API:
1. Ensure the Flask server is running (`python app.py`).
2. Use the `curl` commands above in a terminal.
3. Alternatively, use a tool like **Postman**:
   - Set the HTTP method (GET, POST, DELETE).
   - Enter the URL (e.g., `http://localhost:5000/incidents`).
   - For POST, add a JSON body and set the `Content-Type: application/json` header.
4. Verify responses match the expected JSON and status codes.

## Design Decisions
- **Language/Framework**: Python with Flask was chosen for its simplicity, rapid development, and robust ecosystem, ideal for a small-scale REST API.
- **Database**: MySQL was selected for its reliability, widespread use, and compatibility with SQLAlchemy, making it suitable for a production-like environment.
- **ORM**: SQLAlchemy simplifies database interactions, provides portability across databases, and handles schema creation automatically.
- **Input Validation**: Strict validation ensures:
  - Required fields (`title`, `description`, `severity`) are present.
  - `title` and `description` are non-empty strings.
  - `severity` is one of `Low`, `Medium`, or `High`.
- **Error Handling**: Uses standard HTTP status codes (200, 201, 400, 404) with descriptive JSON error messages to enhance usability.
- **Sample Data**: The `init_db.py` script populates three sample incidents to facilitate testing without manual data entry.
- **DELETE Response**: Returns `200 OK` with `{"message": "Deleted successfully"}` (instead of `204 No Content`) to provide clear confirmation of deletion, as allowed by the assignment.
- **Datetime Handling**: Uses `isoformat()` for `reported_at` in JSON responses to ensure consistent, standards-compliant timestamps.

## Challenges and Solutions
- **MySQL Configuration**: MySQL requires user-specific credentials and a running server. The `README.md` provides detailed steps to create the database and troubleshoot common issues (e.g., wrong password, missing database).
- **Database URI**: The URI in `app.py` assumes a default setup (`root:root@localhost:3306`). Instructions clarify how to update it for custom credentials or setups.
- **Sample Data Population**: The `init_db.py` script checks for existing incidents to avoid duplicates, ensuring idempotent execution.
- **Validation**: Ensuring robust validation required checking for JSON presence, field types, and valid severity values, handled in the `POST` endpoint.
- **Portability**: SQLAlchemy's ORM allows the project to be adapted to other databases (e.g., PostgreSQL) with minimal changes, though MySQL was chosen per the user's request.

## Troubleshooting Common Issues
- **Error: Access denied for user 'root'@'localhost'**:
  - Cause: Incorrect password in the `SQLALCHEMY_DATABASE_URI`.
  - Solution: Update `app.py` with the correct root password.
- **Error: Unknown database 'humanchain'**:
  - Cause: The `humanchain` database wasn't created.
  - Solution: Run `schema.sql` in MySQL (Step 2).
- **Error: Can't connect to MySQL server**:
  - Cause: MySQL isn't running or is on a different host/port.
  - Solution: Start MySQL and verify the host/port in the URI.
- **ModuleNotFoundError**:
  - Cause: Dependencies not installed.
  - Solution: Run `pip install -r requirements.txt` in the virtual environment.
- **API Not Responding**:
  - Cause: Flask server not running or wrong port.
  - Solution: Ensure `python app.py` is running and access `http://localhost:5000`.

## Submission Instructions
To submit the project:
1. Verify all files are present: `app.py`, `models.py`, `requirements.txt`, `init_db.py`, `schema.sql`, `README.md`.
2. Test all API endpoints to ensure they work as expected.
3. Package the project:
   - **Zip File**: Zip the `humanchain-ai-safety` directory:
     ```bash
     zip -r humanchain-ai-safety.zipЛА=zip -r humanchain-ai-safety.zip
     ```
   - **Git Repository**: Push to a public Git repository (e.g., GitHub, GitLab):
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin <repository-url>
     git push -u origin main
     ```
     Share the repository URL in your submission.
4. Include this `README.md` with complete setup and usage instructions.
5. (Optional) Include a cover letter or email referencing the repository or zip file.

## Additional Notes
- **Security**: The project uses the MySQL root user for simplicity. In a production environment, use a dedicated user with limited privileges (see `schema.sql` comments).
- **Extensibility**: The API can be extended with features like pagination for `GET /incidents`, authentication, or additional endpoints (e.g., `PUT` for updating incidents).
- **Performance**: MySQL and SQLAlchemy are suitable for small to medium-scale applications. For high traffic, consider indexing or caching.

Thank you for reviewing my submission. I hope this project demonstrates my backend development skills and attention to detail. Please contact me with any feedback or questions!