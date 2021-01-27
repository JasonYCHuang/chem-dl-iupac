# INSTALL

This guidance is tested on Linux Ubuntu 18.04 with NVIDIA GPU/driver installed.

## 1. Installation

### 1.1. Install Anaconda

Please refer to `https://www.anaconda.com/`.

You can follow [unofficial Anaconda installations for Dummies](training_smi_to_iupac_name/INSTALL_BASIC.md) for a test installation.

However, it is highly recommended to refer to official websites.

### 1.2. Create env

_Logout & login to load installations._

```
$ conda create --name chem-iupac-app-01 python=3.7
$ source activate chem-iupac-app-01
```

```
$ sudo apt-get install gcc libxrender1 libxext-dev pkg-config

$ conda install -c rdkit rdkit=2020.09.1.0

$ conda install -c conda-forge jpype1
```

```
# install pytorch CPU version
# here is an example for Linux, conda, python, CPU (not CUDA)
$ conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

```
# install fairseq
$ pip install fairseq==0.10.1 sacremoses==0.0.43 subword-nmt==0.3.7 Flask==1.1.2
```

Java is required for [opsin](https://github.com/dan2097/opsin).
```
$ sudo apt install openjdk-11-jre-headless
```



# 2. Downlad required data

```
$ bash install_script.sh
```



# 3. Run

```
# run on the production server
$ gunicorn -w 4 -b 0.0.0.0:7107 server:app --daemon
```

```
# for local development only
$ export FLASK_APP=chem_iupac && export FLASK_ENV=development && flask run --host=0.0.0.0 --port=7107
```

