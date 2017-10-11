# Future
from __future__ import with_statement

# Standart Library
from contextlib import contextmanager as _contextmanager

# Third-Party
from fabric.api import env, cd, run, sudo, prefix


env.user = 'root'
env.app_dir = '/home/apps/doit-backend/web/source'
env.activate = 'source ../env/bin/activate'


@_contextmanager
def virtualenv():
    with cd(env.app_dir):
        with prefix(env.activate):
            yield

def pull_source_code(branch):
    run('git fetch')
    run('git checkout %s' % branch)
    run('git pull origin %s' % branch)

def restart_supervisor():
    sudo('supervisorctl reread')
    sudo('supervisorctl update')
    sudo('supervisorctl restart all')

def deploy(branch):
    with virtualenv():
        with cd(env.app_dir):
            # Pull code
            pull_source_code(branch)

            # Install requirements
            run('pip install -r requirements/%s.txt' % branch)

            # Migrate
            run('python manage.py migrate')

            # Test
            run('python manage.py test doit.apps --verbosity=2')

            # Collectstatic
            run('python manage.py collectstatic --noinput')

            # Build docs
            run('mkdocs build --clean')

            # Supervisor
            restart_supervisor()

            # Nginx
            sudo('service nginx restart')
