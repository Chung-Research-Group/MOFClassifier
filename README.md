## MOFClassifier: A Machine Learning Approach for Validating Computation-Ready Metal-Organic Frameworks
                                                                                                                                          
[![Static Badge](https://img.shields.io/badge/arXiv.2506.14845v1-brightgreen?style=flat)](https://arxiv.org/abs/2506.14845)
![GitHub repo size](https://img.shields.io/github/repo-size/Chung-Research-Group/MOFClassifier?logo=github&logoColor=white&label=Repo%20Size)
[![PyPI](https://img.shields.io/pypi/v/MOFClassifier?logo=pypi&logoColor=white)](https://pypi.org/project/MOFClassifier?logo=pypi&logoColor=white)
[![Requires Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg?logo=python&logoColor=white)](https://python.org/downloads)
[![GitHub license](https://img.shields.io/github/license/Chung-Research-Group/MOFClassifier.svg)](https://github.com/mtap-research/MOFClassifier/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Chung-Research-Group/MOFClassifier.svg)](https://GitHub.com/Chung-Research-Group/MOFClassifier/issues/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15654431.svg)](https://doi.org/10.5281/zenodo.15654431)
                                                                     
**Developed by:** [Guobin Zhao](https://github.com/sxm13)                                
                                                                                                         
### Installation 
                                     
```sh
pip install MOFClassifier
```

### Examples                                                                                                     
```python
from MOFClassifier import CLscore
result = CLscore.predict(root_cif="./example.cif", model="core")
```
-  **root_cif**: the path of your structure
-  **model**: the model name: a. "core": training with CoRE MOF DB; b. "qsp": training with CoRE MOF DB and QMOF DB; c. "h": training with ToBaCCo (Hypothetical MOFs)
-  **result**: a. cifid: the name of structure; b. all_score: the CLscore predicted by 100 models (bags); c. mean_score: the mean CLscore of CLscores                                                 

```python
from MOFClassifier import CLscore
results = CLscore.predict_batch(root_cifs=["./example1.cif""./example2.cif","./example3.cif"], model="core", batch_size=512)
```
-  **root_cifs**: the path of your structures
-  **model**: the model name: a. "core": training with CoRE MOF DB; b. "qsp": training with CoRE MOF DB and QMOF DB; c. "h": training with ToBaCCo (Hypothetical MOFs)
-  **batch_size**: the number of samples
-  **results**: a. cifid: the name of structure; b. all_score: the CLscore predicted by 100 models (bags); c. mean_score: the mean CLscore of CLscores  
                                                                                
### Citation                                          
**Guobin Zhao**, **Pengyu Zhao** and **Yongchul G. Chung**. 2025. **arXiv.2506.14845**.


### Acknowledgments
We thank [henk789](https://github.com/henk789) for contribution to batch prediction.