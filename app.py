from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import  *


app= Flask(__name__)




line_bot_api= LineBotApi("6g1a7vGDrHnSn345ATYX+4jDgimHdpoAlN/e2yY2o717kFNWiujz7EMEstiEo+Lng6G0IGpNC2HPAXmU95roOXyGCsDH3NAxSyksHerrVMfyAkQJw+wnCsjaC8JiM2U9uwJqzbUBlgXUGpbSy3vMdAdB04t89/1O/w1cDnyilFU=")
handler=WebhookHandler("4d45ff441a8509be7dea6fca607ac7cb")

@app.route("/callback",methods=["POST"])
def callback():
    signature= request.headers['X-Line-Signature']

    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)


    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message=TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token , message)

    emoji = [
            {
                "index":0,
                "productId":"5ac2197b040ab15980c9b43d",
                "emojiId":"002"
            },
            {
                "index":17,
                "productId":"5ac2197b040ab15980c9b43d",
                "emojiId":"006"
            }
    ]
    text_message = TextSendMessage(text='''$ Master Finance $
Hello! 您好，歡迎您成為 Master Finance 的好友！
                                   
我是Master 財經小幫手
                                   
-這裡有股票、匯率資訊哦～
-直接點選下方[圖中]選單功能
                                   
期待您的光臨''',emojis=emoji)
    sticker_message = StickerMessage(
        package_id='8522',
        sticker_id='16581271'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,sticker_message])


if __name__ =="__main__":
    app.run()