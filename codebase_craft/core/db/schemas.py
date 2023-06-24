

project_scaffolding_management_tables = [
    {
        "table_name": "template",
        "columns": [
            {
                "project_dir_id": "uuid"
            }
        ]
    }
]

event_management_tables = [
    {
        "table_name": "events",
        "columns": [
            {
                "event_type": "text"
            }
        ]
    }
]


project_scaffolding_management_schema = {
    "name": "project_scaffolding_management",
    "tables": project_scaffolding_management_tables
}

event_management_schema = {
    "name": "event_management_schema",
    "tables": event_management_tables
}

schemas = [
    project_scaffolding_management_schema,
    event_management_schema

]
