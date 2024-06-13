# Copyright (c) 2023 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import os
from dotenv import load_dotenv

class Config:
    def __init__(self, **kwargs):
        self.ABBaseURL = kwargs.get('AB_BASE_URL')
        self.ABClientID = kwargs.get('AB_CLIENT_ID')
        self.ABClientSecret = kwargs.get('AB_CLIENT_SECRET')
        self.ABNamespace = kwargs.get('AB_NAMESPACE')
        self.ABUsername = kwargs.get('AB_USERNAME')
        self.ABPassword = kwargs.get('AB_PASSWORD')
        self.GRPCServerURL = kwargs.get('GRPC_SERVER_URL')
        self.ExtendAppName = kwargs.get('EXTEND_APP_NAME', "pythonLootBoxApp")

def get_config():
    load_dotenv()  # Load environment variables from .env file

    required_variables = ['AB_BASE_URL', 'AB_CLIENT_ID', 'AB_CLIENT_SECRET', 'AB_NAMESPACE', 'AB_USERNAME', 'AB_PASSWORD', 'GRPC_SERVER_URL', 'EXTEND_APP_NAME']
    missing_variables = []
    config_values = {}

    for variable in required_variables:
        value = os.getenv(variable)
        if value is None:
            missing_variables.append(variable)
        else:
            config_values[variable] = value

    # if missing_variables:
    #     raise ValueError(f"Missing environment variables: {', '.join(missing_variables)}")

    config = Config(**config_values)
    return config