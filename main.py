import asyncio
import os

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write("<h1>Hello world</h1>")


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    port = int(os.getenv("PORT", "8000"))
    app.listen(port, address="0.0.0.0")
    print(f"listening on http://0.0.0.0:{port}", flush=True)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
