from __future__ import unicode_literals

from .enums import AchRelationshipApprovalMethod
from .structs import AchRelationshipRequest, AchRelationshipResponseStructV2
from .. import BaseEndpoint
from ..errors import error_from_response
from ... import request

__all__ = ['AchRelationshipV2']


class AchRelationshipV2(BaseEndpoint):
    base_url = '/sentinel/api/v2/ach_relationships%s'

    def create(self, ach_relationship_request:AchRelationshipRequest):
        response = request(self._url(''), 'post',
                           json=ach_relationship_request.to_dict())
        code = response.status_code
        if code == 200:
            return AchRelationshipResponseStructV2(response.json())
        return error_from_response(response)

    def approve(self, ach_relationship_id: str,
                approval_method: AchRelationshipApprovalMethod,
                amount1: float, amount2: float):
        """
        The approval method must match the method that was submitted on
        the creation request and the relationship must be in PENDING state.
        A relationship that has already been canceled cannot be approved.

        For MICRO_DEPOSIT approval relationships: The approval request must
        include the micro deposit amounts that were deposited to the bank
        account. A successful confirmation will result in the relationship
        moving the APPROVED status, and the micro deposits will be taken
        back out of the bank account. A PENDING relationship is limited in
        the number of attempts to approve micro deposit amounts. Once this
        limit has been reached, the micro deposit amounts are pulled back from
        the bank account. A new attempt can be made by re-issuing micro
        deposits to the bank account. This cycle may be repeated a limited
        number of times. After the limit has been reached without a successful
        micro deposit amount confirmation, the relationship will be canceled.

        Example:

        Micro Deposit Amounts #1 - auto generated micro deposits sent to the bank
        Failed Amount Confirmation #1
        Failed Amount Confirmation #2
        Failed Amount Confirmation #3
        Micro Deposits Pulled Back From Bank
        Reissue Micro Deposit Request #1
        Micro Deposit Amounts #2 - new amounts for micro deposits are sent to the bank
        Failed Amount Confirmation #1
        Failed Amount Confirmation #2
        Failed Amount Confirmation #3
        Micro Deposits Pulled Back From Bank
        Reissue Micro Deposit Request #2
        Micro Deposit Amounts #3 - new amounts for micro deposits are sent to the bank
        Failed Amount Confirmation #1
        Failed Amount Confirmation #2
        Failed Amount Confirmation #3
        Micro Deposits Pulled Back From Bank
        RELATIONSHIP AUTO CANCELED FOR MAX FAILURE ATTEMPTS

        :param ach_relationship_id: ACH Relationship ID to approve
        :param approval_method: Approval method to use (only MICRO_DEPOSIT supported)
        :param amount1: First amount withdrawn from the account
        :param amount2: Second amount withdrawn from the account
        :return: AchRelationshipResponseStructV2 or APIError
        """

        r = request(self._url('/%s/approve', ach_relationship_id), 'post',
                    json={
                        'method': approval_method.value,
                        'amount1': amount1,
                        'amount2': amount2,
                    })
        if r.status_code == 200:
            return AchRelationshipResponseStructV2(r.json())
        return error_from_response(r)

    def reissue(self, ach_relationship_id: str):
        r = request(self._url('/%s/reissue', ach_relationship_id), 'post')
        if r.status_code != 200:
            return error_from_response(r)

    def cancel(self, ach_relationship_id: str, comment: str):
        r = request(self._url('/%s/cancel', ach_relationship_id), 'post', {
            'comment': comment,
        })
        if r.status_code == 200:
            return AchRelationshipResponseStructV2(r.json())
        return error_from_response(r)

    def update(self, ach_relationship_id: str, nickname: str):
        """
        Only updates to "nickname" are permitted, other fields will be ignored.
        "nickname" can't be empty or null.
        """
        r = request(self._url('/%s', ach_relationship_id), 'put', {
            'nickname': nickname,
        })
        if r.status_code == 200:
            return AchRelationshipResponseStructV2(r.json())
        return error_from_response(r)

    def get(self, ach_relationship_id: str):
        r = request(self._url('/%s', ach_relationship_id))
        if r.status_code == 200:
            return AchRelationshipResponseStructV2(r.json())
        return error_from_response(r)

    def list(self) -> [AchRelationshipResponseStructV2]:
        r = request(self._url(''))
        if r.status_code == 200:
            object_list = r.json()
            return [AchRelationshipResponseStructV2(o) for o in object_list]
        return error_from_response(r)
