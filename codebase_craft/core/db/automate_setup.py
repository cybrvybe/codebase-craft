from codebase_craft.core.db.interfaces.schema import SchemaInterface
from codebase_craft.core.db.schemas import schemas

def main():
    schema_name = "project_scaffolding_management"
    schema_interface = SchemaInterface(schema_name=schema_name)
    schema_interface.init_db(schemas=schemas)

if __name__ == "__main__":
    main()
