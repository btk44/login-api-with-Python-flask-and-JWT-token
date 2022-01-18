from tools.json_dto_mapper import JsonDtoMapper


class AccountDto:
    def __init__(self):
        self.account_name: str = ''
        self.password: str = ''
        self.id: int = 0

    @staticmethod
    def from_json(json_data):
        return JsonDtoMapper.from_json_to_simple_type_class_fields(json_data, AccountDto)

    def to_json(self):
        return JsonDtoMapper.class_fields_to_json_dict(self, {})
