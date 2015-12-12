from setuptools import setup, find_packages

setup(
    name='healthvaultlib',
    version='2.0',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    author='Rajeev S',
    author_email='rajeevs1992@gmail.com',
    maintainer='Rajeev S',
    maintainer_email='rajeevs1992@gmail.com',
    description='Python SDK for HealthVault',
    license='MIT',
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
