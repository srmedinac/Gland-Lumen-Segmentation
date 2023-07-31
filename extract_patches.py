import argparse
from histoprep import SlideReader
import numpy as np
import os
import openslide

# Create the parser
parser = argparse.ArgumentParser(
    description="Generate patches from whole slide images."
)

# Add the arguments
parser.add_argument(
    "SlidesPath",
    metavar="SlidesPath",
    type=str,
    help="the path to the folder containing the slides",
)
parser.add_argument(
    "SavePath",
    metavar="SavePath",
    type=str,
    help="the path to the folder where patches will be saved",
)
parser.add_argument(
    "PatchSize", metavar="PatchSize", type=int, help="the size of the patches"
)
parser.add_argument(
    "Overlap", metavar="Overlap", type=int, help="the overlap between patches"
)
parser.add_argument(
    "MaxBackground",
    metavar="MaxBackground",
    type=float,
    help="the maximum proportion of a patch that can be background",
)

# Parse the arguments
args = parser.parse_args()

# Initiate SlideReader
reader = SlideReader(args.SlidesPath)

threshold, tissue_mask = reader.get_tissue_mask(level=-1)

# Extract overlapping tile coordinates with less than the proportion of background specified
tile_coordinates = reader.get_tile_coordinates(
    tissue_mask,
    width=args.PatchSize,
    overlap=args.Overlap,
    max_background=args.MaxBackground,
)

coords = tile_coordinates.coordinates
tile_metadata = reader.save_regions(
    args.SavePath,
    tile_coordinates,
    threshold=threshold,
    save_metrics=True,
    overwrite=True,
)
