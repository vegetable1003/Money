from line_bot_api import *

def stock_reply_other(stockNumber):
    content_text = "即時股價和K線圖"
    text_message = TextSendMessage(
                                text = content_text , 
                                quick_reply = QuickReply(
                                    items = [
                                        QuickReplyButton(
                                                action = MessageAction(
                                                    label = "即時股價" , 
                                                    text = "#" + stockNumber , 
                                                )   
                                        ) ,
                                        QuickReplyButton (
                                                action = MessageAction(
                                                    label = "K線圖" , 
                                                    text = "@K" + stockNumber
                                                )
                                        ),
                                    ]
                                ))
    return text_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
                        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/y85t4DP.jpeg",
                        "size": "5xl",
                        "aspectMode": "cover",
                        "aspectRatio": "150:196",
                        "gravity": "center",
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "150:98",
                            "gravity": "center",
                            "url": "https://i.imgur.com/QjKHaOi.png"
                        },
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/xFPkFaV.jpeg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "150:98",
                            "gravity": "center"
                        }
                        ],
                        "flex": 1
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/lkK1WZz.png",
                            "aspectMode": "cover",
                            "size": "full"
                        }
                        ],
                        "cornerRadius": "100px",
                        "width": "72px",
                        "height": "72px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "contents": [],
                            "size": "xl",
                            "text": "股價到價提醒",
                            "weight": "bold",
                            "action": {
                            "type": "message",
                            "label": "到價提醒",
                            "text": "股價提醒"
                            }
                        },
                        {
                            "type": "text",
                            "text": "到價提醒定時通知價格",
                            "size": "sm",
                            "color": "#B34E80"
                        }
                        ]
                    }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/oXtXe8R.png",
                            "aspectMode": "cover",
                            "size": "full"
                        }
                        ],
                        "cornerRadius": "100px",
                        "width": "72px",
                        "height": "72px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "contents": [],
                            "size": "xl",
                            "text": "匯率即期推播",
                            "action": {
                            "type": "message",
                            "label": "匯率提醒",
                            "text": "匯率提醒"
                            },
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "匯率價格即時呈現",
                            "color": "#B34E80",
                            "size": "sm"
                        }
                        ]
                    }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px"
                }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "⛔關閉提醒⛔",
                    "size": "lg",
                    "weight": "bold",
                    "align": "center",
                    "color": "#91091E",
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "關閉提醒"
                    }
                }
                ]
            }
            }
        #             contents={
        # "type": "bubble",
        # "body": {
        #     "type": "box",
        #     "layout": "vertical",
        #     "contents": [
        #     {
        #         "type": "text",
        #         "text": "🌻 幣別種類 🌻",
        #         "weight": "bold",
        #         "size": "xl",
        #         "color": "#003E3E",
        #         "contents": [],
        #         "style": "normal",
        #         "position": "relative",
        #         "align": "center"
        #     }
        #     ]
        # },
        # "footer": {
        #     "type": "box",
        #     "layout": "vertical",
        #     "contents": [
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "美金",
        #             "text": "USD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#949449",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "日圓",
        #             "text": "JPY"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#949449",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "港幣",
        #             "text": "HKD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#949449",
        #             "margin": "sm"
        #         }
        #         ],
        #         "borderWidth": "none"
        #     },
        #     {
        #         "type": "separator",
        #         "margin": "md"
        #     },
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "英鎊",
        #             "text": "GBP"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#4F9D9D",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "澳幣",
        #             "text": "AUD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#4F9D9D",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "加拿大幣",
        #             "text": "CAD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#4F9D9D",
        #             "margin": "sm"
        #         }
        #         ]
        #     },
        #     {
        #         "type": "separator",
        #         "margin": "md"
        #     },
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "瑞士法郎",
        #             "text": "CHF"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#AD5A5A",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "新加坡",
        #             "text": "SGD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#AD5A5A",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "南非幣",
        #             "text": "ZAR"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#AD5A5A",
        #             "margin": "sm"
        #         }
        #         ]
        #     },
        #     {
        #         "type": "separator",
        #         "margin": "md"
        #     },
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "瑞典幣",
        #             "text": "SEK"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#7373B9",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "泰幣",
        #             "text": "THB"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#7373B9",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "菲比索",
        #             "text": "PHP"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#7373B9",
        #             "margin": "sm"
        #         }
        #         ]
        #     },
        #     {
        #         "type": "separator",
        #         "margin": "md"
        #     },
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "印尼幣",
        #             "text": "IDR"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#5CADAD",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "韓元",
        #             "text": "KRW"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#5CADAD",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "馬來幣",
        #             "text": "MYR"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#5CADAD",
        #             "margin": "sm"
        #         }
        #         ]
        #     },
        #     {
        #         "type": "separator",
        #         "margin": "md"
        #     },
        #     {
        #         "type": "box",
        #         "layout": "horizontal",
        #         "contents": [
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "越南盾",
        #             "text": "VND"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#84C1FF",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "人民幣",
        #             "text": "CNY"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#84C1FF",
        #             "margin": "sm"
        #         },
        #         {
        #             "type": "button",
        #             "action": {
        #             "type": "message",
        #             "label": "紐元",
        #             "text": "NZD"
        #             },
        #             "gravity": "center",
        #             "style": "primary",
        #             "color": "#84C1FF",
        #             "margin": "sm"
        #         }
        #         ]
        #     }
        #     ]
        # }
        # }
                    
    )
    return flex_message