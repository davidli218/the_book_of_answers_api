answer_url = '/api/v1/answer'


def test_get_answer(client):
    response = client.get(answer_url)
    assert response.status_code == 200
    assert response.json.keys() == {'answer'}
    assert response.json['answer']


def test_answer_invalid_method(client):
    assert client.post(answer_url).status_code == 405
    assert client.put(answer_url).status_code == 405
    assert client.delete(answer_url).status_code == 405
