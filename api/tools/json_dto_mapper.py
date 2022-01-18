import datetime


class JsonDtoMapper:
    __simple_types = (str, int, float, complex, bool, datetime.datetime)
    __is_camel_case = True

    @staticmethod
    def from_json_to_typed_list(json_list: list, type_to_convert_to: type):
        if type(json_list) is list:
            return [JsonDtoMapper.convert_value(item, type_to_convert_to) for item in json_list]
        
        return json_list

    @staticmethod
    def from_json_to_typed_dict(json_dict: dict, key_type_to_convert_to: type, value_type_to_convert_to: type):
        if type(json_dict) is dict:
            return {JsonDtoMapper.convert_value(json_key, key_type_to_convert_to):
                    JsonDtoMapper.convert_value(json_value, value_type_to_convert_to)
                    for json_key, json_value in json_dict}
            
        return json_dict

    @staticmethod
    def from_json_to_simple_type_class_fields(json_dict: dict, dto_type: type):      
        dto = dto_type()
        if type(json_dict) is dict:
            for property_name, property_value in vars(dto).items():
                property_json_key = JsonDtoMapper.attribute_name_to_json_key(property_name)
                if property_json_key in json_dict:
                    property_type = type(property_value)  # all instance properties must be initialized in __init__
                    json_value = json_dict[property_json_key]
                    if property_type in JsonDtoMapper.__simple_types:
                        setattr(dto, property_name, JsonDtoMapper.convert_value(json_value, property_type))

        return dto

    @staticmethod
    def class_fields_to_json_dict(dto, complex_fields_dict_to_append: dict):
        json_dict = dict()
        for property_name, property_value in vars(dto).items():
            property_json_key = JsonDtoMapper.attribute_name_to_json_key(property_name)              

            if not complex_fields_dict_to_append or property_name not in complex_fields_dict_to_append.keys():
                json_dict[property_json_key] = property_value
            else:
                json_dict[property_json_key] = complex_fields_dict_to_append[property_name]

        return json_dict

    @staticmethod
    def convert_value(value, destination_type: type):       
        try:
            return destination_type(value)
        except ValueError:
            return destination_type()

    @staticmethod
    def attribute_name_to_json_key(attribute_name: str):
        if JsonDtoMapper.__is_camel_case:
            name = ''.join([name_part.capitalize() for name_part in attribute_name.split('_')])
            return name[0].lower() + name[1:]
        else:  # snake case
            return attribute_name
