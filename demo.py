from responsible import Account
from chain import BlockChain
from chain import Block

if __name__ == "__main__":
    print('新建一个负责人')
    res = Account()  # 新建一个负责人
    print('name:    ' + str(res.userName))
    print('signKey:   ' + str(res.signingKey))
    input("按任意键继续...............")

    print('新建一个链')
    newBlockChain = BlockChain()  # 新建一个链

    print('已建立好')

    input("按任意键继续...............")

    print('新建一个块, 并将信息输入')
    newBlock = Block().CreateNewBlock(position='None', status='None', responsible=res, BlockChain=None)
    # 因为是创世块，所以BlockChain=False

    input("按任意键继续...............")
    print('将新生成的块加到新生成的链里')
    newBlockChain.AddBlockToChain(newBlock=newBlock)

    input("按任意键继续...............")
    print('重复一次。。。。')
    newBlock2 = Block().CreateNewBlock(position='None', status='None', responsible=res, BlockChain=newBlockChain)
    # 不是创世块，所以BlockChain=True
    newBlockChain.AddBlockToChain(newBlock=newBlock2)

    input("按任意键继续...............")
    print('打印整个链')
    newBlockChain.PrintBlockChain()

    print("保存")
    newBlockChain.ToFile()
    print('保存完成')

    input("按任意键继续...............")
    print('\n')
    print("加载")
    newBlockChain2 = BlockChain()
    newBlockChain2.FileTo()
    newBlockChain2.PrintBlockChain()
    print('已加载')

