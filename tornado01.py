# coding:utf-8

import tornado.web  # 框架
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    # 主页处理类
    def get(self):  # 重写基类定义好的方法
        # get请求方式
        self.write("hello tornado")


if __name__ == '__main__':
    # 路由设置 路由映射
    app = tornado.web.Application([(r"/", IndexHandler)])
    # 监听端口 1实例化一个服务器实例,绑定到指定端口,并没有监听
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()  # 单例模式 start()开启监听
