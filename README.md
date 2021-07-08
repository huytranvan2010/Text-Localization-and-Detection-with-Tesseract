# Text-Localization-and-Detection-with-Tesseract
Hướng dẫn chạy
```python
python text_localization.py --image image2.png
```
Trong bài trước chúng ta đã tìm hiểu sơ bộ về [Tessract](https://huytranvan2010.github.io/Tesseract-OCR-Guide/). Trong bài này cùng tìm hiểu cách thực hiện text localization và text detection với Tesseract. Thực chất nội dung này có thể bị trùng lặp với bài trước. Tuy nhiên ở đây chúng ta sẽ đi sâu hơn một chút.

Khi test có thể thay đổi `min_confidence` để có kết quả tốt nhất. Ví dụ khi test với `image2` nhận diện lá táo thành số 4.
```python
Confidence: 34
Text: 4

Confidence: 96
Text: Apple

Confidence: 96
Text: Support

Confidence: 96
Text: 1-800-275-2273
```
Có thể tăng confidence lên để giải quyết việc này.

Thực chất Tesseract đã bao gồm tất quả các bước trong OCR nên việc phát hiện và định vị text là điều đương nhiên. Như vậy chúng ta đã tìm hiểu các định vị text thông qua Tesseract.
