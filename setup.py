from distutils.core import setup

VERSION = 'v0.2'

setup(
        name='pydialog',
        version=VERSION,
        author='Nic Roland',
        author_email='nicroland9@gmail.com',
        packages=['pydialog'],
        description="Command line dialogs made easy.",
        url = 'https://github.com/nicr9/pydialog',
        download_url = 'https://github.com/nicr9/pydialog/tarball/%s' % VERSION,
        license="MIT",
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: User Interfaces',
            ],
        )
