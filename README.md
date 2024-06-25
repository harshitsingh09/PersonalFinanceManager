
## Setup Instructions

### Prerequisites

- Python 3.6+
- PostgreSQL
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/personal-finance-manager.git
    cd personal-finance-manager/backend
    ```

2. **Create and Activate Virtual Environment** (optional):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**:

    For Unix-based systems:

    ```bash
    export SECRET_KEY='your_secret_key'
    export JWT_SECRET_KEY='your_jwt_secret_key'
    export DATABASE_URL='postgresql://user:password@localhost/personal_finance'
    ```

    For Windows:

    ```bash
    set SECRET_KEY=your_secret_key
    set JWT_SECRET_KEY=your_jwt_secret_key
    set DATABASE_URL=postgresql://user:password@localhost/personal_finance
    ```

5. **Run Database Migrations**:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the Application**:

    ```bash
    python manage.py
    ```

### Running with Docker

1. **Install Docker**:

    Download and install Docker from [Docker's official site](https://www.docker.com/get-started).

2. **Create a `docker-compose.yml` file**:

    ```yaml
    version: '3.8'

    services:
      db:
        image: postgres:latest
        environment:
          POSTGRES_USER: user
          POSTGRES_PASSWORD: password
          POSTGRES_DB: personal_finance
        ports:
          - "5432:5432"
        volumes:
          - postgres_data:/var/lib/postgresql/data

    volumes:
      postgres_data:
    ```

3. **Start the Docker container**:

    ```bash
    docker-compose up -d
    ```

4. **Set the `DATABASE_URL` environment variable**:

    ```bash
    set DATABASE_URL=postgresql://user:password@localhost:5432/personal_finance
    ```

5. **Run the Application**:

    ```bash
    python manage.py
    ```

## Usage

- **Register**: Create a new account.
- **Login**: Authenticate with your credentials to access your personal dashboard.
- **Manage Finances**: Add, update, and categorize your incomes and expenses.
- **Set Budgets**: Define budgets and get alerts when you approach your limits.
- **Track Investments**: Monitor and visualize your investment portfolio.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Marshmallow](https://marshmallow.readthedocs.io/)
