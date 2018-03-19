from setuptools import setup

setup(
    name='flask-sparkle',
    version='0.3.0',
    url='http://github.com/closeio/flask-sparkle',
    license='MIT',
    author='Close.io',
    author_email='engineering@close.io',
    maintainer='Close.io',
    maintainer_email='engineering@close.io',
    description='Flask app that publishes Sparkle update feeds',
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    packages=[
        'flask_sparkle',
    ],
    package_data={
        'flask_sparkle': ['templates/*']
    },
)
