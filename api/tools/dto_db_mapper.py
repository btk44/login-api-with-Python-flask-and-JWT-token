from flask_sqlalchemy import inspect
from common.database import database


class DtoDbMapper:
    __map_configs = {
        # AccountModel: { AccountDto : { 'email' : lambda dto: ''.join(dto.password),
        #                                'password' : lambda dto: dto.email } }
    }

    @staticmethod
    def map(source, destination):
        if not source:
            return destination
        if not destination:
            return None
        if isinstance(destination, type):
            destination = destination() # change given type into instance

        destination_type = type(destination)
        destination_map_config = DtoDbMapper.__map_configs[destination_type] if destination_type in DtoDbMapper.__map_configs else None
        destination_source_map_config = None
        if destination_map_config:
            source_type = type(source)
            destination_source_map_config = destination_map_config[source_type] if source_type in destination_map_config else None

        source_attributes = vars(source).keys()

        attribute_names = vars(destination).keys() if not isinstance(destination, database.Model) else inspect(destination).attrs.keys()

        for destination_attribute_name in attribute_names:
            if destination_source_map_config and destination_attribute_name in destination_source_map_config:
                setattr(destination, destination_attribute_name, destination_source_map_config[destination_attribute_name](source))
            elif destination_attribute_name in source_attributes:
                setattr(destination, destination_attribute_name, getattr(source, destination_attribute_name))

        return destination
