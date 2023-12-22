from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
hostName = "localhost"
serverPort = 8080


class RequestHandler(BaseHTTPRequestHandler):

    html_file = "index.html"

    def get_html(self, filename):
        with open(filename, encoding="utf-8") as f:
            return f.read()

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.get_html(self.html_file)
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    web_server = HTTPServer((hostName, serverPort), RequestHandler)
    print("Создали сервер http://%s:%s" % (hostName, serverPort))
    try:
        print("Запускаем сервер")
        web_server.serve_forever()
        print("Запустили сервер")
    except KeyboardInterrupt:
        print("Сервер остановлен")

    web_server.server_close()
    print("Server stopped.")