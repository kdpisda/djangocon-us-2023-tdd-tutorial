# Mastering Test Driven Development in Django

## DjangoCon US 2023 Tutorial

### Speaker: KD

---

### Prerequisites

1. Git
2. Docker and Docker Compose
3. Poetry
4. Python 3.11

---

### Standalone Setup Guide

#### Step 1: Clone the Repository

Clone the workshop repository to your local machine.

```bash
git clone https://github.com/KD/djangocon-us-2023-tdd-tutorial.git
```

#### Step 2: Navigate to the Repository

Move to the project directory.

```bash
cd djangocon-us-2023-tdd-tutorial/
```

#### Step 3: Checkout to the Initial Branch

The workshop is divided into modules. Start by checking out to the initial branch.

```bash
git checkout initial-setup
```

#### Step 4: Install Dependencies with Poetry

If you don't have Poetry installed, follow [this guide](#setting-up-dependencies-with-poetry). Then, run:

```bash
poetry install
```

#### Step 5: Start Docker Containers

Start the database and Redis containers.

```bash
docker-compose up -d
```

#### Step 6: Database Setup

Run the database migrations.

```bash
poetry run python manage.py migrate
```

#### Step 7: Create Super User

Create a superuser to access the admin interface.

```bash
poetry run python manage.py createsuperuser
```

#### Step 8: Run the Server

Start the Django development server.

```bash
poetry run python manage.py runserver
```

#### Step 9: Validate Setup

Browse to `http://127.0.0.1:8000/admin` and login using the superuser credentials to confirm everything is working as expected.

---

This guide should be adequate for an experienced Python developer to validate that the project setup is correct. If you encounter issues, please reach out during the pre-conference office hours for assistance.

---
