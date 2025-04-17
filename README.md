TODO: add earthmover logo

# Welcome to Earthmover's CNG 2025 Workshop :wave:
## Zarr, Icechunk, & Xarray for Cloud-native Geospatial Data-cube Analysis

TODO: Intro

**Learning Objectives:**

1. Understand the Zarr chunked n-dimensional array format.
2. Understand how the Zarr data model complements the Raster data model underlying the GDAL/GeoTIFF/STAC ecosystem. 
3. Learn how to navigate the two data models by building cloud-native datacubes from an input GeoTIFF dataset.
4. Understand how to use Xarray and the surrounding ecosystem for geospatial analytics.


## Materials

TODO: link to tutorial notebook

## Setup

### Python

We assume that `Python>=3.11` is already installed on the device you are using for this workshop. If it is not, your first step will be to install another version of Python. We recommend using [`pyenv`](https://github.com/pyenv/pyenv) for managing multiple versions of Python. 

### Dependencies

The dependencies required for executing the notebooks in this workshop are in `requirements.txt` and `environment.yaml` for `conda` users. 

We recommend using `pip` + `venv` to create an isolated virtual environment with these dependencies, but you may choose to install these dependencies however you like. Virtualenv and conda are also valid choices.


### `venv`

Create the virtual environment with `venv`. We recommend using Python >= 3.11 for this tutorial.

> 🧠 The Python version specified below must already be installed on the system.

```
python3.12 -m venv em-workshop-env
```

Activate the virtual environment:

```
source em-workshop-env/bin/activate  # Windows: workshop-env\Scripts\activate
```

Install the dependencies in the environment:

```
pip install -r requirements.txt
```

### `virtualenv`

### conda

```
cd workshop-cng-2025-zarr
conda env create -f environment.yml
conda activate em-workshop-env
```

## Running Jupyter Notebooks
To run the tutorial notebooks, activate your virtual environment and run:
```
jupyter notebook
```