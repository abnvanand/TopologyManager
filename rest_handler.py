def redeploy_service(serviceId):
    print("Request sent to redeploy serviceId:", serviceId)


def getContainerStatus(service):
    containerId, ip, port = service.containerId, service.ip, service.port

    import requests

    # Get the dataset
    url = f"http://{ip}:{port}/v1.24/containers/{containerId}/json"
    response = requests.get(url)
    dict = response.json()

    # import ipdb
    # ipdb.set_trace()

    status = dict['State']['Running']

    return status
