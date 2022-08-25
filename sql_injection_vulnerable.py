import http.server
import socketserver
import sqlite3 as db

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)

    #conncect to databse
    conn = db.connect("login.db")
    cursor = conn.cursor()

    httpd.serve_forever()