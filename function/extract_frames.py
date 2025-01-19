import cv2
import os

def extract_frames_from_video(video_path, output_dir, frame_interval=30):
    """
    Trích xuất frame từ video.

    Args:
        video_path (str): Đường dẫn tới video cần xử lý.
        output_dir (str): Thư mục lưu frame.
        frame_interval (int): Số frame bỏ qua trước khi lưu (mặc định: 30 ~ 1s nếu video 30fps).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    count = 0
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Lưu frame sau mỗi frame_interval frame
        if count % frame_interval == 0:
            frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            print(f"Lưu frame: {frame_path}")
            frame_count += 1

        count += 1

    cap.release()
    print("Hoàn thành trích xuất frame.")

# Ví dụ chạy script
if __name__ == "__main__":
    video_path = "./data/data1.mp4"  # Đường dẫn video
    output_dir = "./frames"         # Thư mục lưu frame
    extract_frames_from_video(video_path, output_dir)
