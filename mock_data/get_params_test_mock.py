#！/usr/bin/env.python
#coding:utf-8

def mockFoo(result):
    if result == 'success':
        mockData = {
        'request' : {
            'method':'GET',
            'endpoint':'/api/testdetail',
            'params':{'show_env':1},
            'headers':{
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                        "Accept-Encoding": "gzip, deflate, sdch, br",
                        'Accept':'*/*',
                        'Connection':'keep-alive'
            }
        },

        'response' : {
            'result':True,
            'status_code':400,
            'origin': '183.240.198.176', 'url': 'http://httpbin.org/get?show_env=1',
            'headers': {
                    'X-Forwarded-For': '183.240.198.176',
                    'Via': '1.1 vegur',
                    'Accept': '*/*',
                    'X-Request-Id': 'bd1efb67-6020-462f-b257-36f825a16d1c',
                    'Connect-Time': '1',
                    'Accept-Encoding': 'gzip, deflate, sdch, br',
                    'X-Forwarded-Port': '80',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                    'Connection': 'close',
                    'X-Request-Start': '1515074744084',
                    'Host': 'httpbin.org',
                    'Total-Route-Time': '0',
                    'X-Forwarded-Proto': 'http'},
            'args': {'show_env': '1'}
        }
    }
    else:
        mockData = {
            'request': {
                'method': 'GET',
                'endpoint': '/api/testdetail',
            },

            'response': {
                'result':False,
                'code':301,
                'msg':'请求方式不正确'
            }
        }
    return mockData.get('response')