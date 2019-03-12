import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirementse = f.read().splitlines()

setuptools.setup(
    name="apexlegendspy",
    version="0.0.1",
    author="surister",
    author_email="surister98@gmail.com",
    description="Apex-legends api async wrapper",
    license='MIT',
    long_description=long_description,
    include_package_data=True,
    python_requires='>=3.6.0',
    install_requires=[
        'aiohttp'
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/surister/apexpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
)
