
from lbclassifier import LexiconBasedClassifier

# Lexicon
lexicon = {
  "positive": [
    { "term": "excellent", "weight": 1.0 },
    { "term": "good", "weight": 0.7 }
  ],
  "negative": [
    { "term": "horrible", "weight": 1.0 },
    { "term": "bad", "weight": 0.8 }
  ],
}

# Documents to classify
raw_documents = [
  'This book is excellent',
  'This book is horrible',
]

# Ordered labels (only necessary if the order is different from the lexicon)
labels = [ "positive", "negative" ]

# Create the classifier
classifier = LexiconBasedClassifier(lexicon, labels=labels)

# Predict the labels index of a dataset
predict = classifier.predict(raw_documents)
print(predict)

# Predict the labels of a dataset
predict_labels = classifier.predict_labels(raw_documents)
print(predict_labels)

# Predict with probabilities for a dataset
predict_proba = classifier.predict_proba(raw_documents)
print(predict_proba)

# Predict with labels and probabilities for a dataset
predict_proba_labels = classifier.predict_proba_labels(raw_documents)
print(predict_proba_labels)

# Predict the label index of a single instance
predict_single = classifier.predict_single(raw_documents[0])
print(predict_single)

# Predict the label of a single instance
predict_single_label = classifier.predict_single_label(raw_documents[0])
print(predict_single_label)

# Predict with probabilities for a single instance
predict_proba_single = classifier.predict_proba_single(raw_documents[0])
print(predict_proba_single)

# Predict with labels and probabilities for a single instance
predict_proba_single_label = classifier.predict_proba_single_label(raw_documents[0])
print(predict_proba_single_label)