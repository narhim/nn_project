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

To replicate our work, please ensure your environment contains the modules listed in the provided **environment yaml**
or **requirements.txt** file prior to cloning our repo.

We include 2 versions of the environment yaml files, 1 exported from a Mac OS environment and another from a Linux OS.

Please follow standard conda instructions to re-create an environment from a yaml file **or** follow the standard
instructions for pip installing the required modules from a requirements file.

Scripts are created for and tested on Python 3.

_Note:_ The original data files for Part 1.1 are not provided. 

## Repo File Organization

The project file structure is as follows:

* **Project Parent Directory:** nn_project  
    * README.md  
    * data_preprocess.py  
    * sample.conll  
    * **results/**  
        * sample.tsv
        * sample.info
    * run.sh

## Data Preprocessing

Part 1 of the project includes data preprocessing and information gathering steps as described in the following
sections.

### Download and Concatenate Data Files

The original data files are distributed as 4 .conll files:

* chtb0223.goldconll
* phoenix0001.goldconll
* pri0016.goldconll
* wsj1681.goldconll

To concatenate these 4 files into 1 data file named `sample.conll`, we ran the following command in from the directory 
containing these files.

```
cat *.goldconll >> sample.conll 
```

### Create `sample.tsv` Data File

The `sample.conll` file still contains extraneous information we do not need for the project. We create `sample.tsv`
data file, which only contains word token position, the sentence word tokens, and their corresponding POS tags. 

This step is done in the `data_preprocess.py` script, which can be run with the following arguments:

```bash
python data_preprocess.py \
  --dataset_name sample.conll \
  --output_dataset_name sample.tsv \
  --output_info_name sample.info \
  --output_dir results
```

The `data_preprocess.py` script also performs the next step [(obtaining data statistics)](#obtain-data-statistics), 
hence the script argument for output_info_name filename.  

Both steps are done by executing the `data_preprocess.py` script once.  

We have also made a bash script `run.sh`, which performs the script above with the default arguments.

### Obtain Data Statistics

This step simply obtains information about the data file such as maximum/minimum/mean sentence lengths, number of
sentences, POS tags, and POS tags distribution.  

To obtain the statistics, run the `data_preprocess.py` script as in the previous step 
[(creating `sample.tsv` file)](#create-sampletsv-data-file). An example command is given below. 

```bash
python data_preprocess.py \
  --dataset_name sample.conll \
  --output_dataset_name sample.tsv \
  --output_info_name sample.info \
  --output_dir results
```

The command above can also be executed by the bash script `run.sh`.

As mentioned in the previous section, both this step and the step to create the `sample.tsv` file are done by 
executing the `data_preprocess.py` script once. If you have already
run the `data_preprocess.py` script once to create the `sample.tsv`file, _there is no need to run it again_.



## Part 2

Pending further instructions.