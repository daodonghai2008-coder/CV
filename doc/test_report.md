<<<<<<< HEAD
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
=======
# Báo cáo kiểm thử

## Thông tin chung

- **Dự án:** Portfolio CV - Đào Đông Hải
- **Phiên bản:** v1.0
- **Ngày kiểm thử:** 27/10/2026
- **Phạm vi:** Kiểm tra trang tĩnh, giao diện responsive, tài nguyên, mã nguồn và khả năng phục vụ trên môi trường cục bộ.
- **Kết luận:** Đạt một phần. Trang hiển thị và phục vụ được trong môi trường đã thử; vẫn còn liên kết dự án mẫu và chưa xác minh Docker hoặc môi trường triển khai production.

## Môi trường và phương pháp

- **Hệ điều hành:** Windows
- **Trình duyệt:** Google Chrome (headless)
- **Viewport giao diện:** 390 × 844 px (mobile) và 1440 × 1000 px (desktop)
- **Máy chủ thử nghiệm:** Python HTTP server, cổng 8765
- **Công cụ:** Playwright điều khiển Chrome; kiểm tra phản hồi HTTP và rà soát HTML/CSS.
- Dự án không có bộ kiểm thử tự động, cấu hình lint/build hay mã JavaScript ứng dụng; vì vậy các kiểm tra chức năng được thực hiện trên trang đang chạy và bằng rà soát mã nguồn.

## Tổng hợp kết quả

| Tiêu chí | Kết quả | Tóm tắt |
|---|---|---|
| Tính đúng đắn | Đạt một phần | Trang, các mục nội dung và tài nguyên tải được; bốn liên kết chi tiết dự án vẫn là `#`. |
| UI/UX | Đạt | Đã kiểm tra hai kích thước viewport; bố cục chuyển cột phù hợp và không tràn ngang. |
| Khả năng vận hành - xử lý lỗi | Đạt một phần | Máy chủ tĩnh trả nội dung bình thường và trả 404 cho đường dẫn không tồn tại; không có luồng ứng dụng động để kiểm tra xử lý lỗi. |
| Bảo mật | Đạt một phần | Bề mặt tấn công phía trình duyệt thấp; chưa cấu hình hoặc kiểm tra các header bảo mật và chưa thực hiện kiểm thử xâm nhập. |
| Chất lượng mã nguồn | Đạt một phần | HTML/CSS có cấu trúc responsive và các tài nguyên tải được; chưa có lint, build hoặc test suite để kiểm tra tự động. |
| Khả năng triển khai | Đạt một phần | Đã chạy trang tĩnh qua HTTP trên Windows; chưa xác minh Docker, macOS, Linux hoặc máy chủ production. |

## 1. Tính đúng đắn

**Kết quả: Đạt một phần**

- Trang trả HTTP 200; tiêu đề, phần giới thiệu, kỹ năng, dự án và liên hệ xuất hiện trong trang.
- Các liên kết điều hướng nội bộ có mục tiêu tương ứng (`about`, `skills`, `projects`, `contact`).
- Ảnh đại diện và bốn ảnh minh họa dự án đều tải thành công trong trình duyệt.
- Tệp HTML, CSS và ảnh WebP trả HTTP 200 từ máy chủ thử nghiệm.
- Đường dẫn tệp không tồn tại trả HTTP 404.
- **Tồn tại:** Cả bốn liên kết “Xem chi tiết” đều đang trỏ tới `#`, chưa mở trang dự án hoặc bản demo.

**Minh chứng giao diện:** [Ảnh desktop](../docs/screenshots/desktop.png), [ảnh mobile](../docs/screenshots/mobile.png).

## 2. UI/UX

**Kết quả: Đạt**

- Đã xem trực tiếp trang ở viewport 390 px và 1440 px.
- Ở 390 px, lưới dự án hiển thị một cột; ở 1440 px, hiển thị ba cột.
- Chiều rộng tài liệu bằng chiều rộng viewport trong cả hai lần thử; không phát hiện tràn ngang.
- Điều hướng, nội dung, ảnh đại diện và các thẻ dự án hiển thị trong ảnh chụp toàn trang.
- CSS có trạng thái focus nhìn thấy được và hỗ trợ `prefers-reduced-motion`.
- **Giới hạn kiểm tra:** Chưa đánh giá khả năng tiếp cận bằng công cụ chuyên dụng hoặc thử nghiệm người dùng trên nhiều trình duyệt/thiết bị thực.

**Minh chứng:** [Ảnh desktop](../docs/screenshots/desktop.png) · [Ảnh mobile](../docs/screenshots/mobile.png).

## 3. Khả năng vận hành - xử lý lỗi

**Kết quả: Đạt một phần**

- Máy chủ HTTP cục bộ phục vụ trang và các tài nguyên cần thiết thành công.
- Trang chạy trong trình duyệt không phát sinh lỗi JavaScript; các ảnh đều tải thành công.
- Khi yêu cầu một đường dẫn tĩnh không tồn tại, máy chủ trả HTTP 404 thay vì báo thành công.
- Đây là website tĩnh, không có API, backend, cơ sở dữ liệu hoặc biểu mẫu gửi dữ liệu; do đó không có luồng xử lý lỗi nghiệp vụ, lỗi mạng API hay xác thực để kiểm tra.

## 4. Bảo mật

**Kết quả: Đạt một phần**

- Rà soát mã nguồn không thấy thẻ `<script>`, biểu mẫu nhập liệu hoặc stylesheet bên thứ ba; CSS và ảnh được tham chiếu từ dự án.
- Các liên kết ngoài mở tab mới có `rel="noopener noreferrer"`.
- Không phát hiện khóa API hoặc cấu hình bí mật trong các tệp được kiểm tra.
- **Giới hạn:** Chưa cấu hình/kiểm chứng CSP, HSTS, HTTPS hoặc các HTTP security headers vì dự án không kèm cấu hình máy chủ production. Đây là rà soát cơ bản, không phải kiểm thử xâm nhập hay đánh giá bảo mật toàn diện.

## 5. Chất lượng mã nguồn

**Kết quả: Đạt một phần**

- Nội dung được tách thành HTML và CSS; CSS dùng Flexbox, Grid, biến giao diện và media queries cho responsive.
- Các ảnh có văn bản thay thế; cấu trúc có tiêu đề, điều hướng và các phần nội dung riêng.
- Các kiểm tra trình duyệt xác nhận đủ bốn mục nội dung chính và năm ảnh hiển thị thành công.
- **Giới hạn:** Repository chưa có test suite, linter, formatter hoặc quy trình build tự động; chưa có kết quả kiểm thử tự động để xác nhận chất lượng toàn diện.

## 6. Khả năng triển khai

**Kết quả: Đạt một phần**

- Đã chạy thành công bằng Python HTTP server trên Windows và truy cập trang tại `http://localhost:8765/`.
- Vì đây là website tĩnh, có thể phục vụ thư mục nội dung bằng máy chủ web tĩnh phù hợp.
- **Chưa kiểm chứng:** Chạy bằng Docker, triển khai trên macOS/Linux, cấu hình tên miền/HTTPS, cache, logging và máy chủ production. Môi trường kiểm thử hiện tại không có Docker CLI.

## Ảnh minh chứng

Ảnh được chụp trực tiếp từ trang đang chạy bằng Chrome/Playwright ở ngày kiểm thử.

### Desktop — 1440 px

![Ảnh chụp trang portfolio ở desktop](../docs/screenshots/desktop.png)

### Mobile — 390 px

![Ảnh chụp trang portfolio ở mobile](../docs/screenshots/mobile.png)
>>>>>>> bfa61469310e04f8a0c97e1d90b95db514ab9f9b
