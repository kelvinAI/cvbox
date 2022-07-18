from setuptools import setup, find_packages

setup(name="cvbox",
      version="0.0.5",
      author="Kelvin Kong",
      author_email="kelvin86@gmail.com",
      description="A set of reusable tools for computer vision or any deep learning projects.",
      long_description=open("README.md", "r", encoding="utf-8").read(),
      keywords="deep learning tools library computer vision",
      license="Apache",
      url="https://github.com/kelvinAI/cvbox",
      package_dir={"":"src"},
      packages=find_packages(where='src'),
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
      ],
      )