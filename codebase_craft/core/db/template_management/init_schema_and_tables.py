from ..interfaces.schema import SchemaInterface

class TemplateManagementSchemaAndTableInitializer:
    def __init__(self):
        self.schema_interface=SchemaInterface(schema_name="template_management")
        self.tables_dicts= [
            {
                "name": 'templates',
                "schema_name": 'template_management'
            },
            {
                "name": 'project_dir_structures',
                "schema_name": "template_management"
            },
            {
                "name": 'dependencies',
                "schema_name": "template_management"
            }
        ]
    def init_db(self, tables):
        self.schema_interface.create_schema()
        self.schema_interface.create_tables(tables)

    def init_schemas(self):
        for schema_name in self.schema_names:
            self.schema_interface.create_schema(schema_name=schema_name)

    def create_tables(self):
        for table_dict in self.tables_dicts:
            table_name = table_dict["name"]
            schema_name = table_dict["schema_name"]
            self.schema_interface =
