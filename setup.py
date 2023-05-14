"""Install topicViz package."""""

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as file:

    long_description = file.read()

setup(
    name="ateach",
    version="0.0.1",
    author="Edgar Ortiz",
    author_email="ed.ortizm@gmail.com",
    packages=find_packages(
        where="src", include=["[a-z]*"]
    ),
    package_dir={"": "src"},
    description="Automatic content creation for teaching with LLMs from teachers' notes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ed-ortizm/awesome-teaching",
    license="MIT",
    keywords=(
        "NLP, LLMs, generative AI, teaching, education,"
        "machine learning, data science, content creation,"
        "educational technology, edtech, teaching assistant"
    ),
)
