import json

with open('C:\\Users\\lisac\\PycharmProjects\\pythonProject\\YT Example\\ytsample.json') as f:
    data = json.load(f)

print(data.keys())
print(data['items'])
print(data['kind'])
print(data['etag'])
print(data['nextPageToken'])
print(data['pageInfo']['totalResults'])

for item in data['items']:
    # direct reference method
    print(item)
    print('kind: ' +item['kind'])
    print('etag: ' +item['etag'])
    print('id kind: ' + item['id']['kind'])
    if 'videoId' in item['id']:
        print('videoID: ' + item['id']['videoId'])
    else:
        print('no video id')
    if 'channelId' in item['id']:
        print('channelID: ' + item['id']['channelId'])
    else:
        print('no channel id')

    # get method
    x = item.get("kind")
    print('item kind: ' + x)

    y = item['id'].get("kind")
    print('item id kind: ' + y)

    # use this to test an assign a default value if key "videoId" does not exist
    z = item['id'].get("videoId", "no video id")
    print('item id video id: ' + z)

    c = item['id'].get("channelId", "no channel id")
    print('item id channel id: ' + c)