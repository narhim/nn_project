# Neural Networks Implementation and Application: POS Tagging with BERT

This is the Final Project for the WS2020/2021 Neural Networks Implementation and Application course at the University
of Saarland.

This project is in progress and will be updated periodically. The information in this repository reflects works done
in Part 1 of the projects as outlined in the [Table of Contents](#table-of-contents).

## Group Members

* Priyanka Das _s8prdass_ (2581478)
* Teresa Martín _s8tmart_ (2581298) 
* Noon Pokaratsiri Goldstein _s8supoka_ (2581469)

## Table of Contents

* [Part 1:Data Preprocessing](#data-preprocessing)  
    [1.1 Download and Concatenate Data Files](#download-and-concatenate-data-files)  
    [1.2 Create `sample.tsv` Data File](#create-sampletsv-data-file)  
    [1.3 Obtain Data Statistics](#obtain-data-statistics)
  
* Part 2: _to be continued_

## Prerequisites

To replicate our work, please ensure your environment contains the modules listed in the provided **environment yaml**. 
At the moment, the only specification there is a Python version 3.6 or greater and the default anaconda packages 
(optional). The environment file will be updated if other specific libraries are needed.


Please follow standard conda instructions to re-create an environment from a yaml file.

Scripts are created for Python3 and have been tested on Mac OS and Linux platforms.


## Repo File Organization

The project file structure is as follows:

* **Project Parent Directory:** nn_project  --> **this should be your pwd** for running scripts.
    * README.md  
    * data_preprocess.py  
    * sample.conll  
    * **data/**  
        * sample.tsv
        * sample.info
    * run.sh
    

_Note:_ the **data/** directory and the `.tsv` and `.info` files are not provided per submission instructions. 
This directory (and files) will be created by the `data_preprocess.py` script.

_Note:_ the `sample.conll` file is _not_ provided either. This file structure demonstrate where this file should be
in relation to the `data_preprocess.py` script for the script to run with the default arguments.

## Data Preprocessing

Part 1 of the project includes data preprocessing and information gathering steps as described in the following
sections.

### Download and Concatenate Data Files

The original data files are distributed as 4 .conll files:

* chtb0223.goldconll
* phoenix0001.goldconll
* pri0016.goldconll
* wsj1681.goldconll

To concatenate these 4 files into 1 data file named `sample.conll`, we ran the following command from the directory 
containing these files.

```
cat *.goldconll >> sample.conll 
```

_Note:_ as per submission instructions, data files listed above are not provided.

If these files are saved elsewhere that is not this project directory, the `sample.conll` file, once generated, should
be moved to the location as described in the [Repo File Organization.](#repo-file-organization) This is simply so that
the `data_preprocess.py` script can be executed with the default arguments. Otherwise, please specify the path to the
`sample.conll` generated from this step as appropriate. 

### Create `sample.tsv` Data File

The `sample.conll` file still contains extraneous information we do not need for the project. We create `sample.tsv`
data file, which only contains word token position, the sentence word tokens, and their corresponding POS tags. 

This step is done in the `data_preprocess.py` script, which can be run with the following arguments:

```bash
python data_preprocess.py \
  --dataset_name sample.conll \
  --output_dir data \
  --info_filename sample.info \
  --output_filename sample.tsv \
  --both True
```

The `data_preprocess.py` script also performs the next step [(obtaining data statistics)](#obtain-data-statistics), 
hence the script argument for output_info_name filename.  

Both steps are done by executing the `data_preprocess.py` script once.

We have also made a bash script `run.sh`, which performs the script above with the default arguments.

_Note:_ It is possible to only generate the simplified data file `sample.tsv` without generating the `sample.info` file.
Simply pass `False` to the `--both` argument of the `data_preprocess.py` as in an example below:

```bash
python data_preprocess.py \
  --dataset_name sample.conll \
  --output_dir data \
  --info_filename sample.info \
  --output_filename sample.tsv \
  --both False
```
_Note 2:_ filename arguments for `--info_filename` and `--output_filename` expect **only** file names and **not** paths.

### Obtain Data Statistics

This step simply obtains information about the data file such as maximum/minimum/mean sentence lengths, number of
sentences, POS tags, and POS tags distribution.  

To obtain the statistics, run the `data_preprocess.py` script as in the previous step 
[(creating `sample.tsv` file)](#create-sampletsv-data-file). An example command is given below. 

```bash
python data_preprocess.py \
  --dataset_name sample.conll \
  --output_dir data \
  --info_filename sample.info \
  --output_filename sample.tsv \
  --both True
```

The command above can also be executed by the bash script `run.sh`.

As mentioned in the previous section, both this step and the step to create the `sample.tsv` file are done by 
executing the `data_preprocess.py` script once with the default arguments. If you have already
run the `data_preprocess.py` script once (and you did _not_ specify the argument `--both False`) to create the 
`sample.tsv`file, **there is no need to run `data_preprocess.py` again.**


## Part 2

Pending further instructions.