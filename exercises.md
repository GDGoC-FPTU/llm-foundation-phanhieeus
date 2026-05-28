# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> *Khi temperature càng tăng lên thì câu trả lời có vẻ thêm tính sáng tạo (cùng với đó là sự sai sự thật sảy ra), nghe thì có vẻ hợp lý nhưng hoàn toàn không đúng*

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> *Để temperature thấp vừa phải (<0.5), cân bằng giữa cảm giác trò chuyện tự nhiên, đồng thời không để câu trả lời quá xa rời sự thật.*

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> *Nhìn chung, tính trung bình bằng cách (in+out)/2 thì giá mỗi token của GPT-4o gấp khoảng 12 lần giá của mỗi token GPT-4o-mini. Thực tế cần xét đến domain hướng đến có khả năng tiêu thụ input token so với output token thế nào đối với mỗi model.*

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> *Những nhiệm vụ phức tạp hơn, khi đã thử nghiệm với GPT-4o-mini mà không đáp ứng được nhu cầu khách hàng, thì GPT-4o là lựa chọn xứng đáng để thử. Và ngược lại, khi GPT-4o-mini đáp ứng được nhu cầu thực tiễn thì nó sẽ trở thành lựa chọn tốt hơn*

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> *Streaming quan trọng khi xây dựng ứng dụng có tính chất trò chuyện như chatbot, chăm sóc khách hàng, tạo cho khách hàng cảm giác đang trò chuyện với người thật. Các sản phẩm hiện nay như ChatGPT,... đều streaming để mang lại trải nghiệm tốt hơn. Khách hàng có thể chưa cần biết câu trả lời có tốt hay không, nhưng để họ đợi 5-10 giây rồi đột ngột hiện ra toàn bộ câu trả lời sẽ dễ làm họ thiếu kiên nhẫn và rời đi. Tuy nhiên có 1 số trường hợp non-streaming có thể phù hợp hơn, có thể là các khách hàng doanh nghiệp, khi họ cần sinh ra dữ liệu để cho quá trình SFT, RLHF thì cũng chả cần streaming làm gì.*


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
