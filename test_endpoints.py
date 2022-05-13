import requests
import json


def test_post_questions():
    url = 'https://w786pfro19.execute-api.us-east-1.amazonaws.com/default/question_processor'
    headers = {'Content-Type': 'application/json'}
    payload = {'key1': 1, 'key2': 'value2'}
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    print(resp.text)


def test_get_questions():
    url = 'https://w786pfro19.execute-api.us-east-1.amazonaws.com/default/question_processor'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    print(resp.text)


def test_post_answers():
    url = 'https://wn96j6upad.execute-api.us-east-1.amazonaws.com/default/answer_processor'
    headers = {'Content-Type': 'application/json'}
    payload = {'key1': 1, 'key2': 'value2'}
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    print(resp.text)


def test_get_answers():
    url = 'https://wn96j6upad.execute-api.us-east-1.amazonaws.com/default/answer_processor'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    print(resp.text)


def test_post_score():
    url = 'https://tnqjglxnp2.execute-api.us-east-1.amazonaws.com/default/score_processor'
    headers = {'Content-Type': 'application/json'}
    payload = {'TableName': 'users_score', 'Item': {'id': {'S': '1'}}}
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    print(resp.text)


def test_get_score():
    url = 'https://tnqjglxnp2.execute-api.us-east-1.amazonaws.com/default/score_processor'
    headers = {'Content-Type': 'application/json'}
    payload = {'TableName': 'users_score'}
    resp = requests.get(url, headers=headers, params=payload)
    assert resp.status_code == 200
    print(resp.text)
