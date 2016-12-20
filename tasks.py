from __future__ import print_function

import os
import errno
import shutil
from six.moves import urllib

from invoke import task

ROOT = os.path.abspath(os.path.dirname(__file__))


def fileurl(path):
    path = os.path.abspath(path)
    return urllib.parse.urljoin('file:', urllib.request.pathname2url(path))


@task
def clean(ctx):
    rm_targets = ['build', 'dist', 'huffman.egg-info']

    for t in rm_targets:
        try:
            print('removing {}...'.format(t), end=' ')
            shutil.rmtree(os.path.join(ROOT, t))
            print('OK.')
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise
            print('already gone.')


@task
def build(ctx):
    ctx.run('python setup.py sdist bdist_wheel')


@task
def install(ctx):
    if int(os.environ.get('INSTALL_WHEEL', 0)):
        print('installing bdist_wheel...')
        ctx.run('pip install dist/huffman-*.whl')
    else:
        print('installing sdist...')
        ctx.run('pip install dist/huffman-*.tar.gz')


@task
def test(ctx, coverage=False):
    cmd = 'nosetests tests'
    if coverage:
        cmd += ' --with-coverage --cover-erase --cover-package=huffman'

    ctx.run(cmd)

    if coverage:
        ctx.run('coverage xml')
        ctx.run('coverage html')


@task
def report(ctx):
    import webbrowser
    webbrowser.open_new_tab(fileurl(os.path.join(ROOT, 'coverage_html_report', 'index.html')))


@task
def publish(ctx):
    ctx.run('twine upload dist/*')
