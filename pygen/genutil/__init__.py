import re

# HTML generation utilities

no_content_tags = ["img", "link", "br"]

div = "div"
img = "img"
a = "a"

def print_element(tag, content=None, **kwargs):
    print(f"<{tag}", end='')
    
    if kwargs != None and len(kwargs) > 0:
        print(" ", end='')
        for (k, v) in kwargs.items():
            print(f"{k}=\"{v}\" ", end='')
    
    if content == None and tag in no_content_tags:
        print("/>", end='\n')
        return
    else:
        print(">", end='')

    if content != None:
        print(content,end='')

    print(f"</{tag}>", end='\n')
    
element = print_element

def include_template(source_file, vars):
    file_text = open(source_file).read()
    for k, v in vars.items():
        file_text = file_text.replace(f"${k}", str(v))
    print(file_text)

template = include_template

info_directory = "../wc/"
info_extension = ".info"
info_pattern = re.compile("(\\S+)\\s*:\\s*(?:{([\\s\\S]*?)}|(.*))")
def get_vars(path):
    result = {
        "get_link": path
    }

    file_text = open(f"{info_directory}{path}{info_extension}").read()
    items = re.findall(info_pattern, file_text)
    for (name, long_value, value) in items:
        k = name.strip()
        v = ""
        if len(long_value) > 0:
            v = long_value.strip()
        elif len(value) > 0:
            v = value.strip()
        
        if k in result:
            if isinstance(result[k], list):
                result[k].append(v)
            else:
                result[k] = [result[k], v]
        else:
            result[k] = v
        
    return result

def get_listing(folder):
    return []