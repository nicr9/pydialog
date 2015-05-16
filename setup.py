from distutils.core import setup

VERSION = 'v0.1'

setup(
    name='dialog',
    version=VERSION,
    author='Nic Roland',
    author_email='nicroland9@gmail.com',
    packages=['dialog'],
    description="Command line dialogs made easy.",
    url = 'https://github.com/nicr9/dialog',
    download_url = 'https://github.com/nicr9/dialog/tarball/%s' % VERSION,
    license="MIT",
)
