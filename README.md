# MLPipe-Trainer

Manage your Data Pipline and Tensorflow & Keras models with MLPipe. It is NOT another "wrapper" around Tensorflow, but rather adds utilities to setup an environment to control data flow and managed trained models (weights & results).</br>
To get started, check out this repository and follow the Application Setup described below.

Table of Contents:
1. [ Application Setup ](#app_setup)
    1) [ Install Conda ](#conda)
    2) [ Install MongoDB ](#mongodb)
    3) [ Setup PyCharm (optional) ](#pycharm)
    5) [ Getting Started ](#getting_started)
2. [ Road Map ](#road_map)

<a name="app_setup"></a>
## Application Setup

<a name="conda"></a>
### Install Conda
You can either install Anaconda or Miniconda (https://conda.io/miniconda.html). It is used for package and environment management. The __environment.yml__ file is specifying all the packages needed.</br>
During installation, check the box to add `conda` to your PATH in the .bashrc file or do it manually afterwards.
```bash
>> conda env create -f environment.yml

# And in case you need to update the environment later on
>> conda env update -f environment.yml
```
This will create a conda environment and install all the needed packages (as described in environment.yml).

<a name="mongodb"></a>
### Install MongoDB
MongoDB database is used to store trained Models including their weights and results. Additionally there is also a data reader for MongoDB implemented (basically just a generator as you know and love from using keras). Currenlty that is the only implemented data reader working "out of the box".</br>
Follow the instructions on the MongoDB website for installation e.g. for Linux: https://docs.mongodb.com/manual/administration/install-on-linux/

<a name="pycharm"></a>
### Install PyCharm (optional)
If you development python applications, PyCharm is most probably your goto editor. For installation, use this link and follow the instructions: https://www.jetbrains.com/pycharm/download
</br></br>
After the conda environment is set up, it can be added to the pycharm. Follow:
- File -> Settings -> Project -> Project Interpreter -> Add
- Chose "Existing environment"
- CONDA_PATH/envs/mlpipe_env/bin/python
- Select added environment

Now pycharm will use this conda environment and can access all installed dependencies while developing MLPipe-Trainer with PyCharm.



<a name="getting_started"></a>
### Getting Started
Export the MLPipe-Trainer root to the python path either with (can also be added to .bashrc):
``` bash
# change path accordingly
>> export PYTHONPATH="/home/USER/projects/MLPipe-Trainer"
```
To activate the conda environment call:
```bash
conda activate mlpipe_env
```
For an example you can check out the Cifar-10 example in the project folder

<a name="road_map"></a>
## Road Map
- Create and generat MkDocs documentation
- Add tests
- Create CLI for the project