## Project Management Tools

### Prerequisites

- Python 3.x
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd projectManger
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**:
   ```bash
   python manage.py runserver
    ```
### API Documentation
Access the interactive Swagger documentation at:

#### Swagger UI: http://localhost:8000/api/docs/