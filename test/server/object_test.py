'''
Test object related functions
'''
from unrealcv import client
from conftest import checker

def test_object_list():
    client.connect()
    res = client.request('vget /objects')
    obj_ids = res.split(' ')
    assert checker.not_error(res)

    for obj_id in obj_ids:
        color = client.request(f'vget /object/{obj_id}/color')
        assert checker.not_error(color)
