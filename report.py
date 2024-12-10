from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas("test_report.pdf", pagesize=letter)
    width, height = letter

    c.drawString(100, height - 50, "Отчет по тестам API")
    
    # Код тестов
    c.drawString(100, height - 100, "Код тестов:")
    
    with open("test_api.py", "r") as f:
        lines = f.readlines()
        y = height - 120
        for line in lines:
            c.drawString(100, y, line.strip())
            y -= 12
            
            if y < 50:
                c.showPage()
                y = height - 50
    
    # Результаты тестов (лог консоли)
    c.showPage()
    c.drawString(100, height - 50, "Лог выполнения тестов:")
    
    # Здесь добавьте логи выполнения тестов (например, просто пример)
    log_lines = [
        "Тесты выполнены успешно.",
        "GET /items: OK",
        "POST /items: OK",
        "GET /items/0: OK",
        "PUT /items/0: OK",
        "DELETE /items/0: OK",
        "GET /items/999: Not Found",
        "Тестирование завершено."
    ]
    
    y = height - 70
    for line in log_lines:
        c.drawString(100, y, line)
        y -= 12
    
    c.save()

if __name__ == "__main__":
    create_pdf()
