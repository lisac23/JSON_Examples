import json

with open('ytsample.json') as f:
    data = json.load(f)

print(data.keys())
print(data['items'])
print(data['kind'])
print(data['etag'])
print(data['nextPageToken'])
print(data['pageInfo']['totalResults'])

for item in data['items']:
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
