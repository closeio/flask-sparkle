from setuptools import setup

setup(
    name='flask-sparkle',
    version='0.2',
    url='http://github.com/closeio/flask-sparkle',
    license='MIT',
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
)
