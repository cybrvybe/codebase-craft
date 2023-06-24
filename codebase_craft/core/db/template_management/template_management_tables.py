template_management_tables = [
    {
        "table_name": "templates",
        "table_columns": {
            "pre_templating_dir_structure_id": 'uuid',
            "post_templating_dir_structure_id": 'uuid'
        }

    },
    {
        "table_name": "project_dir_structures",
        "table_columns": {
            "id": "uuid",
            "dir_structure": "text"
        }
    }
]
