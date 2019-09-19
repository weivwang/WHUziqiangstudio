#-*-coding:utf-8-*-

#引入qrcode
import qrcode
from PIL import Image
import os

#欢迎语
print("欢迎使用package")

#选择功能
choose = int(input('请选择你要使用的功能：1，加密并解密；2,字典功能；3，读取文件并生成二维码：'))

#加密
if choose == 1:
    import base64
    try:
        s = input('请输入你要加密的字符:')
        a = base64.b64encode(s.encode('Utf-8'))     #实现加密
        print ('加密后的字符为:',a)
        choose2 = int(input('是否需要解密：4，需要；5，不需要:'))
        if choose2 == 4:
            b = base64.b64decode(a)   #实现解密
            print ('解密后的字符为:',b)
    except:
        print('非法输入')    #非法处理

#字典功能
elif choose == 2:
    print ('欢迎使用字典功能')
    try:
        key1 = input('请输入你的第一个key：')
        value1 = input('请输入你的第一个value：')
        key2 = input('请输入你的第二个key：')
        value2 = input('请输入你的第二个value：')
        key3 = input('请输入你的第三个key：')
        value3 = input('请输入你的第三个value：')
        dict1 = {key1 : value1, key2 : value2, key3 : value3} 
        a = type(dict1)
        print ('为你创建的字典为:',dict1,'类型为：',a)
        L = [key1, key2, key3]
        R = [value1, value2, value3]
        dict2 = dict(zip(R, L))
        b = type(dict2)
        print('反转后的字典为: ',dict2,'类型为：',b)
        import json
        jason1 = json.dumps(dict1)
        c = type(jason1)
        print('转化后的jason:',jason1, '类型为：',c)
    except:
        print('非法输入')


#读取指定文件并生成二维码功能
elif choose == 3:
    file1 = input('请输入你要处理的txt文件名：')
    f = open(file1)
    d = f.read()
    print('文件内容为:',d)

    def make_qr(str,save):
        qr=qrcode.QRCode(
            version = 4,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(str)
        qr.make(fit=True)
    
        img=qr.make_image()
        img.save(save)
        save_path = 'txtqrcode.jpg'
        str = d
print('按enter键退出程序')
rew = input()





    


    
    
    
