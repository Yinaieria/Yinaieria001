from aip import AipSpeech
import config

# 从 config.py 里读取你的密钥
client = AipSpeech(config.APP_ID, config.API_KEY, config.SECRET_KEY)

def recognize_speech(file_path):
    # 读取音频文件
    with open(file_path, 'rb') as fp:
        audio_data = fp.read()

    # 调用百度API，格式为wav，采样率16000，普通话
    result = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1537})

    if result['err_no'] == 0:
        return result['result'][0]
    else:
        return f"识别失败，错误码：{result['err_no']}，原因：{result['err_msg']}"

if __name__ == '__main__':
    print("正在识别 test.wav ...")
    text = recognize_speech('test.wav')
    print("识别结果：", text)