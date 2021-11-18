# Lexicon-based Classifier

Classifies texts using a previously generated lexicon. The lexicon contains a list of weighted terms for each of the classification labels. The weights of these terms are added to each label, and the label with the higher weight is chosen.

### Lexicon format example

```json
{
  "positive": [
    { "term": "excellent", "weight": 1.0 },
    { "term": "good", "weight": 0.7 }
  ],
  "negative": [
    { "term": "horrible", "weight": 1.0 },
    { "term": "bad", "weight": 0.8 }
  ],
}
```

### Basic usage

```python
classifier = LexiconBasedClassifier(lexicon)
prediction = classifier.predict(X)
```

### Usage with different prediction indexes

```python
labels = [ "positive", "negative" ]
classifier = LexiconBasedClassifier(lexicon, labels=labels)
prediction = classifier.predict(X)
```

### Execute the example

```bash
python -m lbclassifier_example