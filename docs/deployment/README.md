# DEPLOYMENT

Uzak Sunucuya Bağlanma:
~~~~
ssh root@doit.unicrow.com
~~~~

## Ngnix

* ### Installation
  ~~~~
  sudo apt-get update
  sudo apt-gey install ngnix
  ~~~~

* ### Status
  ~~~~
  systemctl status ngnix
  ~~~~

* ### Documentation

  [Documentation](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04)

## Supervisor:
* ### Installation
  ~~~~
  sudo apt-get install supervisor
  ~~~~

* ### Restart
  ~~~~
  service supervisor restart
  ~~~~

* ### Documantation

  [Documentation](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps)

## Python
  ~~~~
  sudo apt-get install python-pip
  ~~~~

## Virtualenv
  ~~~~
  sudo apt-get install virtualenv
  ~~~~

## Add New User
  ~~~~
  adduser apps
  ~~~~

## Yeni User' a Geçiş Yapmak için:
  ~~~~
  su - apps
  ~~~~

## Oluşturulan User ' a sudo yetkisi vermek için:
  ~~~~
  sudo usermod -a -G apps
  ~~~~

## Yedeklemeler, konfigürasyon, uygulama patlarsa eğer nedenlerini görebileceğimiz ve kaynak kodlarının bulunacağı dizinler
~~~~
  doit
    * backup
    * conf
      * gunicorn.sock
      * gunicorn start
    * log
      * gunicorn_supervisor.log
      * nginx-access.log
      * nginx-error.log
    * web
      * env
      * source
        * Proje Dosyaları
        * requirements
~~~~

## web dosyasının içerisine virtualenv kurulup aktif edilir:
  ~~~~
  virtualenv -p python3 env
  source env/bin/activate
  ~~~~

## 4096 Bitlik ve RSA ile şifrelenmiş SSH Key' ini oluşturmak içim
  ~~~~
  ssh-keygen -t rsa -b 4096 -C "digitalocean-doit-apps"
  ~~~~

## Postgresql Veri Tabanı
  ~~~~
  sudo apt-get install postgresql postgresql-contrib
  ~~~~

* ### postgresql terminaline girip Database oluşturduk, ardından kullanıcı oluşturup yetkilerini verdik:
  ~~~~
  postgres@doit:~$ psql
  postgres=# CREATE DATABASE doitdb;
  postgres=# CREATE USER doit WITH PASSWORD '-';
  postgres=# GRANT ALL PRIVILEGES ON DATABASE doitdb to doit;
  postgres=# \q
  postgres@doit:~$ exit
  ~~~~

Oluşturduğumuz database bilgilerini projemizdeki settings.py dosyası içerisindeki DATABASES içerisine kaydettik.

## Django,Psycopg2,Gunicorn ,Django Rest Framework ve Djoser
  ~~~~
  pip install Django
  pip install djangorestframework
  pip install djoser
  pip install psycopg2
  pip install gunicorn
  ~~~~
