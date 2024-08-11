from setuptools import setup, find_packages

setup(
    name='example_package',
    version='0.1.0',
    description='An example package for demonstration purposes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/example/example_package',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'example_command=example_module:main_function',
        ],
    },
)
