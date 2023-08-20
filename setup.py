from setuptools import setup

setup(
    name="clean_folder",
    version="1",
    description="Organizing files in folder",
    url="https://github.com/okolobaiev/clean_folder",
    author="Oleh K.",
    author_email="o.kolobaiev@gmail.com",
    license="MIT",
    packages=["clean_folder"],
    entry_points={"console_scripts": ["clean_folder.clean.main"]},
)
