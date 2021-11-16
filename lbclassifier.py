
import re

class LexiconBasedClassifier :

  def __init__(self, lexicon, tokenizer=None, labels_index=None) :
    """Creates a classifier using a previously created lexicon"""
    self.lexicon = lexicon
    self.tokenizer = tokenizer if tokenizer is not None else lambda text: re.split('[^\w]+', text.lower())
    self.labels_index = labels_index if labels_index is not None else { term: index for index, term in enumerate(lexicon) }      

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
      predict[doc_index] = 0