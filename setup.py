from setuptools import setup

setup(
    name='Flask-SMS',
    version='0.1.0',
    url='http://github.com/muromec/flask_sms',
    download_url='https://github.com/dcrosta/flask-pymongo/tags',
    license='BSD',
    author='Ilya Petrov',
    author_email='ilya.muromec@gmail.com',
    description='SMS sending for flask apps',
    zip_safe=False,
    platforms='any',
    packages=["flask_sms"],
    install_requires=[
        'Flask >= 0.8',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
