import base64
import tempfile
import os
from typing import List
import cv2
import numpy as np
import subprocess


def encode_image(image_path: str) -> str:
    """
    Encode a local image file to base64 string.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def extract_audio(video_path: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        audio_path = temp_audio.name

    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-i",
            video_path,
            "-q:a",
            "0",
            "-map",
            "a",
            audio_path,
            "-y",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    print(f"Extracted audio to {audio_path}")
    return audio_path


def sample_frames(video_path: str, max_frames: int = 10) -> List[dict]:
    """
    Sample frames from video, evenly distributed across the timeline.
    Always includes the first and last frames.
    Converts frames to base64 format.
    """
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_count <= 0:
        print(f"Could not read frame count from video: {video_path}")
        return []

    if max_frames >= frame_count:
        frame_indices = list(range(frame_count))
    else:
        frame_indices = [0, frame_count - 1]

        if max_frames > 2:
            remaining = max_frames - 2
            step = (frame_count - 2) / (remaining + 1)

            for i in range(1, remaining + 1):
                idx = int(round(i * step))
                if 0 < idx < frame_count - 1:
                    frame_indices.append(idx)

            frame_indices.sort()

    frames = []
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        success, frame = cap.read()
        if success:
            _, buffer = cv2.imencode(".jpg", frame)
            frames.append(buffer.tobytes())
        else:
            print(f"Failed to read frame {idx} from {video_path}")

    cap.release()

    encoded_frames = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64.b64encode(frame_bytes).decode('utf-8')}"
            },
        }
        for frame_bytes in frames
    ]

    print(f"Extracted {len(encoded_frames)} frames from video: {video_path}")
    return encoded_frames
