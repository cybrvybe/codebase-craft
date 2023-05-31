from core.db.templates.template_management_schema_interface import TemplateManagementSchemaInterface

class DbInitializer:
    def __init__(self):
        self.schema_interface=TemplateManagementSchemaInterface()
        self.schema_names = ['template_management']
    def init_db(self):
        self.schema_interface.create_schema()

    def init_schemas(self):
        for schema_name in self.schema_names:
            self.schema_interface.create_schema(schema_name=schema_name)
    def
