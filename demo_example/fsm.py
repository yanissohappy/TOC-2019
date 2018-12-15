from bottle import route,run,request,abort,static_file
from transitions.extensions import GraphMachine
import requests
import os

GRAPH_URL="https://graph.facebook.com/v2.6"
PAGE_TOKEN="EAAd1FPaRVQgBAOQtOQ2oZCBISe0ebdR2V0ShWZBU8q0QpKb8WYWxnTxWiWrZBIZCillpdU62K4lGJUR1KlCc5MvHpgFl70SX5HITdBYXtCD2AlCqSwtaEbqIV322WKYBOx9C11DDn72F1tWr89ovzJbNs5hCe3v6wdZCryMnQ3QZDZD"
VERIFY_TOKEN="test"
"""
ACCESS_TOKEN=os.environ["EAAd1FPaRVQgBAOQtOQ2oZCBISe0ebdR2V0ShWZBU8q0QpKb8WYWxnTxWiWrZBIZCillpdU62K4lGJUR1KlCc5MvHpgFl70SX5HITdBYXtCD2AlCqSwtaEbqI"]
VERIFY_TOKEN=os.environ["everydayishappyday"]
PORT=os.environ["4000"]
"""

def send_text_message(name,text):
	url="{0}/me/messages?access_token={1}".format(GRAPH_URL,PAGE_TOKEN)
	ctx={
		"recipient":{
			"id":name
		},
		"message":{
			"text":text
		}
	}
	response=requests.post(url,json=ctx)
	if response.status_code!=200:
		print("Unable to send message: "+response.text)
	return response
def send_image_message(name,text):
	url="{0}/me/messages?access_token={1}".format(GRAPH_URL,PAGE_TOKEN)
	ctx={
		"recipient":{
			"id":name
		},
		"message":{
			"attachment":{
				"type":"image",
				"payload":{
					"url":text
				}
			}
		}
	}
	response=requests.post(url,json=ctx)
	if response.status_code!=200:
		print("Unable to send message: "+response.text)
	return response
#不知道為什麼只傳一次，他會一直進來。。。???
class TocMachine(GraphMachine):
	def __init__(self,**machine_configs):
		self.machine=GraphMachine(model=self,**machine_configs)
	def is_going_to_state1(self,event):
		print("is going to state1")
		if event.get("message"):
			text=event["message"]["text"]
			return text.lower()=="go to state1"
		return False
	def is_going_to_state2(self,event):
		print("is going to state2")
		if event.get("message"):
			text=event["message"]["text"]
			return text.lower()=="go to state2"
		return False
	def on_enter_state1(self, event):
		print("I'm entering state1")
		sender_id=event['sender']['id']
		responese=send_image_message(sender_id,"http://www.lxjk999.com/uploads/allimg/150429/1-15042923450bS.jpg")
		self.go_back()
	def on_exit_state1(self):
		print("Leaving state1")
	def on_enter_state2(self, event):
		print("I'm entering state2")
		sender_id=event['sender']['id']
		responese=send_text_message(sender_id,"I'm entering state2")
		self.go_back()
	def on_exit_state2(self):
		print("Leaving state2")
machine=TocMachine(
	states=[
		"user",
		"state1",
		"state2"
	],
	transitions=[
		{
			"trigger":"advance",
			"source":"user",
			"dest":"state1",
			"conditions":"is_going_to_state1"
		},
		{
			"trigger":"advance",
			"source":"user",
			"dest":"state2",
			"conditions":"is_going_to_state2"
		},
		{
			"trigger":"go_back",
			"source":[
				"state1",
				"state2"
			],
			"dest":"user"
		}
	],
	initial="user",
	auto_transitions=False,
	show_conditions=True,
)
@route("/webhook",method=["GET","POST"])
def webhook():
#method="GET"
	if request.method == "GET":
		mode=request.GET.get("hub.mode")
		verify_token=request.GET.get("hub.verify_token")
		challenge=request.GET.get("hub.challenge")
		if mode=="subscribe" and verify_token==VERIFY_TOKEN:
			print("WEBHOOK_VERIFIED")
			return challenge
		else:
			abort(403)
#method="POST"
	else:
		body=request.json
		if body["object"]=="page":
			event=body["entry"][0]["messaging"][0]
			machine.advance(event)
			return "OK"
@route("/show-fsm",method=["GET"])
def show_fsm():
	machine.get_graph().draw("fsm.png",prog="dot",format="png")
	return static_file("fsm.png",root="./",mimetype="image/png")
if __name__ == "__main__":
	show_fsm()
	run(host="localhost",port=4000,debug=True)
