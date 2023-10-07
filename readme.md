# Mastering Test Driven Development in Django

## DjangoCon US 2023 Tutorial

### Speaker: KD

---

## Prerequisites

The following tools are required to run this project:

- Git
- Docker and Docker Compose
- Poetry
- Python 3.11

### Installing on Windows

#### Git
- Download and install it from [git-scm.com](https://git-scm.com/download/win).

#### Docker and Docker Compose
- Download Docker Desktop for Windows from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/) and follow the installation instructions.

#### Poetry
- Install Poetry by running `pip install --user poetry` in your command prompt.

#### Python 3.11
- Download and install it from [python.org](https://www.python.org/downloads/).

### Installing on Linux (Ubuntu)

#### Git
- Run `sudo apt-get update` and then `sudo apt-get install git` to install Git.

#### Docker and Docker Compose
- Follow the [official Docker installation guide for Ubuntu](https://docs.docker.com/engine/install/ubuntu/).
- After installing Docker, install Docker Compose by following the [official guide](https://docs.docker.com/compose/install/).

#### Poetry
- Run `curl -sSL https://install.python-poetry.org | python3` to install Poetry.

#### Python 3.11
- Run `sudo apt-get update` and then `sudo apt-get install python3.11`.

### Installing on macOS

#### Git
- If you have Homebrew installed, run `brew install git`. Otherwise, download and install it from [git-scm.com](https://git-scm.com/download/mac).

#### Docker and Docker Compose
- Download Docker Desktop for macOS from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac/) and follow the installation instructions.

#### Poetry
- Run `brew install poetry` if you have Homebrew. Otherwise, run `pip install --user poetry`.

#### Python 3.11
- If you have Homebrew, run `brew install python@3.11`. Otherwise, download it from [python.org](https://www.python.org/downloads/mac-osx/).


---

### Standalone Setup Guide

#### Step 1: Clone the Repository

Clone the workshop repository to your local machine.

```bash
git clone https://github.com/kdpisda/djangocon-us-2023-tdd-tutorial.git
```

#### Step 2: Navigate to the Repository

Move to the project directory.

```bash
cd djangocon-us-2023-tdd-tutorial/
```

#### Step 3: Checkout to the Initial Branch

The workshop is divided into modules. Start by checking out to the initial branch.

```bash
git checkout main
```

#### Step 4: Modify environment variables

```bash
cp .env.temp .temp
```
Then edit `.env` to be whichever value you'd like, for example you could
use ``"dcus_tdd"`` for all three. For production you'd want to use something
secure.

#### Step 5: Install Dependencies with Poetry

If you don't have Poetry installed, follow [this guide](#setting-up-dependencies-with-poetry). Then, run:

```bash
poetry install
```

#### Step 6: Start Docker Containers

Start the database and Redis containers.

```bash
docker-compose up -d
```

#### Step 7: Database Setup

Run the database migrations.

```bash
poetry run python manage.py migrate
```

#### Step 8: Create Super User

Create a superuser to access the admin interface.

```bash
poetry run python manage.py createsuperuser
```

#### Step 9: Run the Server

Start the Django development server.

```bash
poetry run python manage.py runserver
```

#### Step 10: Validate Setup

Browse to `http://127.0.0.1:8000/admin` and login using the superuser credentials to confirm everything is working as expected.

---

This guide should be adequate for an experienced Python developer to validate that the project setup is correct. If you encounter issues, please reach out during the pre-conference office hours for assistance.

---
