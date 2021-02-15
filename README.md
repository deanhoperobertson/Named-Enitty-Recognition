# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. The data can be found here: https://www.clips.uantwerpen.be/conll2003/ner/ and is under licence by Reuters. 

## Models
### Feature Engineered
- Conditional Random Fields [w] (F1=**77.73**) 
- Conditional Random Fields [w-1] (F1=**83.54**) 
- Conditional Random Fields [w-2] (F1=**83.25**) 
- Conditional Random Fields [w-3] (F1=**83.91**) 

### BiLSTM-CRF + Word Embeddings
![BiLSTM_CRF](https://github.com/deanhoperobertson/Named-Enitty-Recognition/blob/master/Thesis/Images/BiLSTM_CRF.png){width=50%}
#### Glove
- BiLSTM-CRF (Glove 50D) (F1=**82.55**)

#### SENNA
- BiLSTM-CRF (SENNA 50D) (F1=**82.79**)

## Other Models
- BiLSTM-CRF (Glove + Casing Features) (F1=**86.23**)
- BiLSTM-CRF (SENNA + Casing Features) (F1=**85.35**)

## Word Embeddings:
- GloVe
- SENNA

## Requirements
- Python 3.6
- NumPy
- Pandas
- scikit-learn
- Tensorflow
- Keras
