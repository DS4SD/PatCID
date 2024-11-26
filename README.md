# PatCID

This is the repository for [PatCID: an open-access dataset of chemical structures in patent documents](https://www.nature.com/articles/s41467-024-50779-y).

![MolGrapher](assets/introduction.png)

### Installation

Create a virtual environment.

```
conda create -n patcid python=3.11
conda activate patcid
```

Install dependencies.
```
pip install -e .
```

### Download PatCID Dataset 

The [PatCID dataset is available on Zenodo](https://doi.org/10.5281/zenodo.10572870). 
```
wget https://zenodo.org/records/10572870/files/patcid.zip?download=1 -O patcid.zip
unzip patcid.zip -d ./data/patcid/
```
(Download size: `5.7 GB`, files format: `.jsonl`)

### Document Retrieval

Run the notebook `./examples/molecule_query.ipynb` to use PatCID to retrieve documents referencing a molecule of interest. 

### Molecule Retrieval

Run the notebook `./examples/patent_query.ipynb` to use PatCID to retrieve molecules displayed in a given patent document. 

### User Interface 

https://github.com/DS4SD/PatCID/assets/73230090/0fc7c2bd-ce1b-4ded-a278-7d9c4c277244

To request access to the above user interface, please contact the IBM's [Deep Search](https://ds4sd.github.io/) team at deepsearch-core@zurich.ibm.com.

### Benchmark Datasets

The benchmarks datasets [D2C-UNI and D2C-RND are available on Zenodo](https://doi.org/10.5281/zenodo.10978812).

### Code 

The code repositories used to build and evaluate PatCID are available:
- The [classification model](https://github.com/DS4SD/MolClassifier)
- The [recognition model](https://github.com/DS4SD/MolGrapher)
- The [chemical-structure annotation tool](https://github.com/DS4SD/MolAnnotator).

For segmenting chemical-structure images from documents, we use [DECIMER Segmentation](https://github.com/Kohulan/DECIMER-Image-Segmentation) from K. Rajan, H. O. Brinkhaus, M. Sorokina, A. Zielesny and C. Steinbeck.

### Models

The model weights are available on Hugging Face:
- The [classification model](https://huggingface.co/ds4sd/MolClassifier)
- The [recognition model](https://huggingface.co/ds4sd/MolGrapher).

### Training Datasets

The training datasets are available on Zenodo and Hugging Face:
- The [image classification model dataset](https://doi.org/10.5281/zenodo.10978564)
- The [molecule recognition model dataset](https://huggingface.co/datasets/ds4sd/MolGrapher-Synthetic-300K).

### Additional Visualization

To test our processing pipeline outside its main application domain, we process a [scientific publication](https://chemrxiv.org/engage/chemrxiv/article-details/662d287a91aefa6ce198f9b8) published on ChemRxiv. `./data/extra/scientific_paper_example/` contains the pages of the document (`page_*.png`) annotated with the segmentation and classification predictions. For pages containing molecules, the predicted molecules are provided in `page_*_molecules.txt`.

### Citation

If you find this repository useful, please consider citing:

```
﻿@Article{Morin2024,
    author={Morin, Lucas
    and Weber, Val{\'e}ry
    and Meijer, Gerhard Ingmar
    and Yu, Fisher
    and Staar, Peter W. J.},
    title={PatCID: an open-access dataset of chemical structures in patent documents},
    journal={Nature Communications},
    year={2024},
    month={Aug},
    day={02},
    volume={15},
    number={1},
    pages={6532},
    issn={2041-1723},
    doi={10.1038/s41467-024-50779-y},
    url={https://doi.org/10.1038/s41467-024-50779-y}
}
```
