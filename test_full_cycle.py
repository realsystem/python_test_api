import requests
import json

url = 'https://w786pfro19.execute-api.us-east-1.amazonaws.com/default/question_processor'
headers = {'Content-Type': 'application/json'}


def test_send_question_john1():
    user_id = 'John'
    my_question = 'Calculate 2+2'
    payload = {'uid': user_id, 'question': my_question}
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    # print(resp.text)


def test_send_question_sara1():
    user_id = 'Sara'
    my_question = 'How many stars in the sky?'
    payload = {'uid': user_id, 'question': my_question}
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    # print(resp.text)


def test_get_question_sara():
    user_id = 'Sara'
    while 1:
        resp = requests.get(url, headers=headers)
        assert resp.status_code == 200
        # print(resp.text)
        json_data = json.loads(resp.text)
        if 'Messages' in json_data:
            message = json.loads(json_data['Messages'][0]['Body'])
            if 'uid' not in message:
                continue
            print(message)
        else:
            print('End of queue')
            break
        if message['uid'] != user_id:
            print(message['question'])
            break
