from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "everydayishappyday"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state1_1',
        'state1_2',
        'state1_3',
        'state1_4',
        'state1_5',
        'state1_6',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11',
        'state12',
        'state13'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state1_1',
            'conditions': 'is_going_to_state1_1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state1_2',
            'conditions': 'is_going_to_state1_2'
        },
        {
            'trigger': 'advance',
            'source': 'state1_1',
            'dest': 'state1_3',
            'conditions': 'is_going_to_state1_3'
        },
        {
            'trigger': 'advance',
            'source': 'state1_1',
            'dest': 'state1_4',
            'conditions': 'is_going_to_state1_4'
        },
        {
            'trigger': 'advance',
            'source': 'state1_2',
            'dest': 'state1_5',
            'conditions': 'is_going_to_state1_3'
        },
        {
            'trigger': 'advance',
            'source': 'state1_2',
            'dest': 'state1_6',
            'conditions': 'is_going_to_state1_4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state9',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state8',
            'conditions': 'is_going_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state11',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state10',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state12',
            'dest': 'state2',
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1_3',
                'state1_4',
                'state1_5',
                'state1_6',
                'state4',
                'state7',
                'state8',
                'state10',
                'state11',
                'state13'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    show_fsm()
    run(host="localhost", port=5000, debug=True, reloader=True)