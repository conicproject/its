import time
import json
from datetime import datetime, timedelta

from django.http import StreamingHttpResponse

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.repositories.user import UserRepository
from api.repositories.blacklist import BlacklistRepository
from api.repositories.blacklistPassing import BlacklistPassingRepository

def gen(group_id, blacklist_ids):

    checker = True
    counter = 1

    while True:

        if counter == 1:

            result = {
                'status': False,
                'message': 'init notification'
            }

            json_string = json.dumps(result)
            response = 'data: {}\n\n'.format(json_string)

            yield response
            counter = 0

        now = datetime.now() - timedelta(seconds=30)
        sec = now.second

        if sec % 30 == 0:
            if checker:
                time.sleep(2)

                diff = now - timedelta(
                    seconds=30
                )
                date = now.strftime('%Y-%m-%d')

                end_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
                start_datetime = diff.strftime('%Y-%m-%d %H:%M:%S')

                if group_id != 1:
                    if len(blacklist_ids) == 1:
                        blacklist_ids = str(blacklist_ids)
                        blacklist_ids = blacklist_ids.replace(',', '')

                    if len(blacklist_ids) != 0:
                        data = BlacklistPassingRepository().search_notification(
                            start_datetime=start_datetime, end_datetime=end_datetime,
                            blacklist_ids=blacklist_ids
                        )
                        result = {
                            'message': 'notification alert',
                            'data': data,
                            'date': date
                        }
                    else:
                        result = {
                            'message': 'notification alert',
                            'data': [],
                            'date': date
                        }
                else:
                    data = BlacklistPassingRepository().search_notification_master_group(
                        start_datetime=start_datetime, end_datetime=end_datetime
                    )

                    result = {
                        'message': 'notification alert',
                        'data': data,
                        'date': date
                    }
                
                if result['data']:
                    result['status'] = True

                else:
                    result['status'] = False

                json_string = json.dumps(result)
                response = 'data: {}\n\n'.format(json_string)

                yield response

                checker = False
        else:
            checker = True 


def stream(request):

    payloads = SessionValidator().validate_session(
        headers=request.GET
    )
    FeatureValidator().validate_traffic_view(
        user_id=payloads['user_id']
    )
    user = UserRepository().get_by_id(id=payloads['user_id'])
    group_id = user.group_id
    blacklist_ids = tuple(BlacklistRepository()
        .get_all_by_group(group_id=group_id)
        .values_list('id', flat=True)
    )

    response = StreamingHttpResponse(gen(group_id=group_id, blacklist_ids=blacklist_ids), content_type='text/event-stream')

    return response