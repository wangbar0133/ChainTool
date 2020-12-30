import time
from bin import Encrypt
from bin import ListToStr
import os
import json


class Block():

    def __init__(self):
        '''
        初始化Block对象
        '''
        self.BlockJson = {
                "headers": {    # 块头
                    "prBlockHash": "",   # 前一块的hash
                    "timeStamp": "",     # 当前时间戳
                    "mainChain": 'True'  # 是否主链
                },

                "body": {       # 块主题
                    "details": {
                        "position": "",  # 当前位置
                        "timeStamp": "",  # 当前时间戳
                        "status": ""     # 当前状态
                    },
                    "responsibleName": "",  # 负责人名字 （公钥）
                    "responsibleSign": "",  # 负责人对details的签名
                }
                ,
                "blockHash": "",  # body 的hash
            }

        self.status = ''
        #TODO: 状态需要定义

    def CreateNewBlock(self, position, status, responsible, BlockChain):
        '''

        :param position: 当前位置
        :param status: 货物状态
        :param responsible: 负责人对象
        :param BlockChain: 区块链对象
        :return: 返回一个block对象
        '''
        if BlockChain == None:
            pass
        else:
            self.BlockJson['headers']['prBlockHash'] = BlockChain.chain[-1]['blockHash']
        self.BlockJson["headers"]["timeStamp"] = time.asctime(time.localtime(time.time()))
        self.BlockJson["body"]["details"]["status"] = status
        self.BlockJson["body"]["details"]["position"] = position
        self.BlockJson["body"]["responsibleName"] = responsible.userName
        detailsHash = Encrypt().HashEncrypt(data_str=str(self.BlockJson['body']["details"]).encode("utf-8"))
        self.BlockJson["body"]["responsibleSign"] = Encrypt().Sign(detailsHash, responsible)
        self.BlockJson['blockHash'] = Encrypt().HashEncrypt(str(self.BlockJson['body']).encode("utf-8"))
        return self.BlockJson

    def PrintBlock(self):
        '''

        :return:  打印当前区块
        '''
        print(self.BlockJson)

class BlockChain():

    def __init__(self):
        self.chain = []
        self.filename = os.getcwd() + '/' + 'blockchain.json'  # 将区块链存到这个json文件中
        '''
        初始化区块链对象
        '''

    def AddBlockToChain(self, newBlock):
        '''

        :param newBlock:Block对象
        :return: 将传入的区块连到链中
        '''
        self.chain.append(newBlock)

    def PrintBlockChain(self):
        '''

        :return: 打印整个链
        '''
        for block in self.chain:
            print(block)

    def GetChain(self):
        '''

        :return:返回整个链list
        '''
        return self.chain

    def ToFile(self):
        with open(self.filename, 'w') as file_obj:
            jsonStr = json.loads(ListToStr(self.chain))
            json.dump(jsonStr, file_obj)
        file_obj.close()

    def FileTo(self):
        '''

        :return:将文件中的区块链加载到区块链对象
        '''
        with open(self.filename) as file_obj:
            self.chain = json.load(file_obj)

    def ToFile(self):
        '''

        :return:将区块链保存到json文件
        '''
        with open(self.filename, 'w') as file_obj:
            jsonStr = json.loads(ListToStr(self.chain))
            json.dump(jsonStr, file_obj)
        file_obj.close()
