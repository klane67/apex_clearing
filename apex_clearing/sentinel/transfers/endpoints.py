from __future__ import unicode_literals

from datetime import datetime

from .enums import TransferDirection, TransferMechanism, TransferState
from .structs import AchDepositRequest, AchDepositResponse, \
    AchWithdrawalRequest, TransferResponse, TransferSummaryStruct
from .. import BaseEndpoint
from ..errors import APIError, error_from_response
from ... import request

__all__ = [
    'Transfer',
    'AchTransfer',
]


class Transfer(BaseEndpoint):
    base_url = '/v1/transfers%s'

    def list(self, account_id: str,
             start_date: datetime = None, end_date: datetime = None,
             direction: [TransferDirection] = None,
             mechanism: [TransferMechanism] = None,
             state: [TransferState] = None) \
            -> [TransferSummaryStruct] or APIError:
        params = {
            'account': account_id
        }
        if start_date is not None:
            params['start_date'] = start_date.isoformat('T')
        if end_date is not None:
            params['end_date'] = end_date.isoformat('T')
        if direction is not None:
            params['direction'] = direction
        if mechanism is not None:
            params['mechanism'] = mechanism
        if state is not None:
            params['state'] = state

        r = request(self._url(''), params=params)
        if r.status_code == 200:
            object_list = r.json()
            return [TransferSummaryStruct(o) for o in object_list]
        return error_from_response(r)

    def status(self, transfer_id) -> TransferSummaryStruct or APIError:
        r = request(self._url('/%s', transfer_id))
        if r.status_code == 200:
            return TransferSummaryStruct(r.json())
        return error_from_response(r)


class AchTransfer(Transfer):
    base_url = '/v1/transfers/achs/%s'

    def incoming(self, ach_deposit_request: AchDepositRequest) \
            -> AchDepositResponse or APIError:
        """
        The submitted information will be validated and then evaluated.
        Once a transfer is evaluated the status of the transfer will be
        returned to the submitter. Transfers submitted after the daily cutoff
        will not be evaluated until the following day.
        """
        r = request(self._url('/incoming'), 'post',
                    json=ach_deposit_request.to_dict())
        if r.status_code == 200:
            return AchDepositResponse(r.json())
        return error_from_response(r)

    def outgoing(self, ach_withdrawal_request: AchWithdrawalRequest) \
            -> AchDepositResponse or APIError:
        """
        The submitted information will be validated and then evaluated. Once a
        transfer is evaluated the status of the transfer will be returned to
        the submitter. Transfers submitted after the daily cutoff will not be
        evaluated until the following day.
        """
        r = request(self._url('/outgoing'), 'post',
                    json=ach_withdrawal_request.to_dict())
        if r.status_code == 200:
            return AchDepositResponse(r.json())
        return error_from_response(r)

    def status(self, transfer_id) -> TransferResponse or APIError:
        r = request(self._url('/%s', transfer_id))
        if r.status_code == 200:
            return TransferResponse(r.json())
        return error_from_response(r)

    def cancel(self, transfer_id,
               comment: str) -> TransferResponse or APIError:
        """
        Transfers may be canceled up until they are submitted to the bank.
        """
        r = request(self._url('/%s/cancel', transfer_id), 'post', {
            'comment': comment,
        })
        if r.status_code == 200:
            return TransferResponse(r.json())
        return error_from_response(r)
