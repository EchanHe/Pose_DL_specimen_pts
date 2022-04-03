# Pose_DL_specimen_pts

This is the code using Pose estimation to place points to measure digtal sepcimen (e.g. natural history collections) images.

## Prerequisites
Python 3
tensorflow = 1.6.0
numpy >= 1.17.3
pandas >= 0.23.4
opencv-python = 4.1.1.26


R >= 4.0.2

## Installation

```bash
git clone https://github.com/EchanHe/BU_comic.git
```

## Usage

#### Training

```python
python train.py <training_config>.cfg
```

#### Predicting
```python
python pred.py <predict_config>.cfg
```

#### Evaluataions

Use `evaluation/colour_information.R` to evaluate the colour inforamtion
Use `evaluation/pixel_distance_and_pck.R` to calautle the pixel distance and PCK of predicted points


