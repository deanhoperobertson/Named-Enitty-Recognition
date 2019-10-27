# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. The data can be found here: https://www.clips.uantwerpen.be/conll2003/ner/ and is under licence by Reuters. 

## Models
### Feature Engineered
- Memory-Based Tagger Model (F1=**0.52**) 
- RandomForest Model (F1=**0.61**) 
- Condition Random Fields [w-1] (F1=**83.29**) 
- Condition Random Fields [w-2] (F1=**84.23**) 
- Condition Random Fields [w-3] (F1=**83.76**) 

### Neural Network 
- BiLSTM (F1=**0.2**)
- BiLSTM-CRF (F1=**0.68**)
- BiLSTM-CRF (+Glove50D Word Embeddings) (F1=**80.9**)
- BiGRU-CRF (+Glove Word Embeddings) (F1=**0.85**)
- BiLSTM-CRF (Char + Word Embeddings) (F1=**0.894**)
- BiLSTM-CRF (Elmo Embeddings) (F1=**0.898**)

## Word Embeddings:
- 6B.Glove.50d
- 6B.Glove.100d
- 6B.Glove.200d
- 6B.Glove.300d
- Fasttext 16B.wiki-news-300d
- Elmo Embeddings

## Requirements
- Python 3.6
- NumPy
- Pandas
- scikit-learn
- Tensorflow
- Keras
