import json

def class_to_json(obj):
    dict = class_to_dict(obj)
    # print(dict)
    json_str = json.dumps(dict).replace('\\\\','\\')
    return json_str

def dict_to_json(dict):
    json_str = json.dumps(dict).replace('\\\\', '\\')
    return json_str

def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            #把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            #  dict = class_to_json(o)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict