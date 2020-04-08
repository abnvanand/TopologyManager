def redeploy_service(service):
    # TODO: Send request to SLCM
    #  ??? How do I know SLCM's rest endpoint's IP and PORT

    from configparser import ConfigParser
    cfg = ConfigParser()

    cfg.read('config.ini')

    ip = cfg.get('ServiceLCM', 'serverIp')
    port = cfg.get('ServiceLCM', 'servicePort')

    import requests
    startRequestJson = {"serviceId": service.serviceId,
                        "serviceName": service.serviceName,
                        "userId": service.userId}

    print("Request sent to redeploy service:", service)
    print("Request:", startRequestJson)
    r = requests.post(url=f"http://{ip}:{port}/servicelcm/service/start",
                      headers={'Content-type': 'application/json'},
                      json=startRequestJson)

    print("Response:", r.status_code)

    if r.status_code == 200:
        return True

    return False


def getContainerStatus(service):
    containerId, ip, port = service.containerId, service.ip, service.port

    import requests

    # Get the dataset
    url = f"http://{ip}:{port}/v1.24/containers/{containerId}/json"
    print("URL:", url)
    response = requests.get(url)
    print(response)
    dict = response.json()

    # import ipdb
    # ipdb.set_trace()

    status = dict['State']['Running']

    return status
