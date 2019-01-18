def tokenise(line, separator):
    buffer_line = ''
    field = ''
    in_quotes = 0
    splits = []
    for i in range(len(line)):
        # Check for toggling of quotes
        if line[i] == '"' and not buffer_line == '\\':
            in_quotes = not in_quotes
            buffer_line = line[i]
        else:
            # check for separator and end of field
            if not in_quotes and line[i]==separator:
                splits.append(field)
                buffer_line = separator
                field = ''
                continue
            if line[i] == '\n':
                splits.append(field)
                field = ''
            # remove whitespace at end and start of field
            if not in_quotes and line[i]==' ':
                buffer_line = ' '
                continue
            # check for escape character
            if line[i]=='\\':
                # check if it is escaped!
                if buffer_line=='\\':
                    field = field + line[i]
                    buffer_line == ''
                    continue
                else:
                    buffer_line == '\\'                    
            else:
                field = field + line[i]
    return splits

def validate_email(address):
    if len(address)>7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", address) != none:
            return 1
    return 0

def string_from_file(file_name):
    file_handle = open(file_name, 'r')
    read_lines = file_handle.readlines()
    file_handle.close()
    text = ''
    for line in read_lines:
        text += line
        text += '\n'
    return text

