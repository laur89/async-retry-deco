from setuptools import setup
from os.path import exists

readme_f = 'README.rst'
__description__ = 'Retry Decorator for asyncio'


setup(
    name="async-retry-deco",
    # version=get_version(),
    version='0.0.1.dev0',  # managed by zest.releaser!
    author="Laur",
    url="https://github.com/laur89/async-retry-deco",
    description=__description__,
    license='MIT',
    long_description=open(readme_f).read() if exists(readme_f) else __description__,
    install_requires=[
        "async_timeout",
    ],
    extras_require={
        ':python_version=="3.5"': ["asyncio"],
    },
    py_modules=["async_retrying"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=["asyncio", "retry", "retrying", "decorator", "deco"],
)
