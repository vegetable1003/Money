from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvaliSignatureError)
from linebot.models import  *


app= Flask(__name__)




line_bot_api= LineBotApi("6g1a7vGDrHnSn345ATYX+4jDgimHdpoAlN/e2yY2o717kFNWiujz7EMEstiEo+Lng6G0IGpNC2HPAXmU95roOXyGCsDH3NAxSyksHerrVMfyAkQJw+wnCsjaC8JiM2U9uwJqzbUBlgXUGpbSy3vMdAdB04t89/1O/w1cDnyilFU=")
handler=WebhookHandler("4d45ff441a8509be7dea6fca607ac7cb")

@app.route("/callback",method=["POST"])
def callback():
    signature= request.headers['X-Line-Signature']

    body=request.get_data(as_text=True)
    app.logger.info("Request body: "+body)


    try:
        handler.handle(body,signature)
    except IndentationError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message=TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token , message)


if __name__ =="__main__":
    app.run()