# Pose_DL_specimen_pts

This is the code using Pose estimation to place points to measure digtal sepcimen (e.g. natural history collections) images.

## Prerequisites
- Python 3
- tensorflow = 1.6.0
- numpy >= 1.17.3
- pandas >= 0.23.4
- opencv-python = 4.1.1.26


## Installation

```bash
git clone https://github.com/EchanHe/BU_comic.git
```

## Usage

#### Annotation data
A column with images' filenames. And columns of x and y of points.
Example of an annotation file with a point:

| <file_name>  | <pt1_x> | <pt1_y> | 
| ------------- | ------------- | ------------- |
|  |   |   |

#### Config files
Adjust the `[Directory]` section to fit your workspace

`file_col` is the column name for the file name

`cols_override` is the colnumn names for point coordiantes

The other settings and hyperparameters can be set in the config file as well.

#### Training

```python
python train.py <training_config>.cfg
```

#### Predicting
```python
python pred.py <predict_config>.cfg
```

#### Evaluataions
R >= 4.0.2
Use `evaluation/colour_information.R` to evaluate the colour inforamtion
Use `evaluation/pixel_distance_and_pck.R` to calautle the pixel distance and PCK of predicted points


