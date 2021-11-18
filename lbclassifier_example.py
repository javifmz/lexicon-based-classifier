
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

labels = [ "positive", "negative" ]

classifier = LexiconBasedClassifier(lexicon, labels=labels)
prediction = classifier.predict(X)
prediction_labels = classifier.get_labels(prediction)
print(prediction, prediction_labels)