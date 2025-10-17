from setuptools import setup, find_packages

setup(
    name="webapp_ci",
    version="1.0.0",
    packages=find_packages(where="src"),  # look inside src folder
    package_dir={"": "src"},              # tell setuptools src is the root for packages
    py_modules=["app"],                   # app.py is a single module
    include_package_data=True,
    install_requires=[
        "Flask>=3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "run-webapp=app:app.run",    # runs Flask app
        ],
    },
)


