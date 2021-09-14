import json


from files import way_better2


if __name__ == '__main__':
    data = way_better2('data.json')
    print('raw data is:', data, type(data))

    x = json.loads(data)

    print(x)
    print('-----------')
    print(x['object']['key'])




