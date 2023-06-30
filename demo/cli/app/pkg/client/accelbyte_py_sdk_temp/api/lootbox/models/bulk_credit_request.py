# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
# 
# Code generated. DO NOT EDIT!

# template file: ags_py_codegen

# AccelByte Gaming Services Platform Service (4.30.2)

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model

from ..models.credit_request import CreditRequest


class BulkCreditRequest(Model):
    """Bulk credit request (BulkCreditRequest)

    Properties:
        credit_request: (creditRequest) OPTIONAL CreditRequest

        currency_code: (currencyCode) OPTIONAL str

        user_ids: (userIds) OPTIONAL List[str]
    """

    # region fields

    credit_request: CreditRequest                                                                  # OPTIONAL
    currency_code: str                                                                             # OPTIONAL
    user_ids: List[str]                                                                            # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_credit_request(self, value: CreditRequest) -> BulkCreditRequest:
        self.credit_request = value
        return self

    def with_currency_code(self, value: str) -> BulkCreditRequest:
        self.currency_code = value
        return self

    def with_user_ids(self, value: List[str]) -> BulkCreditRequest:
        self.user_ids = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result: dict = {}
        if hasattr(self, "credit_request"):
            result["creditRequest"] = self.credit_request.to_dict(include_empty=include_empty)
        elif include_empty:
            result["creditRequest"] = CreditRequest()
        if hasattr(self, "currency_code"):
            result["currencyCode"] = str(self.currency_code)
        elif include_empty:
            result["currencyCode"] = ""
        if hasattr(self, "user_ids"):
            result["userIds"] = [str(i0) for i0 in self.user_ids]
        elif include_empty:
            result["userIds"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        credit_request: Optional[CreditRequest] = None,
        currency_code: Optional[str] = None,
        user_ids: Optional[List[str]] = None,
    **kwargs
    ) -> BulkCreditRequest:
        instance = cls()
        if credit_request is not None:
            instance.credit_request = credit_request
        if currency_code is not None:
            instance.currency_code = currency_code
        if user_ids is not None:
            instance.user_ids = user_ids
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkCreditRequest:
        instance = cls()
        if not dict_:
            return instance
        if "creditRequest" in dict_ and dict_["creditRequest"] is not None:
            instance.credit_request = CreditRequest.create_from_dict(dict_["creditRequest"], include_empty=include_empty)
        elif include_empty:
            instance.credit_request = CreditRequest()
        if "currencyCode" in dict_ and dict_["currencyCode"] is not None:
            instance.currency_code = str(dict_["currencyCode"])
        elif include_empty:
            instance.currency_code = ""
        if "userIds" in dict_ and dict_["userIds"] is not None:
            instance.user_ids = [str(i0) for i0 in dict_["userIds"]]
        elif include_empty:
            instance.user_ids = []
        return instance

    @classmethod
    def create_many_from_dict(cls, dict_: dict, include_empty: bool = False) -> Dict[str, BulkCreditRequest]:
        return {k: cls.create_from_dict(v, include_empty=include_empty) for k, v in dict_} if dict_ else {}

    @classmethod
    def create_many_from_list(cls, list_: list, include_empty: bool = False) -> List[BulkCreditRequest]:
        return [cls.create_from_dict(i, include_empty=include_empty) for i in list_] if list_ else []

    @classmethod
    def create_from_any(cls, any_: any, include_empty: bool = False, many: bool = False) -> Union[BulkCreditRequest, List[BulkCreditRequest], Dict[Any, BulkCreditRequest]]:
        if many:
            if isinstance(any_, dict):
                return cls.create_many_from_dict(any_, include_empty=include_empty)
            elif isinstance(any_, list):
                return cls.create_many_from_list(any_, include_empty=include_empty)
            else:
                raise ValueError()
        else:
            return cls.create_from_dict(any_, include_empty=include_empty)

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "creditRequest": "credit_request",
            "currencyCode": "currency_code",
            "userIds": "user_ids",
        }

    @staticmethod
    def get_required_map() -> Dict[str, bool]:
        return {
            "creditRequest": False,
            "currencyCode": False,
            "userIds": False,
        }

    # endregion static methods