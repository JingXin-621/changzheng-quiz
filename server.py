# -*- coding: utf-8 -*-
"""
长征里程挑战 — 本地服务器
一键启动，电脑和手机都能访问（需在同一 Wi-Fi 下）

用法：python server.py
"""

import http.server
import socket
import os
import sys
import webbrowser

PORT = 8000

def get_local_ip():
    """获取本机局域网 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("114.114.114.114", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def safe_print(text):
    """安全打印，处理 Windows GBK 编码问题"""
    try:
        print(text)
    except UnicodeEncodeError:
        # 移除无法编码的字符后打印
        print(text.encode('gbk', errors='replace').decode('gbk', errors='replace'))

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    local_ip = get_local_ip()

    safe_print("=" * 56)
    safe_print("  [长征里程挑战] 我的长征路")
    safe_print("=" * 56)
    safe_print("")
    safe_print("  服务已启动！用浏览器打开以下地址：")
    safe_print("")
    safe_print("  [电脑] 本机访问：")
    safe_print(f"     http://localhost:{PORT}")
    safe_print("")
    safe_print("  [手机] 手机访问（需在同一 Wi-Fi）：")
    safe_print(f"     http://{local_ip}:{PORT}")
    safe_print("")
    safe_print("  按 Ctrl+C 停止服务")
    safe_print("=" * 56)

    # 自动打开浏览器
    webbrowser.open(f"http://localhost:{PORT}")

    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n服务已停止。")

if __name__ == "__main__":
    main()
