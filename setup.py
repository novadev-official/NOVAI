from setuptools import setup, find_packages

setup(
    name="novai",
    version="1.0",
    author="Shibin KS",
    author_email="cybernova171717@gmail.com",
    description="A premium Kali Linux security tool and AI terminal assistant.",
    packages=find_packages(),
    py_modules=["novai"],
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "novai=novai:main_menu",
        ],
    },
)
