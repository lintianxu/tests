import datetime
import json
import os
import random
import threading
import time
import token
from ast import Str
from cgi import print_environ
from ctypes.wintypes import FLOAT

import requests

#定义控制台窗口
if os.name == "nt":
    os.system("")
os.system("mode con cols=34 lines=7")


############################################################################################################################################################
#买入数量设定
buy_amount=('200')                                                                                                                                         ############################## 修改购入数量
BN_buy_amount=('200')                                                                                                                                      ############################## 修改购入数量

#利润设定
profit=('5.5')                                                                                                                                             ############################## 利润设定

#DEX.GURU API小数预设
#100000000=float('100000000')                                                                                                                             ############################## API 小数预设

#GAS费用预设                                                                                                                                              ############################## GAS 费用预设
gasfee_pre=('0')       

#高GAS费用预设
high_gasfee_pre=float(gasfee_pre) + 3                                                                                                                      ############################## 高GAS 费用预设

############################################################################################################################################################
#获取利润数据1
def input_func():
    global LR1
    LR1 = input('输入LR1_默认提醒利润:\n')
LR1 = float(buy_amount)+float(profit)
t = threading.Thread(target=input_func)
t.start()
t.join(3)  # 等待3秒
print("LR1是{}".format(LR1))
#获取利润数据2
def input_func():
    global LR2
    LR2 = input('\n输入LR2_高GAS提醒利润:\n')
LR2 = LR1 + float(high_gasfee_pre)
t = threading.Thread(target=input_func)
t.start()
t.join(3)  # 等待3秒
print("LR2是{}".format(LR2))
#获取利润数据3
def input_func():
    global LR3
    LR3 = input('\n输入LR3_显示提醒利润:\n')
LR3 = float(buy_amount)+1
t = threading.Thread(target=input_func)
t.start()
t.join(3)  # 等待3秒
print("LR3是{}".format(LR3))



    #跨桥费用
bridge_fee_control=('')
bridge_fee_amount=('15')

    #gas_fee 控制
gas_fee_control=('')                                                                                                                                    ##############################是否开启GAS检测
gas_fee_amount=('15')                                                                                                                                   ##############################GAS 预设

    #是否采集token价格控制
token_name_control=('')

    #微信群链接
wx_send_url=('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=99b19a36-590f-472b-a3cf-8b741316eb53')                                               ##############################微信群链接修改


#定义通用信息
    #脚本标题
title=('FTM_USTC')
    #TOKEN合约地址
        #eth
eth_token=('')                                                                                                 ##############################修改token合约地址

        #bsc
bsc_token=('')

        #fantom
fantom_token=('0x846e4d51d7e2043c1a87e0ab7490b93fb940357b')

        #polygon
polygon_token=('')
        #avax
avax_token=('')

        #optimism
optimism_token=('')

        #arbitrum
arbitrum_token=('')

        #solana
solana_token=('')

        #terra
terra_pair=('')
terra_token=('')
terra_usd=('')

        #BN
BN_token=('USTCBUSD')#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                                           ##############################修改币安交易对信息，格式为FTM_USTCBUSD

        #...


#######################################################################################################################



	#USD合约地址
        #eth
eth_usd=('0xdac17f958d2ee523a2206206994597c13d831ec7')#USD合约，无需更改 1
eth_ust=('0xa47c8bf37f92abed4a126bda807a7b7498661acd')#UST合约，无需更改

        #bsc
bsc_usd=('0x55d398326f99059ff775485246999027b3197955')#USD合约，无需更改 1

        #fantom
fantom_usd=('0x049d68029688eabf473097a2fc38ef61633a3c7a')#USD合约，无需更改 1

        #polygon 
polygon_usd=('0xc2132d05d31c914a87c6611c10748aeb04b58e8f')#USD合约，无需更改 1 

        #avax
avax_usd=('0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7')#USD合约，无需更改 1

        #optimism
optimism_usd=('0x94b008aa00579c1307b0ef2c499ad98a8ce58e58')#USD合约，无需更改 1

        #arbitrum
arbitrum_usd=('0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9')#USD合约，无需更改 1

        #solana
solana_usd=('Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB')#USD合约，无需更改 1
        #...



    #代币名称
token_name=('FTM_USTC')
eth_token_name=('eth_FTM_USTC')
bsc_token_name=('bsc_FTM_USTC')
fantom_token_name=('fantom_FTM_USTC')
polygon_token_name=('polygon_FTM_USTC')
avax_token_name=('avax_FTM_USTC')
terra_token_name=('terra_FTM_USTC')
BN_token_name=('BN_FTM_USTC')
optimism_token_name=('optimism_FTM_USTC')
arbitrum_token_name=('arbitrum_FTM_USTC')
solana_token_name=('solana_FTM_USTC')



    #采集买入URL
        #eth
eth_url=(f'https://api-trading.dex.guru/v1/market/1/price/all?buyToken={eth_token}&sellAmount={buy_amount}000000&sellToken={eth_usd}')
#eth_url=(f'https://api-trading.dex.guru/v1/market/1/price/all?buyToken={eth_token}&sellAmount={buy_amount}00000000000000000000000000&sellToken={eth_usd}')
print(eth_url)

        #bsc
bsc_url=(f'https://api-trading.dex.guru/v1/market/56/price/all?buyToken={bsc_token}&sellAmount={buy_amount}000000000000000000&sellToken={bsc_usd}')
        #fantom
#fantom_url=(f'https://api-trading.dex.guru/v1/market/250/price/all?buyToken={fantom_token}&sellAmount={buy_amount}000000&sellToken={fantom_usd}')
fantom_url=(f'https://api.1inch.io/v4.0/250/quote?fromTokenAddress={fantom_usd}&toTokenAddress={fantom_token}&amount={buy_amount}000000')

print(fantom_url)
        #polygon
polygon_url=(f'https://api-trading.dex.guru/v1/market/137/price/all?buyToken={polygon_token}&sellAmount={buy_amount}000000&sellToken={polygon_usd}')
print(polygon_url)
#polygon_url=(f'https://api-trading.dex.guru/v1/market/137/price/all?buyToken={polygon_token}&sellAmount={buy_amount}0000000000&sellToken={polygon_usd}')

        #avax
avax_url=(f'https://api-trading.dex.guru/v1/market/43114/price/all?buyToken={avax_token}&sellAmount={buy_amount}000000&sellToken={avax_usd}')
        #terra
terra_url=(f'https://fcd.terra.dev/wasm/contracts/{terra_pair}/store?query_msg=%7B%22pool%22:%7B%7D%7D')
        #cex_bn
cex_bn_url=(f'https://www.binance.com/api/v3/depth?symbol={token_name}USDT&limit=1')
        #optimism
# optimism_url=(f'https://api-trading.dex.guru/v1/market/10/price/all?buyToken={optimism_token}&sellAmount={buy_amount}&sellToken={optimism_usd}')
optimism_url=(f'https://api.1inch.io/v4.0/10/quote?fromTokenAddress={optimism_usd}&toTokenAddress={optimism_token}&amount={buy_amount}000000')
        #arbitrum
arbitrum_url=(f'https://api-trading.dex.guru/v1/market/42161/price/all?buyToken={arbitrum_token}&sellAmount={buy_amount}000000&sellToken={arbitrum_usd}')
        #solana
solana_url=(f'https://quote-api.jup.ag/v1/quote?inputMint={solana_usd}&outputMint={solana_token}&amount={buy_amount}000000&slippage=1')
        #CEX_BN
bn_url=(f'https://www.binance.com/api/v3/depth?symbol={BN_token}&limit=1')
#头文件
headers = {
    #'authority': 'developer.mozilla.org',
    #'pragma': 'no-cache',
    #'cache-control': 'no-cache',
    #'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    #'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #'accept-encoding': 'gzip, deflate, br',
    #'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
    # 'cookie': 'cookie: _fbp=fb.1.1655979021660.251281621; _tt_enable_cookie=1; _ttp=e871e846-6249-4ef6-83b9-84b9b2a6fd26; intercom-id-zgn72x6y=d9feb37d-1752-4cc0-8d5e-d4bbe41bdeb4; intercom-session-zgn72x6y=; _gid=GA1.2.1578547310.1656282609; __adroll_fpc=c3c97e4c8e3dba48d9e9db366cf844d0-1656443457425; __ar_v4=%7CUVL2S2AUCNELVOQ56Q6CJE%3A20220628%3A1%7CRZKR5AXVWNEDVJRIC2PFSG%3A20220628%3A1; _ga_N26MP432JT=GS1.1.1656443457.1.0.1656443459.0; _uetsid=95228920f58711ec8a0209ebb7767527; _uetvid=b0e702a0f2dc11ec83bd19f70348d2d2; _ga=GA1.2.554372595.1652984938; _ga_9D763FF898=GS1.1.1656443457.32.1.1656443883.59; _ga_CYSMXG40WS=GS1.1.1656443461.27.1.1656443883.60',
}



#循环开始
loop = 1
while loop == 1 :

    #时间戳
    sj=str(int(time.time() * 1000))#13位时间戳
    sj10= str(int(time.time()))#10位时间戳
    time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在时间
    print (f'现在时间：{time2}')
    
    try:

###token price采集
        if len(token_name_control) == 0:
            print('skip token_price')
        else:
            token_price_url=(f'https://api.coingecko.com/api/v3/simple/price?ids={token_name}&vs_currencies=usd')
            token_price_url_content = requests.get(token_price_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (token_price_url_content.text)
            token_price = tex.split('":{"usd":')[1]
            token_price = token_price.split('}')[0]
            token_price = float(token_price)
            print(token_price)

    
###gas fee采集
        if len(gas_fee_control) == 0:
            print('skip gas_fee')
        else:
            gas_fee_url=('https://blocknative-api.herokuapp.com/data')
            gas_fee_url_content = requests.get(gas_fee_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (gas_fee_url_content.text)
            gas_fee = tex.split('"baseFeePerGas":')[1]
            gas_fee = gas_fee.split('}')[0]
            gas_fee = float(gas_fee)



        ###1.0币安买入100USD的FTM_USTC
        if len(BN_token) ==0:
            bn_FTM_USTC_buy_100 = ''
            print('skip eth')
        else:    
            Dex_FTM_USTC_buy100_content = requests.get(bn_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            bn_FTM_USTC_buy_100 = tex.split('"asks":[["')[1]
            bn_FTM_USTC_buy_100 = bn_FTM_USTC_buy_100.split('",')[0]
            bn_FTM_USTC_buy_100 = float(BN_buy_amount)/float(bn_FTM_USTC_buy_100)
            print(f' BN  USD>FTM_USTC: ({bn_FTM_USTC_buy_100})')


    ###1.1、ETH买入100USD的FTM_USTC
        if len(eth_token) ==0:
            ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip eth')
        else:    
            Dex_FTM_USTC_buy100_content = requests.get(eth_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/100000000
            print(f' Dex USD>ETH_FTM_USTC：({ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ###1.2、BSC买入100USD的FTM_USTC
        if len(bsc_token) ==0:
            BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip bsc')
        else:   
            Dex_FTM_USTC_buy100_content = requests.get(bsc_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/100000000
            print(f' Dex USD>BSC_FTM_USTC：({BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ###1.3、fantom买入100USD的FTM_USTC
        if len(fantom_token) ==0:
            fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip fantom')
        else:   
            Dex_FTM_USTC_buy100_content = requests.get(fantom_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"toTokenAmount":"')[1]
            #fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/1000000
            print(f' Dex USD>fantom_FTM_USTC：({fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ###1.4、polygon买入100USD的FTM_USTC
        if len(polygon_token) ==0:
            polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip polygon')
        else:   
            Dex_FTM_USTC_buy100_content = requests.get(polygon_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount[:-18]                                    #去除最后18位，按需更改
            polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)
            print(f' Dex USD>polygon_FTM_USTC：({polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')
            
    ###1.5、avax买入100USD的FTM_USTC
        if len(avax_token) ==0:
            avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip avax')
        else:   
            Dex_FTM_USTC_buy100_content = requests.get(avax_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/100000000
            print(f' Dex USD>avax_FTM_USTC：({avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ###1.6、optimism买入100USD的FTM_USTC
        if len(optimism_token) ==0:
            optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip optimism')
        else:    
            Dex_FTM_USTC_buy100_content = requests.get(optimism_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"toTokenAmount":"')[1]
            optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/100000000
            print(f' Dex USD>optimism_FTM_USTC：({optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')
    ###1.7、arbitrum买入100USD的FTM_USTC
        if len(arbitrum_token) ==0:
            arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip arbitrum')
        else:    
            Dex_FTM_USTC_buy100_content = requests.get(arbitrum_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split('",')[0]
            arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/100000000
            print(f' Dex USD>arbitrum_FTM_USTC：({arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ###1.8、solana买入100USD的FTM_USTC
        if len(solana_token) ==0:
            solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = ''
            print('skip solana')
        else:    
            Dex_FTM_USTC_buy100_content = requests.get(solana_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_buy100_content.text)
            solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = tex.split('outAmount":')[1]
            solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount.split(',"')[0]
            solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount = float(solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)/1000000000
            print(f' Dex USD>solana_FTM_USTC：({solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount})')

    ######② ② ② ② ②价格对比1
        # [eth_token_name, float(ETH_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [bsc_token_name, float(BSC_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [fantom_token_name, float(fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [optimism_token_name, float(optimism_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [avax_token_name, float(avax_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [polygon_token_name, float(polygon_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [BN_token_name, float(bn_FTM_USTC_buy_100)]
        # [arbitrum_token_name, float(arbitrum_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]
        # [solana_token_name, float(solana_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]

        nst_buy = [[BN_token_name, float(bn_FTM_USTC_buy_100)],[fantom_token_name, float(fantom_Dex_FTM_USTC_buy100_receive_FTM_USTC_amount)]]        
        idx_buy, max_value_buy= max(nst_buy, key=lambda item: item[1])
        print(f'最多可买入【{idx_buy}】，核对： 【{max_value_buy}】')

    ######③ ③ ③ ③ ③价格采集2
    #采集卖出URL
        #采集买入的数量
        solana_max_buy_amount=float(max_value_buy)
        solana_max_buy_amount=round(solana_max_buy_amount)

        fantom_max_buy_amount=str(max_value_buy)[:4]
        fantom_max_buy_amount=round(float(fantom_max_buy_amount))*1000000

        max_buy_amount=float(max_value_buy)
        max_buy_amount=int(max_buy_amount*100000000)
        max_buy_amount_1inch=int(max_buy_amount*100000000)
                #eth
        eth_url_sell=(f'https://api-trading.dex.guru/v1/market/1/price/all?buyToken={eth_usd}&sellAmount={max_buy_amount}&sellToken={eth_token}')
                #bsc
        bsc_url_sell=(f'https://api-trading.dex.guru/v1/market/56/price/all?buyToken={bsc_usd}&sellAmount={max_buy_amount}&sellToken={bsc_token}')
                #fantom
        #fantom_url_sell=(f'https://api-trading.dex.guru/v1/market/250/price/all?buyToken={fantom_usd}&sellAmount={max_buy_amount}&sellToken={fantom_token}')
        fantom_url_sell=(f'https://api.1inch.io/v4.0/250/quote?fromTokenAddress={fantom_token}&toTokenAddress={fantom_usd}&amount={fantom_max_buy_amount}')
        print(fantom_url_sell)
                #polygon
        polygon_url_sell=(f'https://api-trading.dex.guru/v1/market/137/price/all?buyToken={polygon_usd}&sellAmount={max_buy_amount}&sellToken={polygon_token}')
                #avax
        avax_url_sell=(f'https://api-trading.dex.guru/v1/market/43114/price/all?buyToken={avax_usd}&sellAmount={max_buy_amount}&sellToken={avax_token}')
                #optimism
        # optimism_url_sell=(f'https://api-trading.dex.guru/v1/market/10/price/all?buyToken={optimism_usd}&sellAmount={max_buy_amount}&sellToken={optimism_token}')
        optimism_url_sell=(f'https://api.1inch.io/v4.0/10/quote?fromTokenAddress={optimism_token}&toTokenAddress={optimism_usd}&amount={max_buy_amount}')
                #arbitrum
        arbitrum_url_sell=(f'https://api-trading.dex.guru/v1/market/42161/price/all?buyToken={arbitrum_usd}&sellAmount={max_buy_amount}&sellToken={arbitrum_token}')
                #solana
        solana_url_sell=(f'https://quote-api.jup.ag/v1/quote?inputMint={solana_token}&outputMint={solana_usd}&amount={solana_max_buy_amount}000000000&slippage=1')

    ###1.0币安卖出100USD的UST
        if len(BN_token) == 0:
            bn_FTM_USTC_sell_100 = ''
            print('skip eth')
        else:    
            Dex_FTM_USTC_sell100_content = requests.get(bn_url,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            bn_FTM_USTC_sell_100 = tex.split('"bids":[["')[1]
            bn_FTM_USTC_sell_100 = bn_FTM_USTC_sell_100.split('",')[0]
            bn_FTM_USTC_sell_100 = float(max_value_buy)*float(bn_FTM_USTC_sell_100)
            print(f' BN  USD>FTM_USTC: ({bn_FTM_USTC_sell_100})')

    ###1.1、ETH买入100USD的FTM_USTC
        if len(eth_token) ==0:
            ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip eth')
        else:    
            Dex_FTM_USTC_sell100_content = requests.get(eth_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' ETH_FTM_USTC > Dex USD : ({ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.2、BSC买入100USD的FTM_USTC
        if len(bsc_token) ==0:
            BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip bsc')
        else:   
            Dex_FTM_USTC_sell100_content = requests.get(bsc_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/100000000
            print(f' BSC_FTM_USTC： > Dex USD : ({BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.3、fantom买入100USD的FTM_USTC
        if len(fantom_token) ==0:
            fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip fantom')
        else:   
            Dex_FTM_USTC_sell100_content = requests.get(fantom_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"toTokenAmount":"')[1]
            fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' fantom_FTM_USTC： > Dex USD : ({fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.4、polygon买入100USD的FTM_USTC
        if len(polygon_token) ==0:
            polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip polygon')
        else:   
            Dex_FTM_USTC_sell100_content = requests.get(polygon_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000000
            print(f' polygon_FTM_USTC： > Dex USD : ({polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')
            
    ###1.5、avax买入100USD的FTM_USTC
        if len(avax_token) ==0:
            avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip avax')
        else:   
            Dex_FTM_USTC_sell100_content = requests.get(avax_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' avax_FTM_USTC： > Dex USD : ({avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.6、optimism买入100USD的FTM_USTC
        if len(optimism_token) ==0:
            optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip optimism')
        else:    
            Dex_FTM_USTC_sell100_content = requests.get(optimism_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"toTokenAmount":"')[1]
            optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' optimism_FTM_USTC > Dex USD : ({optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.7、arbitrum买入100USD的FTM_USTC
        if len(arbitrum_token) ==0:
            arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip arbitrum')
        else:    
            Dex_FTM_USTC_sell100_content = requests.get(arbitrum_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('"buy_amount":"')[1]
            arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split('",')[0]
            arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' arbitrum_FTM_USTC > Dex USD : ({arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ###1.8、solana买入100USD的FTM_USTC
        if len(solana_token) ==0:
            solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = ''
            print('skip solana')
        else:    
            Dex_FTM_USTC_sell100_content = requests.get(solana_url_sell,headers=headers)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            tex = (Dex_FTM_USTC_sell100_content.text)
            solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = tex.split('outAmount":')[1]
            solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount.split(',"')[0]
            solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount = float(solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)/1000000
            print(f' solana_FTM_USTC > Dex USD : ({solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount})')

    ######④ ④ ④ ④ ④价格对比2
        # [eth_token_name, float(ETH_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [bsc_token_name, float(BSC_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [fantom_token_name, float(fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [polygon_token_name, float(polygon_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [avax_token_name, float(avax_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [optimism_token_name, float(optimism_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [BN_token_name, float(bn_FTM_USTC_sell_100)]
        # [arbitrum_token_name, float(arbitrum_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        # [solana_token_name, float(solana_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]
        nst_sell =[[BN_token_name, float(bn_FTM_USTC_sell_100)],[fantom_token_name, float(fantom_Dex_FTM_USTC_sell100_receive_FTM_USTC_amount)]]
        idx_sell, max_value_sell= max(nst_sell, key=lambda item: item[1])
        print(f'最多可卖出【{idx_sell}】，核对： 【{max_value_sell}】')



######⑤ ⑤ ⑤ ⑤ ⑤利润计算
    ###利润核算
        if len(gasfee_pre) ==0:
            LR=float(str(max_value_sell)[0:5])
            max_value_buy=float(str(max_value_buy)[0:5])
        else:    
            LR=float(str(max_value_sell)[0:5]) - float(gasfee_pre)
            max_value_buy=float(str(max_value_buy)[0:5])
            print(f'BUY {idx_buy} LR {LR}, 核对：{max_value_buy}')


        if len(bridge_fee_control) == 0:
            print('skip bridge_fee')
            ##发送到微信群
            if len(gas_fee_control) == 0:
                print('skip gas_fee')
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(LR) >= float(LR1):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>LR：\n>>>核对：【{max_value_buy}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')

            elif float(gas_fee) < float(gas_fee_amount):
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(LR) >= float(LR1):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>LR：\n>>>核对：【{max_value_buy}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')

            elif float(gas_fee) > float(gas_fee_amount):
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(LR) >= float(LR2):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>LR：\n>>>核对：【{max_value_buy}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')

            #打印结果
            print(f'\n>>>>>【\033[1;31m {title} \033[0m】<<<<<')
            if LR >= float(LR1):
                print(f'>>>兑换 \033[1;31m {idx_buy} \033[0m\n>>>卖出 \033[1;31m {idx_sell} \033[0m\n>>>L R：【\033[1;31m{LR}\033[0m】\n>>>核对:【\033[1;31m{max_value_buy}\033[0m】')
            if LR >= float(LR3) and LR < float(LR1):
                print(f'>>>兑换 \033[1;35m {idx_buy} \033[0m\n>>>卖出 \033[1;35m {idx_sell} \033[0m\n>>>L R：【\033[1;35m{LR}\033[0m】\n>>>核对:【\033[1;35m{max_value_buy}\033[0m】')
            if LR < float(LR3):
                print(f'>>>兑换 \033[1;36m {idx_buy} \033[0m\n>>>卖出 \033[1;36m {idx_sell} \033[0m\n>>>L R：【\033[1;36m{LR}\033[0m】\n>>>核对:【\033[1;36m{max_value_buy}\033[0m】')

            # #####核算利润
            # if LR > float(LR1):
            #     print('核算中...')
            #     check()




        else:
            bridge_fee_count=float(bridge_fee_amount)*float(token_price)
            profit=LR-bridge_fee_count

            ##发送到微信群
            if len(gas_fee_control) == 0:
                print('skip gas_fee')
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(profit) >= float(LR1):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>PF：【{profit}】\n>>>核对：【{max_value_buy}】\nBridge Fee: 【{bridge_fee_count}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')

            elif float(gas_fee) < float(gas_fee_control):
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(profit) >= float(LR1):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>PF：【{profit}】\n>>>核对：【{max_value_buy}】\nBridge Fee: 【{bridge_fee_count}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')

            elif float(gas_fee) > float(gas_fee_control):
            #发送企业微信群提醒
                wx_url = wx_send_url  # 机器人
                if float(profit) >= float(LR2):
                    send_message = (f">>>FTM_USTC预警\n>>>兑换【{buy_amount}】{idx_buy}\n>>>卖出【{LR}】{idx_sell}\n>>>PF：【{profit}】\n>>>核对：【{max_value_buy}】\nBridge Fee: 【{bridge_fee_count}】\n{time2}")       
                    
                    def send_msg(content):
                        data = json.dumps({"msgtype": "text", "text": {"content": content}})
                        r = requests.post(wx_url, data, auth=('Content-Type', 'application/json'))

                    send_msg(send_message)
                    print('差价提醒 Send!')




        #打印结果
            print(f'\n>>>>>【\033[1;31m {title} \033[0m】<<<<<')
            if profit >= float(LR1):
                print(f'>>>兑换 \033[1;31m {idx_buy} \033[0m\n>>>卖出 \033[1;31m {idx_sell} \033[0m\n>>>P F：【\033[1;31m{profit}\033[0m】\n>>>核对:【\033[1;31m{max_value_buy}\033[0m】\n>>>Bridge Fee: 【{bridge_fee_count}】')
            if profit >= float(LR3) and profit < float(LR1):
                print(f'>>>兑换 \033[1;35m {idx_buy} \033[0m\n>>>卖出 \033[1;35m {idx_sell} \033[0m\n>>>P F：【\033[1;35m{profit}\033[0m】\n>>>核对:【\033[1;35m{max_value_buy}\033[0m】\n>>>Bridge Fee: 【{bridge_fee_count}】')
            if profit < float(LR3):
                print(f'>>>兑换 \033[1;36m {idx_buy} \033[0m\n>>>卖出 \033[1;36m {idx_sell} \033[0m\n>>>P F：【\033[1;36m{profit}\033[0m】\n>>>核对:【\033[1;36m{max_value_buy}\033[0m】\n>>>Bridge Fee: 【{bridge_fee_count}】')


            # #####核算利润
            # if profit > float(LR1):
            #     print('核算中...')
            #     check()

        #随机休息
        sleep_time=random.randint(3, 5)
        for i in range(sleep_time):
            print("-", end="", flush=True)
            time.sleep(10)



    except:  
    #发送故障提醒 
        sleep_time=random.randint(3,5)

        print('\n 网络故障，等待中......\n')
        num = sleep_time
        for i in range(num):
            print("X", end="", flush=True)
            time.sleep(5)
        print('\n Sleep done!\n')
