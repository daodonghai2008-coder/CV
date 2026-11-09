# Báo cáo kiểm thử A2.1 — Portfolio CV

## 1. Thông tin

- **Chủ sở hữu:** Đào Đông Hải
- **Phiên bản:** Mint Doodle — mã nguồn đã chỉnh sửa
- **Phạm vi:** HTML5 semantic, CSS3, Flexbox/Grid, responsive, điều hướng, form và tài liệu minh chứng.
- **Phương pháp:** Rà soát mã nguồn và đối chiếu tiêu chí; kiểm thử trình duyệt trực quan phải được thực hiện trên máy người học.

## 2. Các lỗi đã phát hiện và sửa trong lần hoàn thiện này

| STT | Vấn đề trước sửa | Cách sửa | Trạng thái mã nguồn |
|---|---|---|---|
| 1 | Form góp ý thiếu thẻ đóng `</form>` và cấu trúc đóng container chưa rõ | Đóng form và container đúng thứ tự | Đã sửa |
| 2 | Các trường form chỉ có placeholder, chưa có label liên kết | Bổ sung label, `for`/`id`, autocomplete và aria-label | Đã sửa |
| 3 | Focus input bị tắt outline, làm giảm khả năng nhận biết khi bàn phím | Dùng `:focus-visible` với outline rõ | Đã sửa |
| 4 | Grid desktop mới có 2 cột, không khớp AC-07 và wireframe | Bổ sung 3 cột từ 1280px | Đã sửa |
| 5 | README và tài liệu phụ mô tả điều hướng/breakpoint không đồng nhất | Đồng bộ 5 mục nav và 1/2/3 cột | Đã sửa |

## 3. Ma trận kiểm thử

| Mã | Kích thước | Kỳ vọng | Kết quả hiện tại |
|---|---:|---|---|
| VP-01 | 360 × 800 | Project 1 cột; không cuộn ngang | CSS/HTML đã rà soát; cần xác nhận bằng trình duyệt trên máy người học |
| VP-02 | 768 × 1024 | Hero 2 cột; project 2 cột | CSS đã rà soát; cần xác nhận bằng trình duyệt trên máy người học |
| VP-03 | 1280 × 900 | Project 3 cột; container max 1120px | CSS đã rà soát; cần xác nhận bằng trình duyệt trên máy người học |
| NAV-01 | Mọi kích thước | 5 liên kết nav tới đúng ID | Đã đối chiếu href/ID trong HTML; cần bấm thử trực tiếp |
| FORM-01 | Mọi kích thước | Label, trường bắt buộc, form đóng hợp lệ | Đã rà soát HTML; cần gửi thử endpoint Formspree |
| A11Y-01 | Mọi kích thước | Ảnh alt, focus bàn phím, skip-link | Đã rà soát mã; cần thao tác bàn phím trực tiếp |

## 4. Giới hạn kiểm thử

Trong môi trường xử lý gói bài hiện tại, thao tác khởi chạy/điều khiển Chromium và truy cập localhost bị chặn bởi chính sách môi trường. Vì vậy báo cáo này **không giả định** đã đo `scrollWidth`, chụp ảnh ở ba viewport hoặc gửi form thành công. Hai ảnh desktop/mobile cũ trong ZIP là 1440px và 390px, chỉ là minh chứng tham khảo và không được gắn nhãn là ảnh kiểm thử 360/768/1280px.

## 5. Ảnh minh chứng cần bổ sung trên máy người học

- `docs/screenshots/before-mobile-360.png` và `mobile-360.png` — trước/sau tại 360 × 800 CSS px.
- `docs/screenshots/before-tablet-768.png` và `tablet-768.png` — trước/sau tại 768 × 1024 CSS px.
- `docs/screenshots/before-desktop-1280.png` và `desktop-1280.png` — trước/sau tại 1280 × 900 CSS px.
- `docs/screenshots/viewport-results.json` — số liệu đo tự động tương ứng.

Nếu có lỗi được phát hiện trong lúc kiểm thử, chụp thêm ảnh `*-before.png`, sửa lỗi, rồi chụp `*-after.png`; ghi rõ hiện tượng và cách khắc phục. Không dựng ảnh lỗi giả để thay cho ảnh trước sửa thực tế.

## 6. Kết luận

Mã nguồn đã được chỉnh sửa để khớp yêu cầu cấu trúc A2.1: HTML5 semantic, design tokens, Box Model, Flexbox, CSS Grid và ba breakpoint 360/768/1280. Hồ sơ wireframe, truy vết và smoke test đã được đồng bộ. Phần còn cần xác nhận thủ công trước khi nộp là kiểm thử trực quan trên trình duyệt, đo không tràn ngang tại 360px, kiểm tra form Formspree và lưu ảnh minh chứng đúng ba viewport.
