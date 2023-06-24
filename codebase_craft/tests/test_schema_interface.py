import unittest
from nexus_db.core.api.cross_app_db_interface import CrossAppDbInterface
from codebase_craft.core.db.interfaces.schema import SchemaInterface

class TestSchemaInterface(unittest.TestCase):
    def setUp(self):
        self.schema_name = "test_schema"
        self.schema_interface = SchemaInterface(self.schema_name)

    def test_get_schema_name(self):
        self.assertEqual(self.schema_interface.get_schema_name(), self.schema_name)

    def tearDown(self):
        self.schema_interface.drop_schema(self.schema_name)

    # Add more tests for other functions

if __name__ == "__main__":
    unittest.main()
