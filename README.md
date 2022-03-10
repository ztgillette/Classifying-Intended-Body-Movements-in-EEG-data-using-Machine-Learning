# Classifying Intended Body Movements in EEG Data Using Machine Learning

## Overview

The source code is included to allow for the reproducibility of our results. Make sure to download all files, as well as the dataset folder.

## Important Note

This code was heavily repurposed. The original code was written by Michael Hersche and Tino Rellstab (credited in the Authors section below). 

## Getting Started

First, download the source code. While the dataset is included in this source code for ease of reproducibility, the original [BCI competition IV-2a] set can be found at http://bnci-horizon-2020.eu/database/data-sets.  

### Prerequisites

Make sure to install the following packages using pip or pip3 in the terminal. For example:
```
$ pip3 install numpy
```

- python3
- numpy
- sklearn
- pyriemann
- scipy

According to the authors of the original code, the packages can also be installed with conda and the _config.yml file: 
```
$ conda env create -f _config.yml -n msenv
$ source activate msenv 
```

### Recreate results

For the recreation of the SVM results run main_svm.py. 
```
$ python3 main_svm.py
```

For the recreation of the KNN results run main_knn.py. 

```
$ python3 main_knn.py
```

For the recreation of the LDA results run main_lda.py. 
```
$ python3 main_lda.py
```

### Generate Plot

To create a plot visualizing the results, run plot.py.
```
$ python3 plot.py
```

The data is manually inputted in a Python list, so make sure to adjust the list with your reproduced results to get the updated plot.

## Authors

* **Zach Gillette** - *Other work* - [ztgillette](https://github.com/ztgillette)

* **Orlando Azuara** - *Other work* - [orlandoazu0709](https://github.com/orlandoazu0709)

* **Michael Hersche** - *Initial work* - [MHersche](https://github.com/MHersche)
* **Tino Rellstab** - *Initial work* - [tinorellstab](https://github.com/tinorellstab)
