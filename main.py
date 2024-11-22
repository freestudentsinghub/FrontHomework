from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Настройки запуска
HOST_NAME = "localhost"
SERVER_PORT = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        path = self.get_path()
        print(f"Запрос к: {path}")
        try:
            with open(path, "r", encoding="utf-8") as file:
                page_content = file.read()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")
        else:
            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "text.html")  # Отправка типа данных
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа

    def get_path(self) -> str:
        if self.path == "/":
            return "contacts.html"
        return self.path[1:]

    def get_content_type(self) -> str:
        if self.path.endswith(".css"):
            return "text/css"
        elif self.path.endswith(".js"):
            return "text/javascript"
        else:
            return "text/html"

if __name__ == "__main__":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    print(f"Сервер запущен по адресу http://{HOST_NAME}:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
