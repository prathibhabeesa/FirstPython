from setuptools import setup, find_packages

setup(
    name='logging_module',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'run_logger=logging_module.log_script:main',
        ],
    },
)
