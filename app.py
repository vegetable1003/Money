from line_bot_api import *
from events.basic import  *
from events.oil import *
from events.msg_template import *
import re
import datetime
import twstock 
app=Flask(__name__)

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
    profile= line_bot_api.get_profile(event.source.user_id)
    uid=profile.user_id  #使用者ID
    message_text =str(event.message.text).lower()
    msg=str(event.message.text).upper().strip()  #使用者輸入內容
    emsg=event.message.text
    
    ######## 自動回覆一樣的訊息 #####################
    # message=TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token , message)
    ####### 使用說明 選單 油價查詢 ##################
    if message_text =='@使用說明':
        about_us_event(event)
        Usage(event)

    if event.message.text=="油價":
        content= oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
    ########### 股票區 #############################
    if event.message.text == "股價查詢":
        line_bot_api.push_message(uid,TextSendMessage("請輸入#加股票代號..."))

    ##股價查詢

    if re.match("想知道股價[0-9]",msg):
        stockNumber=msg[2:6]
        btn_msg=stock_reply_other(stockNumber)
        line_bot_api.push_message(uid,btn_msg)
        return 0
    if(emsg.startswith("#")):
        text=emsg[1:]
        content=""

        stock_rt=twstock.realtime.get(text)
        my_datetime= datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time=my_datetime.strftime("%H:%M:%S")

        content+='%s(%s) %s\n' %(
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        content+='現價: %s/開盤: %s\n' %(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        content+='最高: %s/最低: %s\n' %(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        content+='量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume']
        )

        stock=twstock.Stock(text)
        content +='-----/n'
        content +='最近五日價格: \n'
        price5 =stock.price[-5:][::-1]
        date5=stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s \n' %(date5[i].strftime("%Y-%m-%d"),price5[i])

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )



@handler.add(FollowEvent)
def handle_folow(event):
    welcome_msg ='''Hello! 您好，歡迎您再次成為 恭禧發財 的好友！
                                   
封鎖解除了'''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))    


    ###########先進趨勢#########################
    
    # if event.message.text=='@先進趨勢':
    #     buttons_template = TemplateSendMessage(
    #         alt_text="小幫手 template",
    #         template=ButtonsTemplate(
    #             title="選擇服務",
    #             text="請選擇",
    #             thumbnail_image_url="https://i.imgur.com/Ssns07Ub.jpg",
    #             actions=[
    #                 MessageTemplateAction(
    #                     label="油價查詢",
    #                     text="油價查詢"
    #                 ),
    #                  MessageTemplateAction(
    #                     label="匯率查詢",
    #                     text="匯率查詢"
    #                 ),
    #                  MessageTemplateAction(
    #                     label="股價查詢",
    #                     text="股價查詢"
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token,buttons_template)
if __name__ =="__main__":
    app.run()