# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. The data can be found here: https://www.clips.uantwerpen.be/conll2003/ner/ and is under licience by Reuters. 

## Models
### Feature Engineered
- Memory-Based Tagger Model (F1=0.52) 
- RandomForest Model (F1=0.61) 
- Condition Random Fields (F1=0.82) 

### Neural Network 
- BiLSTM (F1=0.2)
- BiLSTM-CRF (F1=)
- BiLSTM-CRF (+Glove Word Embeddings) (F1=0.85)
- BiLSTM-CRF (Char + Word Embeddings) (F1=0.89)

## Requirements
- Python 3.6
- NumPy
- Pandas
- scikit-learn
- Tensorflow
- Keras
