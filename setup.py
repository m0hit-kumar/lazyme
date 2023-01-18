from setuptools import setup

setup(
    name="lazyme",
    version="0.1",
    py_modules=["main"],
    install_requires=["click", "typer", "requests"],
    entry_points="""
        [console_scripts]
        greet=main:main
    """,
)
