
import re

class LexiconBasedClassifier :

  def __init__(self, lexicon, tokenizer=None, labels=None) :
    """Creates a classifier using a previously created lexicon"""
    self.lexicon = lexicon
    self.tokenizer = tokenizer if tokenizer is not None else lambda text: re.split('[^\w]+', text.lower())
    self.labels = labels.copy() if labels is not None else [ term for term in lexicon ]
    self.labels_index = { term: index for index, term in enumerate(self.labels) }

  def _get_single_weights(self, raw_document) :
    doc_tokens = set(self.tokenizer(raw_document))
    doc_weight = [0] * len(self.lexicon)
    for label, label_lexicon in self.lexicon.items() :
      label_index = self.labels_index[label]
      for term_data in label_lexicon :
        term = term_data['term']
        term_weight = term_data['weight']
        term_tokens = self.tokenizer(term)
        if term_tokens[0] in doc_tokens :
          doc_weight[label_index] += term_weight
    return doc_weight

  def predict_single(self, raw_document) :
    doc_weight = self._get_single_weights(raw_document)
    max_value = max(doc_weight)
    max_index = doc_weight.index(max_value)
    return max_index
  
  def predict_proba_single(self, raw_document) :    
    doc_weight = self._get_single_weights(raw_document)
    total = sum(doc_weight)
    doc_proba = [ weight / total for weight in doc_weight ] if total > 0 else [0] * len(doc_weight)
    return doc_proba

  def predict_single_label(self, raw_document) :
    label_index = self.predict_single(raw_document)
    return self.labels[label_index]

  def predict_proba_single_label(self, raw_document) :
    doc_proba = self.predict_proba_single(raw_document)
    return { self.labels[label_index]: proba for label_index, proba in enumerate(doc_proba) }

  def predict(self, raw_documents) :
    predict = [0] * len(raw_documents)
    for index, raw_document in enumerate(raw_documents) :
      predict[index] = self.predict_single(raw_document)
    return predict

  def predict_proba(self, raw_documents) :
    predict = [None] * len(raw_documents)
    for index, raw_document in enumerate(raw_documents) :
      predict[index] = self.predict_proba_single(raw_document)
    return predict

  def predict_labels(self, raw_documents) :
    prediction = self.predict(raw_documents)
    return self.get_labels(prediction)

  def predict_proba_labels(self, raw_documents) :
    prediction = self.predict_proba(raw_documents)
    return self.get_proba_labels(prediction)

  def get_labels(self, prediction) :
    return [ self.labels[label_index] for label_index in prediction ]
  
  def get_proba_labels(self, prediction_proba) :
    return [ { self.labels[label_index]: proba for label_index, proba in enumerate(doc_proba) } for doc_proba in prediction_proba ]