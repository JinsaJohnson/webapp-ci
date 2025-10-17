from setuptools import setup, find_packages

setup(
    name="webapp_ci",
    version="1.0.0",
    packages=find_packages(include=[]),
    py_modules=["app"],
    include_package_data=True,
    install_requires=[
        "Flask>=3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "run-webapp = app:app.run",
        ],
    },
)
