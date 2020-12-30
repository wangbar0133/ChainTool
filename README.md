# ChainTool

## 安装

```
git clone https://github.com/wangbar0133/ChainTool.git
```

## 安装依赖

   ```
pip install -r requirements.txt
   ```

## 负责人对象

```
from responsible import Account

res = Account()  # 新建一个负责人
```

### 属性

| userName      | 用户名                |
| ------------- | --------------------- |
| signingKey    | 签名密钥              |
| VerifiyingKey | 验证密钥（25519对象） |
| SigningKey    | 签名密钥（25519对象） |

## Block对象

```
from chain import Block

newBlock = Block().CreateNewBlock(position=position, status=status, responsible=res, BlockChain=BlockChain)
```

### 属性

| BlockJson                                                    | 块的json对象                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| CreateNewBlock(self, position, status, responsible, BlockChain): | 函数，返回新块，传入position, status, responsible, BlockChain（BlockChain对象） |
| PrintBlock                                                   | 函数，打印这个块                                             |

### BlockJson

```
{
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

```



## BlockChain对象

```
from chain import BlockChain

newBlockChain = BlockChain()
```

### 属性

| AddBlockToChain | 把块对象加入到链中     |
| --------------- | ---------------------- |
| PrintBlockChain | 打印整个链             |
| GetChain        | 函数，返回整个链列表   |
| ToFile          | 函数，保存到文件       |
| FileTo          | 函数，从文件加载到对象 |

