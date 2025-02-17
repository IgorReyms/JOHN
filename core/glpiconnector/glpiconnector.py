from __future__ import annotations

import os

from core.config.engine import ConfigEngine



class GLPIConnector:
    glpi_api_url_prod = os.getenv("GLPI_API_URL_PROD")
    glpi_api_url_test = os.getenv("GLPI_API_URL_TEST")
    glpi_api_apptoken_prod = os.getenv("GLPI_API_APP_TOKEN_PROD")
    glpi_api_apptoken_test = os.getenv("GLPI_API_APP_TOKEN_TEST")
    glpi_api_usertoken_prod = os.getenv("GLPI_API_USER_TOKEN_PROD")
    glpi_api_usertoken_test = os.getenv("GLPI_API_USER_TOKEN_TEST")
    def __init__(self,
                 connect_prod: bool = False,
                 connect_test: bool = False):
        pass



GLPIConnector.init_connector_settings(GLPIConnector)
o = GLPIConnector()




