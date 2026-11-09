# Nhật ký thay đổi

## v1.0 — 27/10/2026

### Chức năng mới

- Tạo trang portfolio/CV cá nhân giới thiệu Đào Đông Hải.
- Hiển thị phần giới thiệu, kỹ năng, dự án tiêu biểu và thông tin liên hệ.
- Thiết kế giao diện responsive cho điện thoại, máy tính bảng và máy tính để bàn.
- Hỗ trợ chạy trực tiếp trên trình duyệt, qua máy chủ web tĩnh hoặc Docker với Nginx.
- Bổ sung README tiếng Việt với hướng dẫn cài đặt và chạy trên Windows, macOS, Linux và Docker.

### Lỗi đã sửa

- Đây là bản phát hành đầu tiên; chưa có lỗi từ phiên bản trước được ghi nhận.

### Hạn chế còn tồn tại

- Các dự án hiển thị trên trang hiện là nội dung giới thiệu/minh họa; chưa tích hợp chức năng ứng dụng thực tế.
- Liên kết “Xem chi tiết” của các dự án chưa trỏ đến trang hoặc bản demo cụ thể.
- Trang chưa có backend, cơ sở dữ liệu hoặc biểu mẫu gửi liên hệ.
## 2026-11-03 – Mint Doodle visual refresh
- Đổi design tokens sang #DDFFF7 / #62C4C3.
- Thêm doodle background, hover/reveal animations và 4 meme project images.
- Giữ nguyên ảnh đại diện và bổ sung responsive guard cho màn hình 360px.


## 2026-11-04 — Hoàn thiện A2.1
- Sửa cấu trúc form góp ý, bổ sung label, autocomplete và trạng thái focus bàn phím.
- Đồng bộ project grid: 1 cột mobile, 2 cột tablet, 3 cột desktop từ 1280px.
- Bỏ overflow-x hidden ở body để không che khuất lỗi tràn ngang trong quá trình kiểm thử.
- Đồng bộ README, wireframe desktop, báo cáo DOCX, ma trận kiểm thử và bảng truy vết.
- Bổ sung script Playwright để người học chụp và đo ba viewport trên máy cá nhân.
