# Lexicon-based Classifier

A lexicon-based classifier

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

See the [example](./libclassifier_example.py)

### Execute example

```bash
python -m lbclassifier_example
```

### Execute example with docker (if python is not installed)

```bash
sudo docker run --rm -it -v "$PWD:/app" lbclassifier python -u -m lbclassifier_example
```

