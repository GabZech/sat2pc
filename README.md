# Sat2PC

By Yoones Rezaei, Stephen Lee

# Citation

If you find our paper helpful in your work, please consider citing:

```
@misc{https://doi.org/10.48550/arxiv.2205.12464,
  doi = {10.48550/ARXIV.2205.12464},

  url = {https://arxiv.org/abs/2205.12464},

  author = {Rezaei, Yoones and Lee, Stephen},

  keywords = {Computer Vision and Pattern Recognition (cs.CV), Artificial Intelligence (cs.AI), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},

  title = {sat2pc: Estimating Point Cloud of Building Roofs from 2D Satellite Images},

  publisher = {arXiv},

  year = {2022},

  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

# Introduction

In this repository we release the code and data for our paper "sat2pc: Generating Building Roof's Point Cloud from a Single 2D Satellite Images" in ICCPS 2023. You can find the original paper [here](https://arxiv.org/abs/2205.12464).

# Installation

To use this repository you need an environemnt with python 3.7.9. We suggest creating a conda environment with the following command:

```
conda env create -f environment.yml
```

Next, activate the environment:

```
conda activate sat2pc
```

Finally, run the following commands:

```
conda install -c "nvidia/label/cuda-11.7.0" cuda
python PyTorchEMD/setup.py install
python neuralnet-pytorch-master/setup.py install
```

These commands will install extra required packages.

# Data

The dataset from the paper can be dowloaded from [here](https://pitt-my.sharepoint.com/:f:/g/personal/yor10_pitt_edu/Eo4HLZ9ysERBkBem0wl5HZ8BBcqzDruuI77PhfqL_kWIWg).

# Usage

To train the model you can run the following command:

```
python train.py --config ./configs/sat2pc.gin --data-dir ./datasets/
```

To test the model you can run the following command:

```
python test.py --config ./configs/sat2pc.gin --data-dir ./datasets/ --ckpt-path [location of the saved weights]
```

# Visualization

To visualize the predictions from the model you can use the following command:

```
python visualize.py --data-dir ./datasets --results [location of the .res file generated by running the test script]
```

