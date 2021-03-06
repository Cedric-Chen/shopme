# python built-in function
from config import app
import re

@app.context_processor
def utility_processor():
    def split_field_name(text):
        return ' '.join(filter(None, re.split("([A-Z][^A-Z]*)", s)))
    def is_dict(var):
        return type(var) == dict
    def true_or_false(var):
        if var:
            return True
        else:
            return False

    return dict(
        split_field_name = split_field_name,
        is_dict = is_dict,
        true_or_false = true_or_false
        )
