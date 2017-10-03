# Development


## Required Packages

**Pip**
```bash
apt-get update
apt-get python-pip
```

**Virtualenv**
```bash
apt-get update
apt-get virtualenv
```


## Steps for running the project

**Create project and change directory**
```bash
mkdir Doit
cd Doit
```

**Create virtualenv with python3**
```bash
virtualenv -p python3 env
```

**Make active virtualenv**
```bash
source env/bin/activate
```

**Get source code**
```bash
git clone https://github.com/crownest/doit-backend.git source (Use HTTPS)
git clone git@github.com:crownest/doit-backend.git source     (Use SSH)
```

**Change directory and branch**
```bash
cd source
git checkout develop
```

**Create required files**
```bash
cp doit/settings/local-dist.py doit/settings/local.py
touch doit/settings/secrets.py
```

Note: Please ask secret credentials from admin.

**Install requirements**
```bash
pip install -r requirements/dev.txt
```

**Create database**
```bash
./manage.py migrate
```

**Create superuser**
```bash
./manage.py createsuperuser
```

**Run project**
```bash
./manage.py runserver 0.0.0.0:8000 (http://127.0.0.1:8000)
```

**Run tests**
```bash
./manage.py test doit.apps
```
