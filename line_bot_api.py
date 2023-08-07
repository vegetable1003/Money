from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import  *


app= Flask(__name__)

line_bot_api= LineBotApi("6g1a7vGDrHnSn345ATYX+4jDgimHdpoAlN/e2yY2o717kFNWiujz7EMEstiEo+Lng6G0IGpNC2HPAXmU95roOXyGCsDH3NAxSyksHerrVMfyAkQJw+wnCsjaC8JiM2U9uwJqzbUBlgXUGpbSy3vMdAdB04t89/1O/w1cDnyilFU=")
handler=WebhookHandler("4d45ff441a8509be7dea6fca607ac7cb")


