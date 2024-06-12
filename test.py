import logging
import boto3
from botocore.config import Config

API_KEY = ""bchfverjfvjknkj
def list_specific_services(cluster_name, service_name):
    """
    Lists all services with matching service_name and each pagesize of 100 within a specific cluster

    Args:
        cluster_name (str): Name of the ECS Cluster
        service_name (str): Name of the matching ECS service string

    Returns:
        list: list of ECS Services Arns.
    """
    paginator = ecs.get_paginator("list_services")
    response_iterator = paginator.paginate(
        cluster=cluster_name, PaginationConfig={"PageSize": 100}
    )
    servicearn = []
    for service in response_iterator:
        for list_services in service.get("serviceArns"):
            if service_name in list_services:
                servicearn.append(list_services)
    return servicearn
