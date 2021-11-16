
from lbclassifier import LexiconBasedClassifier

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

X = [
  'This book is excellent',
  'This book is horrible',
]

labels_index = {
  "positive": 0,
  "negative": 1,
}

classifier = LexiconBasedClassifier(lexicon, labels_index=labels_index)
prediction = classifier.predict(X)
