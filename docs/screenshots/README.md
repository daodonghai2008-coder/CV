# Ảnh minh chứng A2.1

Các file `desktop.png` và `mobile.png` có sẵn trong gói ban đầu là ảnh cũ (1440px và 390px), chỉ dùng tham khảo, không đại diện cho kiểm thử tại breakpoint yêu cầu.

Để tạo ảnh minh chứng TRƯỚC/SAU đúng kích thước, chạy từ thư mục gốc dự án:

```bash
pip install playwright
python -m playwright install chromium
python tools/capture_responsive.py
```

Script so sánh bản gốc được lưu nguyên trạng tại `docs/baseline-before/` với website đã sửa ở thư mục gốc. Ảnh được lưu thành `before-mobile-360.png`, `before-tablet-768.png`, `before-desktop-1280.png` và `mobile-360.png`, `tablet-768.png`, `desktop-1280.png`. Kết quả đo nằm trong `viewport-results.json`. Mở và kiểm tra ảnh trước khi đưa vào báo cáo. Không đánh dấu một ca kiểm thử là PASS nếu chưa chạy thực tế.
