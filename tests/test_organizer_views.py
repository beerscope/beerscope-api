import json


def test_add_keg(client):
    from beerscope import models

    assert models.Keg.query.count() == 0
    beer_description = 'Some awesome beer'
    response = client.post(
        '/api/keg',
        content_type='application/json',
        data=json.dumps({'description': beer_description}),
    )
    assert response.status_code == 201, json.loads(response.get_data(as_text=True))['message']
    assert models.Keg.query.count() == 1
