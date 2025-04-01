# Installation Guide for MolPAL and pyscreener

This is a simple guide to installing MolPAL and pyscreener in a fresh environment. For now, I keep some of the `pip` and `conda` calls separated out just for full clarity for some of the most important dependencies.

## Prerequisites
- Miniconda or Anaconda
- macOS, Linux, or WSL

If you don't have conda/miniconda on your HPC, follow your HPC documentation's instructions to install it (miniconda is best).

## Step 1: Create a new conda environment

 Then, you can run

```bash
conda create -n molpal-env python=3.11 -y
conda activate molpal-env
```

## Step 2: Install pyscreener

```bash
# core dependencies 
conda install -c conda-forge rdkit openbabel openmm pdbfixer -y
pip install numpy scipy pandas scikit-learn tqdm

# install pyscreener (forked version with updated dependencies)
git clone https://github.com/mcox3406/pyscreener.git
cd pyscreener
pip install -e .
cd ..
```

## Step 3: Install required binaries for docking

1. Download binaries:
   ```bash
   # create a bin directory in your PyScreener directory
   mkdir -p pyscreener/bin
   cd pyscreener/bin
   
   # download AutoDock Vina (use v1.1.2 for compatibility for the time being)
   # if on macOS, switch link to 
   # https://vina.scripps.edu/wp-content/uploads/sites/55/2020/12/autodock_vina_1_1_2_mac_64bit.tar.gz 
   wget https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v1.1.2-boost-new/vina_1.1.2-boost-new_linux_x86_64 -O vina
   chmod +x vina
   
   # download ADFRsuite
   # if on macOS, switch link to https://ccsb.scripps.edu/adfr/download/1033/
   # additionally, when you extract the tar file, the name might be different
   # so modify to the correct name for the `rm` and `cd` commands below
   wget https://ccsb.scripps.edu/adfr/download/1038 -O ADFRsuite_x86_64Linux_1.0.tar.gz
   tar -xzvf ADFRsuite_x86_64Linux_1.0.tar.gz
   rm -rf ADFRsuite_x86_64Linux_1.0.tar.gz

   # install ADFRsuite (see README in ADFRsuite directory)
   # again, this might be named slightly differently if you're on macOS
   cd ADFRsuite_x86_64Linux_1.0
   ./install.sh -d . -c 0
   cd ../../..
   ```

2. Add binaries to your PATH by creating an activation script:
   ```bash
   # create the activation directory if it doesn't exist
   mkdir -p $CONDA_PREFIX/etc/conda/activate.d
   
   # create the activation script
   # NOTE THAT YOU WILL NEED TO CHANGE THESE PATHS TO POINT TOWARDS YOUR INSTALLATIONS
   # these are what the paths look like for me
   echo 'export PATH="/nobackup1/mcox340/pyscreener/bin:/nobackup1/mcox340/pyscreener/bin/ADFRsuite_x86_64Linux_1.0/bin:$PATH"' > $CONDA_PREFIX/etc/conda/activate.d/pyscreener_activate.sh
   
   # Make the script executable
   chmod +x $CONDA_PREFIX/etc/conda/activate.d/pyscreener_activate.sh
   ```

3. Reactivate your environment to apply the changes:
   ```bash
   conda deactivate
   conda activate molpal-env
   ```

4. Verify the binaries are in your PATH:
   ```bash
   which vina
   which prepare_receptor
   ```
## Step 4: Install MolPAL

```bash
# install torch (using CPU version for simplicity since GPU acceleration is unnecessary)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip install lightning
pip install "ray[train]"

# install MolPAL (forked version with updated dependencies)
git clone https://github.com/mcox3406/molpal.git
cd molpal
pip install -e .
```

## Step 5: Test the installation

Run the example calculation in the [`molpal_test`](molpal_test/) directory to check that everything works:
```bash
conda activate molpal-env
cd molpal_test
molpal run --config configs/sample_config.ini
```

If you're on an HPC, be sure to first get off of the login node before running molpal. You can do this via a command similar to the following:
```bash
srun --partition=sched_mit_ccoley --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=8G --time=02:00:00 --pty bash -i
```


That's it! You now have a working installation of MolPAL with pyscreener that uses Python 3.11, PyTorch 2.6.0, PyTorch Lightning 2.5.1, and Ray 2.44.1.

Other files related to submitting jobs on an HPC (which is what you have to do when using large libraries) are located in the [`molpal_maba`](molpal_maba/) directory.
