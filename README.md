# TOC Project 2018
###Topic:超展開奇片式自助餐有限狀態機

Template Code for TOC Project 2018

A Facebook messenger bot based on a finite state machine


## Finite State Machine
![fsm](./img/fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "使用說明"
		* Reply: "遊戲的一開始，請您輸入想吃的自助餐，[吃大八]？[吃海港]？[吃香格里拉]？"
		* Reply: ![為甚麼你不問神奇海螺呢](https://img.moegirl.org/common/thumb/7/7b/SpongeBob_SquarePants.jpg/250px-SpongeBob_SquarePants.jpg)
		* Next State: state3→user

	* Input: "吃大八"
		* Reply: "你選錯了，只能選海港，這就是自助餐一言堂狀態機。"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state1→user
		
	* Input: "吃香格里拉"
		* Reply: "你選錯了，只能選海港，這就是自助餐一言堂狀態機。"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state1→user

	* Input: "吃海港"
		* Reply: "您真是會選擇，好吃的自助餐在海港，猜猜看好吃的時段是甚麼時候？[下午茶]或[晚餐]？"
		* Next State: state2	
* state2
	* Input: "下午茶"
		* Reply: "叭叭！！！！下午茶很難吃捏！打沒！掰掰！"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state4→user

	* Input: "晚餐"
		* Reply: "對呀，選晚餐就對了，從現在開始您可以跟食物來個美好的邂逅，你要選擇[生魚片]還是[剩魚片]？"
		* Next State: state5
* state5		
	* Input: "生魚片"
		* Reply: "經理走過來，說：「您吃的鮭魚生魚片來自濁水溪，是個不可多得的珍貴食材！你[知道]或[不知道]濁水溪有鮭魚？」"
		* Next State: state6

	* Input: "剩魚片"
		* Reply: "孟婆：「嘻嘻您吃了剩魚片所以拉到壞掉，重新輪迴，喝杯孟婆湯吧。（強灌）」"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state7→user		
* state6
	* Input: "知道"
		* Reply: "經理：「這位客人，您不但懂吃，還懂地理，[要]或[不要]明天跟我去環遊世界，探查地理？」"
		* Next State: state9

	* Input: "不知道"
		* Reply: "經理：「濁水溪有鮭魚！我說得算！給我滾出去！海港不要有你這種客人！」"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state8→user
* state9		
	* Input: "要"
		* Reply: "吃一次海港，寫成了亙股雋永的淒美愛情故事，所以請大家多多支持海港（按：海港與作者沒有任何關係）"
		* Reply: ![Iloveu](https://sayingimages.com/wp-content/uploads/Lily-the-Swim-Pup-Love-You.jpg)
		* Next State: state11→user

	* Input: "不要"
		* Reply: "經理：「不要？給我滾出去！海港不要有你這種客人！」"
		* Reply: ![GO TO HELL](https://i.imgflip.com/13jurj.jpg)
		* Next State: state10→user		
		
