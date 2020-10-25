import re
import yaml

class FileFormatError(Exception):
    def __init__(self, ind, msg=None, field=None):
        if msg is None:
            msg = "File format error occured with index {ind}".format(ind=ind)
        if field is not None:
            msg += " field: {field}".format(field=field)
        super(FileFormatError, self).__init__(msg)
        

defaults = {}


    # def read_yaml(self):
    #     read_file = os.path.join(self.institution.storage_directory(), 
    #                               self.statement_name('yaml'))
    #     if os.path.xfisfile(read_file):
    #         with open(read_file) as f:
    #             self.details = yaml.load(f)
    #     else:
    #         raise FileNotFoundError("No such yaml file " + read_file)
    #         with open(write_file, 'w') as f:
    #             f.write(yaml.dump(statement))

def update_from_file(dictionary, file):
    """Update a given dictionary with the fields from a specified file."""
    md= open(file, 'r')
    text = md.read()
    md.close()
    dictionary.update(yaml.load(text, Loader=yaml.FullLoader))
    return dictionary
    

def header_field(field, fields):
    """Return one field from yaml header fields."""
    if field not in fields:
        if field in defaults:
            answer=defaults[field]
        else:
            raise FileFormatError(1, "Field not found in file or defaults.", field)
    else:
        answer = fields[field]
    return answer


def header_fields(filename):
    """Extract headers from a talk file."""
    head, _ = extract_header_body(filename)
    return yaml.load(head, Loader=yaml.FullLoader)

    raise FileFormatError(1, "This does not appear to be a valid talk file.", filename)

def extract_header_body(filename):
    """Extract the text of the headers and body from a yaml headed file."""
    import codecs
    with codecs.open(filename, 'rb', 'utf-8') as f:
        text = f.read()
    z = re.fullmatch("(^---[\s\S]+---)\n([\s\S]*)", text)
    if z:
        return z.groups()[0].replace('---', ''), z.groups()[1]
    else:
        z = re.fullmatch("(^---[\s\S]+---)", text)
        if z:
            return z.groups()[0].replace('---', ''), ''
        else:
            z = re.fullmatch("(^---[\s\S]+)", text)
            if z:
                return z.groups()[0].replace('---', ''), ''
            else:
                raise FileFormatError(1, "This does not appear to be a valid yaml headed file.", filename)

