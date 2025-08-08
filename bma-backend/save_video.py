# import subprocess

# def download_hls_stream(url, output_dir):
#     # Use the hlsdl command-line tool to download the HLS stream
#     cmd = ["hlsdl", url, "-o", output_dir]

#     try:
#         subprocess.run(cmd, check=True)
#         print("HLS stream downloaded successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error downloading HLS stream: {e}")

# if __name__ == "__main__":
#     hls_url  = "http://10.129.90.105/HLS/channel/101/startTime/20230906T100000/endTime/20230906T100200/playBack.m3u8"  # Replace with the actual video URL
#     output_directory  = "C:\\Users\\Administrator\\Desktop\\BMA\\bma-backend\\video-playback"  # Replace with the desired save path

#     download_hls_stream(hls_url, output_directory)

import subprocess
import datetime
import time

def download_hls_video(hls_url, output_file, duration_seconds):
    # Generate a unique filename based on the current timestamp
    output_file = f"{output_file}_{int(time.time())}.mp4"

    # Use ffmpeg to download and save the video
    subprocess.run([
        'ffmpeg', '-i', hls_url,
        '-t', str(duration_seconds),  # Set the duration in seconds
        '-c', 'copy',  # Copy the streams without re-encoding
        output_file
    ])

    print(f"Video saved to {output_file}")

if __name__ == "__main__":
    hls_url = "http://10.115.90.5/HLS/channel/101/startTime/20230906T100000/endTime/20231106T090010/playBack.m3u8"
    output_file = "output_video"
    duration_seconds = 10

    download_hls_video(hls_url, output_file, duration_seconds)