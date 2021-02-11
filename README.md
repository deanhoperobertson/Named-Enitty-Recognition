# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. The data can be found here: https://www.clips.uantwerpen.be/conll2003/ner/ and is under licence by Reuters. 

## Models
### Feature Engineered
- Conditional Random Fields [w] (F1=**77.73**) 
- Conditional Random Fields [w-1] (F1=**83.54**) 
- Conditional Random Fields [w-2] (F1=**83.25**) 
- Conditional Random Fields [w-3] (F1=**83.91**) 

### Neural Network + Word Embeddings
#### Glove
- BiLSTM-CRF (Glove 50D) (F1=**82.55**)

#### SENNA
- BiLSTM-CRF (SENNA 50D) (F1=**82.79**)

### Neural Network + Word Embeddings + Casing
- BiLSTM-CRF (6B Glove 50D + Features) (F1=**85.20**)
- BiLSTM-CRF (SENNA 50D + Features) (F1=**85.55**)

## Other Models
- BiLSTM-CRF (42B + Glove 300D) (F1=**75**)
- BiLSTM-CRF (Char + Word Embeddings) (F1=**89.4**)
- BiLSTM-CRF (Elmo Embeddings) (F1=**89.8**)

## Word Embeddings:
- Standford Glove
- SENNA
- Elmo Embeddings

## Requirements
- Python 3.6
- NumPy
- Pandas
- scikit-learn
- Tensorflow
- Keras
