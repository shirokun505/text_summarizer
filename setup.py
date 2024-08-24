import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()  

__version__ ="0.0.0"
REPO_NAME="text_summarizer"
AUTHOR_USER_NAME="Anish Routh"
SRC_REPO="text_summarizer"  
AUTHOR_EMAIL="a.routh10@outlook.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple NLP summarizer .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shirokun505/" + REPO_NAME,
    package_dir={"":"src"},
    packages=setuptools.find_packages() 
)