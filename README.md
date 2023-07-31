# Gland lumen segmentation

This document contains instructions on how to run the Python script for generating patches from whole slide images.

## Description

This script takes as input a directory containing whole slide images. It then generates patches from these images based on specified parameters including patch size, overlap, and the maximum proportion of a patch that can be background. The generated patches are saved to a specified output directory.

## Requirements

To run this script, you will need Python 3.6 or later and the following libraries:
- histoprep
- numpy
- openslide

You can install these libraries using pip:
\```
pip install histoprep numpy openslide-python
\```

## Running the Script

The script takes five command line arguments:

- `SlidesPath`: The path to the folder containing the slides.
- `SavePath`: The path to the folder where patches will be saved.
- `PatchSize`: The size of the patches.
- `Overlap`: The overlap between patches.
- `MaxBackground`: The maximum proportion of a patch that can be background.

You can run the script using the following command:

\```
python script_name.py SlidesPath SavePath PatchSize Overlap MaxBackground
\```

Replace `script_name.py` with the name of your Python script. Replace `SlidesPath`, `SavePath`, `PatchSize`, `Overlap`, and `MaxBackground` with the appropriate values for your data.

Example:
\```
python generate_patches.py /path/to/slides /path/to/save/patches 1000 0 0.1
\```

In this example, the script will generate patches of size 1000 with no overlap. Patches with more than 10% background will be discarded. 

## Output

The script will save the generated patches to the directory specified by `SavePath`. It will also save metadata about the generated patches if `save_metrics=True` is set in the script.
