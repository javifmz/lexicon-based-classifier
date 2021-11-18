
import re

class LexiconBasedClassifier :

  def __init__(self, lexicon, tokenizer=None, labels=None) :
    """Creates a classifier using a previously created lexicon"""
    self.lexicon = lexicon
    self.tokenizer = tokenizer if tokenizer is not None else lambda text: re.split('[^\w]+', text.lower())
    self.labels = labels.copy() if labels is not None else [ term for term in lexicon ]
    self.labels_index = { term: index for index, term in enumerate(self.labels) }

  def fit(self, X) :
    """This method does nothing, only for compatibility"""
    pass

  def predict(self, X) :
    predict = [0] * len(X)
    for doc_index, doc in enumerate(X) :
      doc_tokens = set(self.tokenizer(doc))
      doc_weight = [0] * len(self.lexicon)
      for label, label_lexicon in self.lexicon.items() :
        label_index = self.labels_index[label]
        for term_data in label_lexicon :
          term = term_data['term']
          term_weight = term_data['weight']
          term_tokens = self.tokenizer(term)
          if term_tokens[0] in doc_tokens :
            doc_weight[label_index] += term_weight
      max_value = max(doc_weight)
      max_index = doc_weight.index(max_value)
      predict[doc_index] = max_index
    return predict
  
  def predict_labels(self, X) :
    prediction = self.predict(X)
    return self.get_labels(prediction)

  def get_labels(self, prediction) :
    return [ self.labels[label_index] for label_index in prediction ]