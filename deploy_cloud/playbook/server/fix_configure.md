# history from ubuntu server

Author: mark
Created: 2020-06-30.02:56

safhir-id-deploy

        3  cd /opt/django-projects/
        4  ls
        5  git clone https://github.com/OnyxHealth/safhir-vmi.git /opt/django-projects/vmi
        6  sudo git clone https://github.com/OnyxHealth/safhir-vmi.git /opt/django-projects/vmi
        7  exit
        8  cd /opt/django-projects/vmi
        9  source env/bin/activate
       10  ls .env
       11  pip install gunicorn
       12  pip install -r requirements.txt 
       13  cat requirements.txt 
       14  pip install python-ldap
       15  python setup.py install
       16  python -m pip install setuptools
       17  python setup.py install
       18  apt-get install build-essential python3-dev python2.7-dev     libldap2-dev libsasl2-dev slapd ldap-utils python-tox     lcov valgrind
       19  sudo apt-get apt-get install build-essential python3-dev python2.7-dev     libldap2-dev libsasl2-dev slapd ldap-utils python-tox     lcov valgrind
       20  sudo apt-get install build-essential python3-dev python2.7-dev     libldap2-dev libsasl2-dev slapd ldap-utils python-tox     lcov valgrind
       21  cd /opt/django-projects/vmi
       22  source env/bin/activate
       23  pip install -r requirements.txt 
       24  exit
       25  sudo apt-get install sqlite
       26  exit
       27  cd /opt/django-projects/vmi
       28  source env/bin/activate
       29  pip install setuptools
       30  pip install gunicorn
       31  exit
       32  cd /opt/django-projects/vmi 
       33  source env/bin/activate
       34  sudo apt-get install python3-setuptools
       35  sudo apt-get install python-setuptools
       36  pip install gunicorn
       37  exit
       38  cd /opt/django-projects/vmi
       39  source env/bin/activate
       40  source .env
       41  python manage.py migrate
       42  cat manage.py
       43  exit
       44  cd /opt/django-projects/vmi
       45  source env/bin/activate
       46  source .env
       47  python manage.py runserver
       48  cat .env
       49  ls
       50  ls db
       51  cat db/README.md 
       52  ls -la db
       53  python manage.py migrate
       54  echo $DATABASES_CUSTOM
       55  export $DATABASES_CUSTOM=sqlite:////opt/django-projects/vmi/db/db.sqlite3
       56  python manage.py migrate
       57  export $DATABASES_CUSTOM=sqlite:///./db/db.sqlite3
       58  python manage.py migrate
       59  export $DATABASES_CUSTOM=sqlite:////opt/django-projects/vmi/db/db.sqlite3
       60  export DATABASES_CUSTOM=sqlite:////opt/django-projects/vmi/db/db.sqlite3
       61  source .env
       62  python manage.py migrate
       63  ls -la $DATABASES_CUSTOM
       64  vi  .env
       65  source .env
       66  python manage.py migrate
       67  exit
       68  cd /opt/django-projects/vmi/
       69  cat  env/bin/activate
       70  cat .env
       71  exit
       72  cd /opt/django-projects/vmi
       73  ls -la env/bin
       74  cat env/bin/activate
       75  cat env/bin/activateexit
       76  exit
       77  cd /opt/django-projects/vmi
       78  ls -la env
       79  ls -la env/include
       80  ls -la env/include/site
       81  ls -la env/include/site/python3.6/
       82  ls -la env/include/site/python3.6/greenlet/
       83  ls -la env/bin
       84  exit
       85  cd /opt/django-projects/VMI
       86  cd /opt/django-projects/vmi
       87  source env/bin/activate
       88  source .env
       89  python manage.py migrate
       90  cat .env
       91  exit
       92  curl http://localhost
       93  cd /opt/django-projects/vmi
       94  source env/bin/activate
       95  source .env
       96  python manage.py runserver
       97  cat .env
       98  curl http://localhost
       99  curl $HOSTNAME_URL
      100  vi .env
      101  source .env
      102  curl $HOSTNAME_URL
      103  sudo service supervisor restart
      104  curl $HOSTNAME_URL
      105  curl http://168.62.172.248
      106  sudo service nginx restart
      107  curl http://168.62.172.248
      108  sudo service uwsgi reload
      109  sudo service gunicorn reload
      110  sudo service supervisor reload
      111  sudo service supervisor start
      112  curl http://168.62.172.248
      113  sudo cat /etc/systemd/system/gunicorn.service
      114  sudo vi /etc/systemd/system/gunicorn.service
      115  sudo service supervisor reload
      116  exit
      117  cd /opt/django-projects/vmi
      118  source env/bin/activate
      119  sudo service supervisor start
      120  sudo service supervisor reload
      121  curl http://localhost
      122  exit
      123  curl http://localhost


Use this to troubleshoot some of the install steps to improve robustness.

