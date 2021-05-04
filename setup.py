import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepsynthbody", 
    version="1.0.2",
    author="Vajira Thambawita",
    author_email="vlbthambawita@gmail.com",
    description="Unlimited deep synthetic medical data generators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlbthambawita/deepsynthbody",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[

        'deepsynth_gitract',
        'deepfake-ecg'

  ],
)