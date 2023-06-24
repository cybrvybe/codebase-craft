import unittest
import os
from nexus_db.core.api.db_direct_access_point import DbDirectAccessPoint
from codebase_craft.core.db.interfaces.schema import SchemaInterface

class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_db_api_url = os.getenv("TEST_DB_API_URL", "http://127.0.0.1:5000")
        cls.db_access_point = DbDirectAccessPoint(test_db_api_url)
        cls.schema_name = "test_schema"
        cls.schema_interface = SchemaInterface(cls.schema_name)

    def test_create_schema(self):
        self.db_access_point.create_schema(self.schema_name)

    def test_create_table(self):
        table_name = "test_table"
        table_columns = {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT NOT NULL",
            "age": "INTEGER"
        }
        self.schema_interface.create_new_table(table_name, table_columns)

    # Add more tests for creating tables with different column types

if __name__ == "__main__":
    unittest.main()
