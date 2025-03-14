# Flask Web Application

This is a simple Flask-based web application that provides routing, form handling, and static file serving.

## Features
- Serves few HTML pages
- Handles static resources: `style.css`, `logo.png`
- Processes form submissions on `message.html` and stores messages in `storage/data.json`
- Returns a `404 Not Found` error page when necessary
- Provides a `/read` route to display stored messages using Jinja2 templates

## Project Structure
```
/goit-pythonweb-hw-03
│── app.py
│── templates/
│   ├── index.html
│   ├── message.html
│   ├── error.html
│── static/
│   ├── style.css
│   ├── logo.png
│── storage/
│   ├── data.json
│── requirements.txt
│── readme.md
│── Dockerfile
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone <repository_url>
cd your_project
```

### 2. Create and Activate Virtual Environment
#### On Windows
```sh
python -m venv venv
venv\Scripts\activate
```
#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```
The app will run on `http://127.0.0.1:3000/` by default.

### 5. Stop the Application
To deactivate the virtual environment, use:
```sh
deactivate
```

## API Endpoints
| Route       | Method | Description                           |
|------------|--------|--------------------------------------|
| `/`        | GET    | Renders `index.html`                |
| `/message` | GET    | Renders `message.html`               |
| `/message` | POST   | Saves form data to `storage/data.json` |
| `/read`    | GET    | Displays stored messages             |

## You can run it via Docker

2. Build and run the container:
```sh
docker build -t flask_app .
docker run -p 3000:3000 flask_app
```

## License
This project is licensed under the MIT License.

