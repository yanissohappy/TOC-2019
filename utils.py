import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAd1FPaRVQgBAOQtOQ2oZCBISe0ebdR2V0ShWZBU8q0QpKb8WYWxnTxWiWrZBIZCillpdU62K4lGJUR1KlCc5MvHpgFl70SX5HITdBYXtCD2AlCqSwtaEbqIV322WKYBOx9C11DDn72F1tWr89ovzJbNs5hCe3v6wdZCryMnQ3QZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_url(name,text): #test.
	url="{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
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


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
