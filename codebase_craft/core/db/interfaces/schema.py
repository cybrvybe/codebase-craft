from nexus_db.core.api.cross_app_db_interface import CrossAppDbInterface

class SchemaInterface(CrossAppDbInterface):
    def __init__(self, schema_name):
        self.schema_name = schema_name
        super().__init__(schema_name=self.schema_name)

    def get_schema_name(self):
        return self.schema_name

