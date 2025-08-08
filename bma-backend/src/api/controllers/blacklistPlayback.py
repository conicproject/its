import cv2
import datetime
from django.http import StreamingHttpResponse, FileResponse, JsonResponse

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator

from api.repositories.blacklistPassing import BlacklistPassingRepository
from api.repositories.oracleVehiclePass import OracleVehiclePassRepository
from api.logics.trafficView import TrafficViewLogic


def gen(url):

    capture = cv2.VideoCapture(url)

    while(capture.isOpened()):
        success, frame = capture.read()
        if not success:
            break
        else:
            frame = cv2.resize(frame, (1152, 648))
            ret, buffer = cv2.imencode('.jpg', frame)
            cv2.waitKey(10)
            # frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytearray(buffer) + b'\r\n')


def camerafeed(request):

    payloads = SessionValidator().validate_session(
        headers=request.GET
    )
    FeatureValidator().validate_vehicle_search(
        user_id=payloads['user_id']
    )

    blacklist_passing_id = request.GET.get('id', False)

    if blacklist_passing_id:
        data = BlacklistPassingRepository().get_by_id(id=blacklist_passing_id)
        pass_id = data["pass_id"]
        vehicle_data = OracleVehiclePassRepository().get_playback_data_by_pass_id(
            pass_id=pass_id
        )

        camera_code = vehicle_data[0]['camera_code']
        pass_time = datetime.datetime.strptime(vehicle_data[0]['pass_time'], '%Y-%m-%d %H:%M:%S')

        start_time = pass_time - datetime.timedelta(seconds=7)
        end_time = pass_time + datetime.timedelta(seconds=10)

        start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%S') + '.000+07:00'
        end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%S') + '.000+07:00'

        rtsp_url = TrafficViewLogic().get_rstp_playback(
            camera_code=camera_code, start_time=start_time_str, end_time=end_time_str
        )

        if rtsp_url:

            return StreamingHttpResponse(gen(rtsp_url),content_type="multipart/x-mixed-replace;boundary=frame")
        else:

            no_signal_img = open(r'C:\Users\Administrator\Desktop\workspace\bma-backend\src\api\images\No signal.png', 'rb')
            response = FileResponse(no_signal_img)

            return response

    else:
        response = JsonResponse({
            'status_code': 400,
            'message': 'id field required' 
        }, status=400)

        return response

    