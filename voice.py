from aip import AipSpeech
# 语音播报!
APP_ID = '9353398'
API_KEY = 'amV5MIyGHTevu0GdjRmOU7Bs'
SECRET_KEY = '265ccf53c71f1001c848bb755f39d14a'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('二娃!二娃!此鸡乃是非凡鸡! 红色眼睛绿色衣', 'zh', 1, {
    'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('MP3/二娃喊你吃饭了.mp3', 'wb') as f:
        f.write(result)

