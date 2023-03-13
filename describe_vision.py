import cloudsight

def describe_photo(Path):
    auth = cloudsight.SimpleAuth('mRTVz-5iyX19xMIaLBe-_Q')
    api = cloudsight.API(auth)

    with open(Path, 'rb') as f:
        response = api.image_request(f, Path, {
            'image_request[locale]': 'zh-CN',
            'image_request[language]': 'zh-CN',
        })
    status = api.image_response(response['token'])
    if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
        # Done!
        pass
    status = api.wait(response['token'], timeout=30)
    return status