import icechunk as ic
import xarray as xr

storage = ic.s3_storage(
    bucket="icechunk-public-data",
    prefix=f"v1/glad",
    region="us-east-1",
    anonymous=True,
)
repo = ic.Repository.open(storage=storage)
session = repo.readonly_session("main")
ds = xr.open_dataset(
    session.store, chunks=None, consolidated=False, engine="zarr"
)
print(ds)

import geopandas as gpd

shapes = gpd.read_file("notebooks/gz_2010_us_040_00_500k.json")
utah = shapes.loc[shapes["NAME"] == "Utah"]["geometry"]

print(utah.crs)


import odc.geo.xr  # registers the `.odc` accessor
import rioxarray

bbox = utah.to_crs("EPSG:4326").total_bounds

clipped = ds.rio.clip_box(*bbox).chunk({"x": 1000, "y": 1000})
print(clipped)

import pandas as pd
from xarray.groupers import BinGrouper

legend = {
    "True desert": pd.Interval(0, 1, closed="both"),
    "Semi-arid": pd.Interval(2, 18, closed="both"),
    "Tree cover": pd.Interval(25, 48, closed="both"),
    "Open surface water": pd.Interval(200, 207, closed="both"),
    "Built-up": pd.Interval(250, 250, closed="both"),
}

index = pd.IntervalIndex(list(legend.values()))

lulc_grouper = BinGrouper(bins=index, labels=list(legend.keys()))
print(lulc_grouper)

data_group = clipped.groupby(lclu=lulc_grouper)
print(data_group)
# data_group = data_group.count(dim=("x", "y"))
# print(data_group)

# import time
# start = time.perf_counter()
# clipped = clipped.load()
# end = time.perf_counter()
# print(end- start)


# Define the tree cover mask
# tree_mask = (clipped["lclu"] >= 25) & (clipped["lclu"] <= 48)
# Count tree-covered pixels per year
# tree_pixels = tree_mask.sum(dim=("y", "x"))
# print(tree_pixels)
# # Count total valid (non-NaN) pixels per year
# total_pixels = ds["lclu"].notnull().sum(dim=("y", "x"))
# # Calculate percent tree cover per year
# percent_tree_cover = (tree_pixels / total_pixels) * 100
# # Trigger computation (if using Dask)
# percent_tree_cover = percent_tree_cover.compute()
#  print(percent_tree_cover)


# min_x, min_y, maxx, maxy = bbox

# subset = ds.sel(
#     x=slice(min_x, maxx),
#     y=slice(min_y, maxy)
# )

# subset.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
# subset.rio.write_crs("EPSG:4326", inplace=True)
# clipped = ds.rio.clip(subset, "EPSG:4326")
# print(clipped)

# ds.odc.crop(utah)