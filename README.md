# Portfolio CV - Đào Đông Hải

Trang portfolio/CV cá nhân giới thiệu Đào Đông Hải, các kỹ năng Frontend, một số dự án tiêu biểu và thông tin liên hệ. Giao diện được xây dựng theo hướng tối giản, responsive và có thể chạy trực tiếp bằng trình duyệt hoặc phục vụ bằng máy chủ web tĩnh.

## Chức năng

- Giới thiệu cá nhân và định hướng Frontend Developer.
- Hiển thị các kỹ năng: HTML5, CSS3, JavaScript, responsive design, Git/GitHub và Figma/wireframe.
- Trình bày các thẻ dự án mẫu: Landing Page, Todo List, Weather Dashboard và Blog cá nhân.
- Điều hướng đến các phần Giới thiệu, Kỹ năng, Dự án và Liên hệ.
- Bố cục thích ứng với màn hình điện thoại, máy tính bảng và máy tính để bàn.
- Cung cấp liên kết email, GitHub và LinkedIn.

> Các dự án trong portfolio hiện là nội dung giới thiệu/minh họa. Những liên kết “Xem chi tiết” đang dùng `#`; trang chưa tích hợp chức năng của các ứng dụng mẫu hoặc backend.

## Công nghệ

- HTML5: cấu trúc nội dung và ngữ nghĩa.
- CSS3: giao diện, Flexbox, CSS Grid, custom properties và media queries theo hướng mobile-first.
- SVG nhúng và ảnh WebP: hình minh họa dự án và ảnh đại diện.
- Nginx (tùy chọn): phục vụ trang tĩnh trong Docker.

Dự án không cần Node.js, npm, cơ sở dữ liệu hay bước biên dịch.

## Yêu cầu môi trường

### Để xem trang

- Trình duyệt hiện đại như Chrome, Firefox, Edge hoặc Safari.
- Không cần cài thêm thư viện hay công cụ phát triển.

### Để chạy máy chủ cục bộ

- Python 3 (tùy chọn; chỉ cần nếu muốn mở trang qua máy chủ HTTP thay vì mở trực tiếp `index.html`).

### Để chạy bằng Docker

- Docker Desktop trên Windows/macOS hoặc Docker Engine trên Linux.
- Docker CLI có thể truy cập từ terminal.

## Cài đặt

Lấy mã nguồn bằng Git:

```bash
git clone https://github.com/daodonghai2008-coder/CV.git
cd CV
```

Hoặc tải mã nguồn về và giải nén. Đảm bảo cấu trúc thư mục tối thiểu như sau:

```text
CV/
├── index.html
├── assets/
│   ├── css/
│   │   └── styles.css
│   └── img/
│       └── IMG_20260417_215934.webp
└── README.md
```

## Cấu hình và tùy chỉnh

Trang không dùng tệp cấu hình môi trường (`.env`) và không yêu cầu thiết lập khóa API.

- Sửa tên, mô tả, kỹ năng, dự án và thông tin liên hệ trong [`index.html`](./index.html).
- Sửa màu sắc, kiểu chữ, khoảng cách và bố cục trong [`assets/css/styles.css`](./assets/css/styles.css). Các biến giao diện nằm trong khối `:root` ở đầu tệp.
- Thay ảnh đại diện bằng cách cập nhật đường dẫn ảnh trong `index.html`; đặt ảnh mới trong `assets/img/` để dùng đường dẫn tương đối.
- Thay các liên kết `href="#"` ở thẻ dự án bằng URL dự án thật khi có.

## Chạy thử

### Mở trực tiếp

Mở tệp `index.html` bằng trình duyệt. Cách này không cần cài thêm phần mềm, phù hợp để xem nhanh giao diện.

### Chạy máy chủ cục bộ

Chạy lệnh tại thư mục gốc của dự án, sau đó truy cập <http://localhost:8000>.

**Windows (PowerShell):**

```powershell
py -m http.server 8000
```

Nếu lệnh `py` không có nhưng đã cài Python:

```powershell
python -m http.server 8000
```

**macOS:**

```bash
python3 -m http.server 8000
```

**Linux:**

```bash
python3 -m http.server 8000
```

Nhấn `Ctrl+C` trong terminal để dừng máy chủ. Nếu cổng `8000` đang được sử dụng, thay `8000` trong lệnh bằng một cổng khác và mở đúng cổng đó trên trình duyệt.

## Chạy bằng Docker

Các lệnh sau chạy Nginx trong container và mount chỉ `index.html` cùng thư mục `assets` ở chế độ chỉ đọc; không cần tạo Dockerfile hoặc cài dependency của dự án. Chạy lệnh từ thư mục gốc `CV`.

**Windows (PowerShell, Docker Desktop đang chạy):**

```powershell
docker run --rm --name cv-portfolio -p 8080:80 `
  --mount "type=bind,source=$($PWD.Path)\index.html,target=/usr/share/nginx/html/index.html,readonly" `
  --mount "type=bind,source=$($PWD.Path)\assets,target=/usr/share/nginx/html/assets,readonly" `
  nginx:alpine
```

**macOS hoặc Linux:**

```bash
docker run --rm --name cv-portfolio -p 8080:80 \
  --mount "type=bind,source=$(pwd)/index.html,target=/usr/share/nginx/html/index.html,readonly" \
  --mount "type=bind,source=$(pwd)/assets,target=/usr/share/nginx/html/assets,readonly" \
  nginx:alpine
```

Mở <http://localhost:8080> để xem trang. Container chạy ở foreground; nhấn `Ctrl+C` để dừng. Tùy chọn `--rm` tự xóa container sau khi dừng, còn ảnh `nginx:alpine` được Docker tải về khi chạy lần đầu.

## Cấu trúc dự án

```text
.
├── index.html                 # Nội dung portfolio
├── assets/
│   ├── css/
│   │   └── styles.css         # Toàn bộ giao diện và responsive
│   └── img/
│       └── IMG_20260417_215934.webp
└── README.md
```

## Thông tin liên hệ

- **Tên:** Đào Đông Hải
- **Email:** [daodonghai2008@gmail.com](mailto:daodonghai2008@gmail.com)
- **GitHub:** [daodonghai2008-coder](https://github.com/daodonghai2008-coder)
- **LinkedIn:** [Hải Đào Đông](https://www.linkedin.com/in/h%E1%BA%A3i-%C4%91%C3%A0o-%C4%91%C3%B4ng-53a848441/)