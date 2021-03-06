# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
self.name为Redis中的一个key
'''

import json

import redis


class RedisClient(object):
    """
    Reids client
    """

    def __init__(self, name, host, port):
        """
        init
        :param name:
        :param host:
        :param port:
        :return:
        """
        self.name = name
        self.__conn = redis.Redis(host=host, port=port, db=0)

    def get(self):
        """
        get random result
        :return:
        """
        return self.__conn.srandmember(name=self.name)

    def put(self, value):
        """
        put an  item
        :param value:
        :return:
        """
        value = json.dump(value, ensure_ascii=False).encode('utf-8') if isinstance(value, (dict, list)) else value
        return self.__conn.sadd(self.name, value)

    def pop(self):
        """
        pop an item
        :return:
        """
        value = self.get()
        if value:
            self.__conn.spop(self.name)
        return value

    def delete(self, value):
        """
        delete an item
        :param key:
        :return:
        """
        self.__conn.srem(self.name, value)

    def getAll(self):
        return self.__conn.smembers(self.name)

    def get_status(self):
        return self.__conn.scard(self.name)

    def changeTable(self, name):
        self.name = name


if __name__ == '__main__':
    redis_con = RedisClient('proxy', 'localhost', 6379)
    # redis_con.put('abc')
    # redis_con.put('123')
    # redis_con.put('123.115.235.221:8800')
    # print redis_con.getAll()
    # redis_con.delete('abc')
    # print redis_con.getAll()
    # redis_con.pop()
    # print redis_con.getAll()
    redis_con.changeTable('raw_proxy')

    redis_con.put('132.112.43.221:8888')
    # redis_con.changeTable('proxy')
    print redis_con.get_status()
    print redis_con.getAll()