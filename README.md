# Named-Enitty-Recognition

This repository explores different techiques used for Named Entity Recognition (NER) on the CONLL 2003 Reuters Dataset. 

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

- 

## Requirements
- Python 3.6
- NumPy
- Pandas
- scikit-learn
- Tensorflow
- Keras
