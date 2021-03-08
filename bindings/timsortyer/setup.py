from setuptools import setup
from setuptools_rust import RustExtension, Binding


setup(
    name="timsortyer",
    version="0.1.1",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    packages=["timsortyer"],
    rust_extensions=[RustExtension("timsortyer._timsortyer", "Cargo.toml", debug=False, binding=Binding.PyO3)],
    include_package_data=True,
)