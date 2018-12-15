# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '吃大八' or '吃香格里拉' #輸入這兩個是很不可以的，只有海港比較好吃，這就是自助餐一言堂
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '吃海港'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '使用說明'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '下午茶' #下午茶很難吃，我是認真的
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '晚餐' #晚餐葛來分多得100000分
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '生魚片' #很棒棒
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '剩魚片' #糟糕了唷
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '知道' #經理會給愛的鼓勵
        return False

    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '不知道' #經理會把你請出去（哪門子的經理？！）
        return False

    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '要' #跟經理環遊世界，很棒！
        return False

    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '不要' #不環遊世界，經理會把你請出去（again 哪門子的經理？！）
        return False


    def on_enter_state1(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你選錯了，只能選海港，這就是自助餐一言堂狀態機。")
        responese = send_image_url(sender_id,"https://i.imgflip.com/13jurj.jpg" )#TEST YOU GO TO HELL
        self.go_back()

    def on_enter_state2(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "您真是會選擇，好吃的自助餐在海港，猜猜看好吃的時段是甚麼時候？[下午茶]或[晚餐]？")

    def on_enter_state3(self, event): #使用說明
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "遊戲的一開始，請您輸入想吃的自助餐，[吃大八]？[吃海港]？[吃香格里拉]？")
        responese = send_image_url(sender_id,"https://img.moegirl.org/common/thumb/7/7b/SpongeBob_SquarePants.jpg/250px-SpongeBob_SquarePants.jpg" )#TEST 為甚麼你不問神奇海螺ㄋ
        self.go_back()

    def on_enter_state4(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "叭叭！！！！下午茶很難吃捏！打沒！掰掰！")
        responese = send_image_url(sender_id,"https://i.imgflip.com/13jurj.jpg" )#TEST YOU GO TO HELL
        self.go_back()

    def on_enter_state5(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "對呀，選晚餐就對了，從現在開始您可以跟食物來個美好的邂逅，你要選擇[生魚片]還是[剩魚片]？")

    def on_enter_state6(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "經理走過來，說：「您吃的鮭魚生魚片來自濁水溪，是個不可多得的珍貴食材！你[知道]或[不知道]看過濁水溪的鮭魚嗎？」")

    def on_enter_state7(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "孟婆：「嘻嘻您吃了剩魚片所以拉到壞掉，重新輪迴，喝杯孟婆湯吧。（強灌）」")#回答[剩餘片]的後果->回到user
        responese = send_image_url(sender_id,"https://i.imgflip.com/13jurj.jpg" )#TEST YOU GO TO HELL
        self.go_back()

    def on_enter_state8(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "經理：「濁水溪有鮭魚！我說得算！給我滾出去！海港不要有你這種客人！」")#回答[沒有]鮭魚的後果->回到user
        responese = send_image_url(sender_id,"https://i.imgflip.com/13jurj.jpg" )#TEST YOU GO TO HELL
        self.go_back()

    def on_enter_state9(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "經理：「這位客人，您不但懂吃，還懂地理，[要]或[不要]明天跟我去環遊世界，探查地理？」")

    def on_enter_state10(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "經理：「不要？給我滾出去！海港不要有你這種客人！」")#回答[不要]環遊世界的後果->回到user
        responese = send_image_url(sender_id,"https://i.imgflip.com/13jurj.jpg" )#TEST YOU GO TO HELL
        self.go_back()

    def on_enter_state11(self, event):
        #print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "吃一次海港，寫成了亙股雋永的淒美愛情故事，所以請大家多多支持海港（按：海港與作者沒有任何關係）")#回答[要]環遊世界的後果->回到user
        responese = send_image_url(sender_id,"https://sayingimages.com/wp-content/uploads/Lily-the-Swim-Pup-Love-You.jpg" )#TEST I LOVE U
        self.go_back()




   