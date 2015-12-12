from setuptools import setup, find_packages

setup(
    name='healthvaultlib',
    version='2.0',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    maintainer='Rajeev S',
    maintainer_email='rajeevs1992@gmail.com',
    description='README.rst',
    long_description='Description',
    license='NotDecided',
    url='https://github.com/rajeevs1992/pyhealthvault',
    download_url='https://github.com/rajeevs1992/pyhealthvault/archive/master.zip',
    install_requires=[
        'cryptography',
        'enum34',
        'lxml',
        'pycrypto',
        'python-dateutil',
        'pytz',
        ],
    )
