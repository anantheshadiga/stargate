
## Prerequisite
Install virualenv
bash
pip3 install --upgrade virtualenv

- Create virtual environment 
bash
virtualenv myvenv

- Activate the virtual environment
bash
source myvenv/bin/activate
#### install postgresql
- Install postgresql & postGIS. This will be used as the datastore
```bash
brew install postgresql
brew install postgis
```
- Start the services with postgresql
```bash
brew services start postgresql
```
- If postgreql is not running, Then do the following
```bash
sudo rm -rf /usr/local/var/postgres  # in case this is not your first try
sudo mkdir /usr/local/var/postgres
sudo chmod 0700 /usr/local/var/postgres
user=$(whoami) && sudo chown -R $user /usr/local/var/postgres
initdb -D /usr/local/var/postgres
```

#### Create db/table


Create database 
```bash
> psql -d template1
psql (12.3)
Type "help" for help.

template1=# CREATE DATABASE stargate;
CREATE DATABASE
(reverse-i-search)`CREATE ': ^CEATE DATABASE stargate;
template1=# CREATE USER stargate WITH PASSWORD 'abracadabra';
CREATE ROLE
template1=# GRANT ALL PRIVILEGES ON DATABASE stargate TO stargate;
GRANT
template1=# \q
```

```bash
python manage.py makemigrations
python manage.py migrate
```
