import cv2
import os

# Ganti path_video dengan path lengkap video .avi yang ingin diolah
path_video = 'Database/Data 2/Video/12.avi'

# Ganti path_output dengan folder tempat Anda ingin menyimpan setiap frame
path_output = 'Database/Data 2/Frame'

nama_file = os.path.basename(path_video)

# Membuat folder output jika belum ada
if not os.path.exists(path_output):
    os.makedirs(path_output)

# Membaca video
cap = cv2.VideoCapture(path_video)

# Menghitung jumlah frame dalam video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop untuk membaca setiap frame dan menyimpannya sebagai gambar
for frame_num in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break
    
    # Simpan frame sebagai gambar
    frame_filename = f'{nama_file}-{frame_num:03d}.png'  # Format nama file
    frame_path = os.path.join(path_output, frame_filename)
    cv2.imwrite(frame_path, frame)
    
    print(f"Frame {nama_file}-{frame_num} tersimpan")

# Tutup video
cap.release()
cv2.destroyAllWindows()

