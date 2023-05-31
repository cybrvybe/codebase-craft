from nexus_db.core.api.cross_app_db_interface import CrossAppDbInterface

class TemplateManagementSchemaInterface(CrossAppDbInterface):
    def __init__(self):
        super().__init__(scShohema_name="template_management")
        