from line_bot_api import *
from events.basic import *
from events.oil import *
from events.msg_template import *
from model.mongodb import *
from events.EXRate import *
import re
import twstock
import datetime


app = Flask(__name__)

#抓使用者關心的股票
def cache_users_stock():
    db=constructor_stock()
    namelist = db.list_collection_names()
    users = []
    for i in range(len(namelist)):
        collect = db[namelist[i]]
        cel = list(collect.find({"tag":"stock"}))
        users.append(cel)
    return users

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'ID?' or event.message.text == 'id?':
        User_ID = TextMessage(text=event.source.user_id)
        line_bot_api.reply_message(event.reply_token, User_ID)
        print ('Reply User ID =>' + event.source.user_id)
    elif event.message.text == 'GroupID?':
        Group_ID = TextMessage(text=event.source.group_id)
        line_bot_api.reply_message(event.reply_token, Group_ID)
        print ('Reply Group ID =>' + event.source.group_id)
    else:
        None
    
#line_bot_api.push_message("USER ID or GROUP ID",TextSendMessage(text=""))

#監聽所有來自 /callback的post request
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id  # 使用者id
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip()
    emsg = event.message.text
    user_name=profile.display_name #使用者名稱

    #############"使用說明"############
    if message_text == "@使用說明":
        about_us_event(event)
        Usage(event)

    #############"油價查詢"############
    if message_text == "想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(content)
        )

    #############"股價查詢"############
    if message_text == "股價查詢":
        line_bot_api.push_message(
        uid, 
        TextSendMessage("請輸入'#' + '股票代號'\n範例：#2330")
        )

    #股價查詢
    if re.match("想知道股價[0-9]" , msg):
        stockNumber = msg[5:9]
        btn_msg = stock_reply_other(stockNumber)
        line_bot_api.push_message(uid , btn_msg)
        return 0
    #新增使用者關注的股票到mongodb
    if re.match("關注[0-9]{4}[<>][0-9]" ,msg):
        stockNumber =msg[2:6]
        line_bot_api.push_message(uid,TextSendMessage("加入股票代號"+stockNumber))
        content =write_my_stock(uid,user_name,stockNumber, msg[6:7], msg[7:])
        line_bot_api.push_message(uid,TextSendMessage(content))

    #查詢股票篩選條件清單
    if re.match('股票清單',msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，股票查詢中...'))
        content = show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    #刪除存在資料庫裏面的股票
    if re.match('刪除[0-9]{4}',msg):
        content = delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    #清空存在資料庫裏面的股票
    if re.match('刪除[0-9]{4}',msg):
        content = delete_my_allstock(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0

    if(msg.startswith("#")):
        text=msg[1:]
        content=''
    
    if (emsg.startswith('#')):
        text = emsg[1:]
        content =''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content +='%s (%s) %s\n' % (
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time)
        
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open'])
        
        content += '最高: %s / 最低:%s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low'])
        
        content += '量: %s\n'%(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' % (date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(text=content)
        )
    #################匯率區####################
    if re.match("幣別種類",emsg):
        message= show_Button()
        line_bot_api.reply_message(event.reply_token,message)
    
    if re.match("查詢換匯[A-Z]{3}", msg):
        msg = msg[4:]
        content = showcurrency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
    
    ##換匯
    if re.match("換匯[A-Z]{3}/[A-Z]{3}/[0-9]", msg):
        line_bot_api.push_message(uid, TextSendMessage("正在為您計算..."))
        content = getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))

     # ############"@小幫手"############
    if message_text == "@小幫手":
        button_template = ButtonsTemplate()
        line_bot_api.reply_message(
        event.reply_token, button_template
        )
    
             #######################股價提醒#######################
    if re.match("關閉提醒",msg):
        import schedule
        schedule.clear()
    if re.match("股價提醒", msg):
        import schedule
        import time
        # 查看當前股價
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, "html.parser")
            getstock= soup.findAll('span')[11].text
            content = stock + "當前股市價格為: " +  getstock
            if condition == '<':
                content += "\n篩選條件為: < "+ price
                if float(getstock) < float(price):
                    content += "\n符合" + getstock + " < " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '>':
                content += "\n篩選條件為: > "+ price
                if float(getstock) > float(price):
                    content += "\n符合" + getstock + " > " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == "=":
                content += "\n篩選條件為: = "+ price
                if float(getstock) == float(price):
                    content += "\n符合" + getstock + " = " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
        def job():
            print('啟動喔')
            line_bot_api.push_message(uid , TextSendMessage("快買股票喔!"))
            dataList = cache_users_stock()
            # print(dataList)
            for i in range(len(dataList)):
                for k in range(len(dataList[i])):
                    # print(dataList[i][k])
                    look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
        schedule.every(5).seconds.do(job).tag('daily-tasks-stock'+uid,'second') #每10秒執行一次
        #schedule.every().hour.do(job) #每小時執行一次
        #schedule.every().day.at("17:19").do(job) #每天9點30執行一次
        #schedule.every().monday.do(job) #每週一執行一次
        #schedule.every().wednesday.at("14:45").do(job) #每週三14點45執行一次
        # 無窮迴圈
        while True: 
            schedule.run_pending()
            time.sleep(1)

        


@handler.add(FollowEvent)
def handle_follow(event):
    emojis = [
        {
            "index": 0, 
            "productId": "5ac21a18040ab15980c9b43e", 
            "emojiId": "009"
        }, 
        {
            "index": 16, 
            "productId": "5ac21a18040ab15980c9b43e", 
            "emojiId": "014"
        }
    ]

    welcome_message = TextSendMessage(text='''$ Agave Finance $
    您好，歡迎加入成為 Agave Finance 的好友!!!
    我是Agave財經小幫手~
    下方選單有：
    股票查詢、油價查詢、匯率查詢、自動提醒、資訊整理、使用說明
    使用上有任何問題可以參考使用說明''', emojis=emojis)

    line_bot_api.reply_message(
        event.reply_token, welcome_message
        )
    

@handler.add(UnfollowEvent)
def hadle_unfollow(event):
    print(event)


if __name__ == "__main__":
    app.run()
