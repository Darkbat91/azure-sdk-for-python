# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_all_request(
    subscription_id: str,
    *,
    target_resource: Optional[str] = None,
    target_resource_group: Optional[str] = None,
    target_resource_type: Optional[str] = None,
    monitor_service: Optional[Union[str, "_models.MonitorService"]] = None,
    monitor_condition: Optional[Union[str, "_models.MonitorCondition"]] = None,
    severity: Optional[Union[str, "_models.Severity"]] = None,
    smart_group_state: Optional[Union[str, "_models.AlertState"]] = None,
    time_range: Optional[Union[str, "_models.TimeRange"]] = None,
    page_count: Optional[int] = None,
    sort_by: Optional[Union[str, "_models.SmartGroupsSortByFields"]] = None,
    sort_order: Optional[Union[str, "_models.SortOrder"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-05-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if target_resource is not None:
        _params["targetResource"] = _SERIALIZER.query("target_resource", target_resource, "str")
    if target_resource_group is not None:
        _params["targetResourceGroup"] = _SERIALIZER.query("target_resource_group", target_resource_group, "str")
    if target_resource_type is not None:
        _params["targetResourceType"] = _SERIALIZER.query("target_resource_type", target_resource_type, "str")
    if monitor_service is not None:
        _params["monitorService"] = _SERIALIZER.query("monitor_service", monitor_service, "str")
    if monitor_condition is not None:
        _params["monitorCondition"] = _SERIALIZER.query("monitor_condition", monitor_condition, "str")
    if severity is not None:
        _params["severity"] = _SERIALIZER.query("severity", severity, "str")
    if smart_group_state is not None:
        _params["smartGroupState"] = _SERIALIZER.query("smart_group_state", smart_group_state, "str")
    if time_range is not None:
        _params["timeRange"] = _SERIALIZER.query("time_range", time_range, "str")
    if page_count is not None:
        _params["pageCount"] = _SERIALIZER.query("page_count", page_count, "int")
    if sort_by is not None:
        _params["sortBy"] = _SERIALIZER.query("sort_by", sort_by, "str")
    if sort_order is not None:
        _params["sortOrder"] = _SERIALIZER.query("sort_order", sort_order, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_by_id_request(smart_group_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-05-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "smartGroupId": _SERIALIZER.url("smart_group_id", smart_group_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_change_state_request(
    smart_group_id: str, subscription_id: str, *, new_state: Union[str, "_models.AlertState"], **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-05-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "smartGroupId": _SERIALIZER.url("smart_group_id", smart_group_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["newState"] = _SERIALIZER.query("new_state", new_state, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_history_request(smart_group_id: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-05-preview"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "smartGroupId": _SERIALIZER.url("smart_group_id", smart_group_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class SmartGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.alertsmanagement.AlertsManagementClient`'s
        :attr:`smart_groups` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_all(
        self,
        target_resource: Optional[str] = None,
        target_resource_group: Optional[str] = None,
        target_resource_type: Optional[str] = None,
        monitor_service: Optional[Union[str, "_models.MonitorService"]] = None,
        monitor_condition: Optional[Union[str, "_models.MonitorCondition"]] = None,
        severity: Optional[Union[str, "_models.Severity"]] = None,
        smart_group_state: Optional[Union[str, "_models.AlertState"]] = None,
        time_range: Optional[Union[str, "_models.TimeRange"]] = None,
        page_count: Optional[int] = None,
        sort_by: Optional[Union[str, "_models.SmartGroupsSortByFields"]] = None,
        sort_order: Optional[Union[str, "_models.SortOrder"]] = None,
        **kwargs: Any
    ) -> Iterable["_models.SmartGroup"]:
        """Get all Smart Groups within a specified subscription.

        List all the Smart Groups within a specified subscription.

        :param target_resource: Filter by target resource( which is full ARM ID) Default value is
         select all. Default value is None.
        :type target_resource: str
        :param target_resource_group: Filter by target resource group name. Default value is select
         all. Default value is None.
        :type target_resource_group: str
        :param target_resource_type: Filter by target resource type. Default value is select all.
         Default value is None.
        :type target_resource_type: str
        :param monitor_service: Filter by monitor service which generates the alert instance. Default
         value is select all. Known values are: "Application Insights", "ActivityLog Administrative",
         "ActivityLog Security", "ActivityLog Recommendation", "ActivityLog Policy", "ActivityLog
         Autoscale", "Log Analytics", "Nagios", "Platform", "SCOM", "ServiceHealth", "SmartDetector",
         "VM Insights", and "Zabbix". Default value is None.
        :type monitor_service: str or ~azure.mgmt.alertsmanagement.models.MonitorService
        :param monitor_condition: Filter by monitor condition which is either 'Fired' or 'Resolved'.
         Default value is to select all. Known values are: "Fired" and "Resolved". Default value is
         None.
        :type monitor_condition: str or ~azure.mgmt.alertsmanagement.models.MonitorCondition
        :param severity: Filter by severity.  Default value is select all. Known values are: "Sev0",
         "Sev1", "Sev2", "Sev3", and "Sev4". Default value is None.
        :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
        :param smart_group_state: Filter by state of the smart group. Default value is to select all.
         Known values are: "New", "Acknowledged", and "Closed". Default value is None.
        :type smart_group_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :param time_range: Filter by time range by below listed values. Default value is 1 day. Known
         values are: "1h", "1d", "7d", and "30d". Default value is None.
        :type time_range: str or ~azure.mgmt.alertsmanagement.models.TimeRange
        :param page_count: Determines number of alerts returned per page in response. Permissible value
         is between 1 to 250. When the "includeContent"  filter is selected, maximum value allowed is
         25. Default value is 25. Default value is None.
        :type page_count: int
        :param sort_by: Sort the query results by input field. Default value is sort by
         'lastModifiedDateTime'. Known values are: "alertsCount", "state", "severity", "startDateTime",
         and "lastModifiedDateTime". Default value is None.
        :type sort_by: str or ~azure.mgmt.alertsmanagement.models.SmartGroupsSortByFields
        :param sort_order: Sort the query results order in either ascending or descending.  Default
         value is 'desc' for time fields and 'asc' for others. Known values are: "asc" and "desc".
         Default value is None.
        :type sort_order: str or ~azure.mgmt.alertsmanagement.models.SortOrder
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SmartGroup or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.alertsmanagement.models.SmartGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SmartGroupsList]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_get_all_request(
                    subscription_id=self._config.subscription_id,
                    target_resource=target_resource,
                    target_resource_group=target_resource_group,
                    target_resource_type=target_resource_type,
                    monitor_service=monitor_service,
                    monitor_condition=monitor_condition,
                    severity=severity,
                    smart_group_state=smart_group_state,
                    time_range=time_range,
                    page_count=page_count,
                    sort_by=sort_by,
                    sort_order=sort_order,
                    api_version=api_version,
                    template_url=self.get_all.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("SmartGroupsList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseAutoGenerated2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_all.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups"}  # type: ignore

    @distributed_trace
    def get_by_id(self, smart_group_id: str, **kwargs: Any) -> _models.SmartGroup:
        """Get information related to a specific Smart Group.

        Get information related to a specific Smart Group.

        :param smart_group_id: Smart group unique id. Required.
        :type smart_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroup or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SmartGroup]

        request = build_get_by_id_request(
            smart_group_id=smart_group_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseAutoGenerated2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))

        deserialized = self._deserialize("SmartGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_by_id.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}"}  # type: ignore

    @distributed_trace
    def change_state(
        self, smart_group_id: str, new_state: Union[str, "_models.AlertState"], **kwargs: Any
    ) -> _models.SmartGroup:
        """Change the state of a Smart Group.

        :param smart_group_id: Smart group unique id. Required.
        :type smart_group_id: str
        :param new_state: New state of the alert. Known values are: "New", "Acknowledged", and
         "Closed". Required.
        :type new_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroup or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SmartGroup]

        request = build_change_state_request(
            smart_group_id=smart_group_id,
            subscription_id=self._config.subscription_id,
            new_state=new_state,
            api_version=api_version,
            template_url=self.change_state.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseAutoGenerated2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))

        deserialized = self._deserialize("SmartGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    change_state.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState"}  # type: ignore

    @distributed_trace
    def get_history(self, smart_group_id: str, **kwargs: Any) -> _models.SmartGroupModification:
        """Get the history a smart group, which captures any Smart Group state changes
        (New/Acknowledged/Closed) .

        :param smart_group_id: Smart group unique id. Required.
        :type smart_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroupModification or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroupModification
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SmartGroupModification]

        request = build_get_history_request(
            smart_group_id=smart_group_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_history.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseAutoGenerated2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SmartGroupModification", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_history.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history"}  # type: ignore
