import numpy as np

from .base import BaseTokenTagger


class BooleanTagger(BaseTokenTagger):
    """BooleanTagger
    
    Tagger for all spaCy Token attributes that return a boolean.
    These include: is_alpha, is_ascii, is_digit, is_lower, is_upper,
                   is_title, is_punct, is_left_punct, is_right_punct,
                   is_space, is_bracket, is_quote, is_currency,
                   like_url, like_num, like_email, is_oov, is_stop
                   
    Args:
        boolean_attribute (str): The boolean spaCy attribute to query.
        invert (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
    
    Attributes
        boolean_attribute (str): The boolean spaCy attribute to query.
        condition (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
        indexes (list): List of token indexes that satisfy the tagging
            criteria within their parent documents.
    """
    
    def __init__(self, boolean_attribute='is_stop', invert=False):
        self.boolean_attribute = boolean_attribute
        super().__init__(invert)
        
    def tag_criteria(self, token):
        """tag_criteria
        """
        if getattr(token, self.boolean_attribute):
            return True
        else:
            return False


class MatchTagger(BaseTokenTagger):
    """MatchTagger
    
    Tagger for any spaCy Token attribute that can be used to match any
    user-specified match criteria.
                   
    Args:
        token_attribute (str): The boolean spaCy attribute to query.
        match (str or list-like): A series of criteria that a token is checked
            against.
        invert (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
    
    Attributes
        token_attribute (str): The boolean spaCy attribute to query.
        match (str or list-like): A series of criteria that a token is checked
            against.
        invert (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
        indexes (list): List of token indexes that satisfy the tagging
            criteria within their parent documents.
    """
    
    def __init__(self, token_attribute, match, invert=False):
        self.token_attribute = token_attribute
        
        if np.isscalar(match):
            match = [match]
        self.match = match
        
        super().__init__(invert)
        
    def tag_criteria(self, token):
        token_attribute = self.token_attribute
        match = self.match 
        if getattr(token, token_attribute) in match:
            return True
        else:
            return False


class ValidateTagger(BaseTokenTagger):
    """ValidateTagger
    
    Tagger for using user-defined functions to tag spaCy tokens.
                   
    Args:
        validate (function): Function that returns boolean based on some user-
            specified criteria for a token.
        invert (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
    
    Attributes
        validate (function): Function that returns boolean based on some user-
            specified criteria for a token.
        invert (bool): Whether to return indices of tokens that
            match the condition or do not match the condition. Defaults to
            False.
        indexes (list): List of token indexes that satisfy the tagging
            criteria within their parent documents.
    """
    
    def __init__(self, validate, invert=False):
        self.validate = validate
        super().__init__(invert)
    
    def tag_criteria(self, token):
        return self.validate(token)
