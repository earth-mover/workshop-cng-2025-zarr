![](./assets/earthmover.png)

# Zarr, Icechunk, & Xarray for Cloud-native Geospatial Data-cube Analysis

## CNG 2025: Earthmover Workshop

This workshop is designed as an on-ramp to using the Zarr data format for cloud-native geospatial datacube analysis. Guided by experience running similar workshops for the earth, ocean, atmosphere, & climate sciences, we focus on the conceptual underpinnings of array data analytics using Zarr & Xarray.

-----

**Learning Objectives:**

1. Understand the Zarr chunked n-dimensional array format.
2. Understand how the Zarr data model complements the Raster data model underlying the GDAL/GeoTIFF/STAC ecosystem. 
3. Learn how to navigate the two data models by building cloud-native datacubes from an input GeoTIFF dataset.
4. Understand how to use Xarray and the surrounding ecosystem for geospatial analytics.

## Materials

Materials for this workshop can be found under the [`notebooks`](./notebooks/). The workshop has been split into two parts:
- Part 1 serves as a introduction to the Zarr storage model via a tutorial on how to convert a timeseries of GeoTIFF files into a Zarr store ([notebook](./notebooks/workshop-part-1.ipynb))
- Part 2 focuses on how to effectively wield a global Zarr datacube for common geospatial use-cases such as AOI-driven zonal statistics, masking, and reprojecting ([notebook](./notebooks/workshop-part-2.ipynb))

## Setup

### Python

We assume that `Python>=3.11` is already installed on the device you are using for this workshop. If it is not, your first step will be to install another version of Python. We recommend using [`pyenv`](https://github.com/pyenv/pyenv) for managing multiple versions of Python. 

### Dependencies

The dependencies required for executing the notebooks in this workshop are in `requirements.txt` and `environment.yaml` for `conda` users. 

We recommend using `pip` + `venv` to create an isolated virtual environment with these dependencies, but you may choose to install these dependencies however you like. `Virtualenv` and `conda` are also valid choices.


### `venv`

Create the virtual environment with `venv`. We recommend using Python >= 3.11 for this tutorial.

> 🧠 The Python version specified below must already be installed on the system.

```
python3.12 -m venv em-workshop-env
```

Activate the virtual environment:

```
# On Linux/macOS:
source em-workshop-env/bin/activate
# On Windows (cmd):
em-workshop-env\Scripts\activate
# On Windows (PowerShell):
em-workshop-env\Scripts\Activate.ps1
```

Install the dependencies in the environment:

```
pip install -r requirements.txt
```

### `virtualenv`

```
virtualenv -p python3.12 venv

# On Linux/macOS:
source em-workshop-env/bin/activate
# On Windows (cmd):
em-workshop-env\Scripts\activate
# On Windows (PowerShell):
em-workshop-env\Scripts\Activate.ps1

pip install -r requirements.txt
```

### `conda`

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
