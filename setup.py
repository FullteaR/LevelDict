from setuptools import setup, find_packages


setup(
    name = "leveldict",
    version = "0.0.1",
    author = "Fulltea",
    author_email = "rikuta@furutan.com",
    url = "git@github.com:FullteaR/LevelDict.git",
    install_requires = ["leveldb"],
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    ext_modules = []
)