import cv2
from django.http import StreamingHttpResponse, FileResponse

from api.validators.session import SessionValidator
from api.validators.feature import FeatureValidator
from api.validators.trafficView import TrafficViewValidator

from api.repositories.oracleCheckpoint import OracleCheckpointRepository
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
    FeatureValidator().validate_traffic_view(
        user_id=payloads['user_id']
    )

    checkpoint_id, camera_code, start_time, end_time = TrafficViewValidator().validate_request_playback(
        params=request.GET
    )

    rtsp_url, camera_code = TrafficViewLogic().get_playback_view(
        checkpoint_id=checkpoint_id, camera_code=camera_code,
        start_time=start_time, end_time=end_time
    )

    if rtsp_url:

        return StreamingHttpResponse(gen(rtsp_url),content_type="multipart/x-mixed-replace;boundary=frame")
    else:

        no_signal_img = open(r'C:\Users\Administrator\Desktop\workspace\bma-backend\src\api\images\No signal.png', 'rb')
        response = FileResponse(no_signal_img)

        return response
