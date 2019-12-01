# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. The data can be found here: https://www.clips.uantwerpen.be/conll2003/ner/ and is under licence by Reuters. 

## Models
### Feature Engineered
- Conditional Random Fields [w] (F1=**78.50**) 
- Conditional Random Fields [w-1] (F1=**83.66**) 
- Conditional Random Fields [w-2] (F1=**84.93**) 
- Conditional Random Fields [w-3] (F1=**84.54**) 

### Neural Network 
- BiLSTM (F1=**0.2**)
- BiLSTM-CRF (F1=**53.3**)
- BiLSTM-CRF (6B + Glove 50D) (F1=**81.4**)
- BiLSTM-CRF (6B + Glove 100D) (F1=**82.4**)
- BiLSTM-CRF (6B + Glove 200D) (F1=**83.5**)
- BiLSTM-CRF (6B + Glove 300D) (F1=**83.1**)
- BiLSTM-CRF (Casing Features + 6B Glove 50D) (F1=**0.857**)

## Other Models
- Memory-Based Tagger Model (F1=**52**) 
- RandomForest Model (F1=**61**) 
- BiLSTM-CRF (42B + Glove 300D) (F1=**75**)
- BiLSTM-CRF (Char + Word Embeddings) (F1=**89.4**)
- BiLSTM-CRF (Elmo Embeddings) (F1=**89.8**)

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
