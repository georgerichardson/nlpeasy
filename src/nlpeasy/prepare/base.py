
class BaseTokenTagger():
    """BaseTokenTagger
    
    Provides a bass class to perform tagging at the token level.
    """
    
    def __init__(self, invert=False):
        self.invert = invert
        
    def tag_criteria(self, token):
        """tag_criteria
        Function to be overwritten.
        """
        return True
        
    def invert_tag(self, condition):
        return True - condition
    
    def tag(self, documents):
        invert = self.invert
        indexes = []
        for document in documents:
            document_indexes = []
            for token in document:
                tag = self.tag_criteria(token)
                if invert:
                    tag = self.invert_tag(tag)
                if tag:
                    document_indexes.append(token.i)
                else:
                    continue
            indexes.append(document_indexes)
        self.indexes = indexes
