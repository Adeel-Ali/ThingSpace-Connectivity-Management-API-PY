# Getting Started

## How to Build


You must have Python greater than 2.7 installed in your system to build and run your SDK files. 
The generated code has dependencies over external libraries like nose, jsonpickle, etc. These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, we use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

The paths of Python and PIP must be properly set in the environment variables. Open command prompt and type ```pip --version```.
This should display the current version of the PIP Dependency Manager installed if the installation was successful.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python)


## How to Use

The following section explains how to use the ThingSpaceConnectivityManagementAPI library in a new project.

### 1. Open Project in an IDE

Open an IDE for Python like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python&projectName=thingspaceconnectivitymanagementapilib)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python&projectName=thingspaceconnectivitymanagementapilib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python&projectName=thingspaceconnectivitymanagementapilib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from thingspaceconnectivitymanagementapilib.thingspaceconnectivitymanagementapi_client import *
```

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python&libraryName=thingspaceconnectivitymanagementapilib.thingspaceconnectivitymanagementapi_client&projectName=thingspaceconnectivitymanagementapilib)

After this you can add code to initialize the client library and acquire the instance of a Controller class. Sample code to initialize the client library and using controller methods is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=ThingSpace%20Connectivity%20Management%20API-Python&libraryName=thingspaceconnectivitymanagementapilib.thingspaceconnectivitymanagementapi_client&projectName=thingspaceconnectivitymanagementapilib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

## Initialization

### Authentication and Initialization
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| api_key | TODO: add a description |



API client can be initialized as following.

```python
# Configuration parameters and credentials
api_key = "api_key"

client = ThingSpaceConnectivityManagementAPIClient(api_key)
```

## Class Reference

### <a name="list_of_controllers"></a>List of Controllers

* [SmsController](#sms_controller)
* [SessionController](#session_controller)
* [PlansController](#plans_controller)
* [LeadsController](#leads_controller)
* [GroupsController](#groups_controller)
* [DevicesController](#devices_controller)
* [CallbacksController](#callbacks_controller)

### <a name="sms_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SmsController") SmsController

#### Get controller instance

An instance of the ``` SmsController ``` class can be accessed from the API Client.

```python
 sms_client = client.sms
```

#### <a name="update_start_sms_callback_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".SmsController.update_start_sms_callback_using_put") update_start_sms_callback_using_put

> Starts delivery of queued SMS messages for the specific account.

```python
def update_start_sms_callback_using_put(self,
                                            aname,
                                            vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| aname |  ``` Required ```  | Account name |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
aname = 'aname'
vz_m_2_m_token = 'VZ-M2M-Token'

result = sms_client.update_start_sms_callback_using_put(aname, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="get_sms_messages_using_get"></a>![Method: ](http://apidocs.io/img/method.png ".SmsController.get_sms_messages_using_get") get_sms_messages_using_get

> Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

```python
def get_sms_messages_using_get(self,
                                   aname,
                                   vz_m_2_m_token,
                                   next = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| aname |  ``` Required ```  | Account name |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| next |  ``` Optional ```  | Continue the previous query from the URL in Location Header |



#### Example Usage

```python
aname = 'aname'
vz_m_2_m_token = 'VZ-M2M-Token'
next = 231

result = sms_client.get_sms_messages_using_get(aname, vz_m_2_m_token, next)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_send_sms_message_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".SmsController.create_send_sms_message_using_post") create_send_sms_message_using_post

> Sends an SMS message to one or more devices.

```python
def create_send_sms_message_using_post(self,
                                           request,
                                           vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | SMS Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = SMSSendRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = sms_client.create_send_sms_message_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="session_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SessionController") SessionController

#### Get controller instance

An instance of the ``` SessionController ``` class can be accessed from the API Client.

```python
 session_client = client.session
```

#### <a name="update_reset_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".SessionController.update_reset_using_put") update_reset_using_put

> Returns a new, randomly generated password for the current username

```python
def update_reset_using_put(self,
                               request,
                               vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Current Password |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = SessionResetPasswordRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = session_client.update_reset_using_put(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_logout_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".SessionController.create_logout_using_post") create_logout_using_post

> Ends a Connectivity Management session.

```python
def create_logout_using_post(self,
                                 vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'

result = session_client.create_logout_using_post(vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_login_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".SessionController.create_login_using_post") create_login_using_post

> Initiates a Connectivity Management session and returns a session token required in subsequent API requests.

```python
def create_login_using_post(self,
                                request = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Optional ```  | request |



#### Example Usage

```python
request = LogInRequest()

result = session_client.create_login_using_post(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="plans_controller"></a>![Class: ](http://apidocs.io/img/class.png ".PlansController") PlansController

#### Get controller instance

An instance of the ``` PlansController ``` class can be accessed from the API Client.

```python
 plans_client = client.plans
```

#### <a name="get_service_plan_list_using_get"></a>![Method: ](http://apidocs.io/img/method.png ".PlansController.get_service_plan_list_using_get") get_service_plan_list_using_get

> Returns a list of all data service plans that are associated with a specified account.

```python
def get_service_plan_list_using_get(self,
                                        vz_m_2_m_token,
                                        aname)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'

result = plans_client.get_service_plan_list_using_get(vz_m_2_m_token, aname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="leads_controller"></a>![Class: ](http://apidocs.io/img/class.png ".LeadsController") LeadsController

#### Get controller instance

An instance of the ``` LeadsController ``` class can be accessed from the API Client.

```python
 leads_client = client.leads
```

#### <a name="get_list_using_get_1"></a>![Method: ](http://apidocs.io/img/method.png ".LeadsController.get_list_using_get_1") get_list_using_get_1

> Returns information for all leads associated with the account

```python
def get_list_using_get_1(self,
                             vz_m_2_m_token,
                             aname,
                             next = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |
| next |  ``` Optional ```  | Continue the previous query from the pageUrl in Location Header |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'
next = 231

result = leads_client.get_list_using_get_1(vz_m_2_m_token, aname, next)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="groups_controller"></a>![Class: ](http://apidocs.io/img/class.png ".GroupsController") GroupsController

#### Get controller instance

An instance of the ``` GroupsController ``` class can be accessed from the API Client.

```python
 groups_client = client.groups
```

#### <a name="delete_device_group_using_delete"></a>![Method: ](http://apidocs.io/img/method.png ".GroupsController.delete_device_group_using_delete") delete_device_group_using_delete

> Deletes a device group. Devices in the group are moved to the default device group and are not deleted from the account.

```python
def delete_device_group_using_delete(self,
                                         vz_m_2_m_token,
                                         aname,
                                         gname)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |
| gname |  ``` Required ```  | Group name |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'
gname = 'gname'

result = groups_client.delete_device_group_using_delete(vz_m_2_m_token, aname, gname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="update_device_group_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".GroupsController.update_device_group_using_put") update_device_group_using_put

> Make changes to a device group, including changing the name and description, and adding or removing devices.

```python
def update_device_group_using_put(self,
                                      request,
                                      aname,
                                      gname,
                                      vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| aname |  ``` Required ```  | Account name |
| gname |  ``` Required ```  | Group name |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = GroupUpdateRequest()
aname = 'aname'
gname = 'gname'
vz_m_2_m_token = 'VZ-M2M-Token'

result = groups_client.update_device_group_using_put(request, aname, gname, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="get_device_group_info_using_get"></a>![Method: ](http://apidocs.io/img/method.png ".GroupsController.get_device_group_info_using_get") get_device_group_info_using_get

> Returns the name, description, and list of devices in a device group.

```python
def get_device_group_info_using_get(self,
                                        aname,
                                        gname,
                                        vz_m_2_m_token,
                                        next = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| aname |  ``` Required ```  | Account name |
| gname |  ``` Required ```  | Group name |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| next |  ``` Optional ```  | Continue the previous query from the pageUrl pagetoken |



#### Example Usage

```python
aname = 'aname'
gname = 'gname'
vz_m_2_m_token = 'VZ-M2M-Token'
next = 231

result = groups_client.get_device_group_info_using_get(aname, gname, vz_m_2_m_token, next)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="get_list_using_get"></a>![Method: ](http://apidocs.io/img/method.png ".GroupsController.get_list_using_get") get_list_using_get

> Returns a list of device groups in an account

```python
def get_list_using_get(self,
                           vz_m_2_m_token,
                           aname)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'

result = groups_client.get_list_using_get(vz_m_2_m_token, aname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_device_group_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".GroupsController.create_device_group_using_post") create_device_group_using_post

> Creates a new device group and optionally adds a set of devices to that group.

```python
def create_device_group_using_post(self,
                                       request,
                                       vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CreateDevGroupRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = groups_client.create_device_group_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="devices_controller"></a>![Class: ](http://apidocs.io/img/class.png ".DevicesController") DevicesController

#### Get controller instance

An instance of the ``` DevicesController ``` class can be accessed from the API Client.

```python
 devices_client = client.devices
```

#### <a name="change_device_id_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.change_device_id_using_put") change_device_id_using_put

> Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service.

```python
def change_device_id_using_put(self,
                                   service_type,
                                   request,
                                   vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serviceType |  ``` Required ```  | Identifier type |
| request |  ``` Required ```  | Device Usage Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
service_type = 'serviceType'
request = ChangeDeviceIdRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.change_device_id_using_put(service_type, request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_aggregate_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_aggregate_using_post") create_aggregate_using_post

> Returns the total amount of data sent and the total number of SMS messages sent or received by a set of devices in a specified timeframe.

```python
def create_aggregate_using_post(self,
                                    request,
                                    vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceAggregateUsageListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_aggregate_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_usage_list_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_usage_list_using_post") create_usage_list_using_post

> Returns the network data usage history of a device during a specified time period.

```python
def create_usage_list_using_post(self,
                                     request,
                                     vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device Usage Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceUsageListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_usage_list_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_prl_list_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_prl_list_using_post") create_prl_list_using_post

> Requests the current PRL version for devices, which can help determine which devices need a PRL update.

```python
def create_prl_list_using_post(self,
                                   request,
                                   vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device PRL Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DevicePrlListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_prl_list_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_provisioning_history_list_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_provisioning_history_list_using_post") create_provisioning_history_list_using_post

> Returns the provisioning history of a device during a specified time period.

```python
def create_provisioning_history_list_using_post(self,
                                                    request,
                                                    vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device ProHistory Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceProvisioningHistoryListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_provisioning_history_list_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="change_cost_center_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.change_cost_center_using_put") change_cost_center_using_put

> Changes or removes the costCenterCode value for one or more devices.

```python
def change_cost_center_using_put(self,
                                     request,
                                     vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceCostCenterRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.change_cost_center_using_put(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_connection_list_history_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_connection_list_history_using_post") create_connection_list_history_using_post

> Returns a list of network connection events for a device during a specified time period.

```python
def create_connection_list_history_using_post(self,
                                                  request,
                                                  vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device Connection Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceConnectionListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_connection_list_history_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_connection_list_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_connection_list_using_post") create_connection_list_using_post

> Returns a list of network connection events for a device during a specified time period.

```python
def create_connection_list_using_post(self,
                                          request,
                                          vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device Connection Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceConnectionListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_connection_list_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_restore_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_restore_using_post") create_restore_using_post

> Restore service to one or more suspended devices. 

```python
def create_restore_using_post(self,
                                  request,
                                  vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Update state |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CarrierActionsRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_restore_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_suspend_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_suspend_using_post") create_suspend_using_post

> Suspends service for one or more devices. 

```python
def create_suspend_using_post(self,
                                  request,
                                  vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Update state |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CarrierActionsRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_suspend_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="update_service_plan_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.update_service_plan_using_put") update_service_plan_using_put

> Sets a new service plan for one or more devices.

```python
def update_service_plan_using_put(self,
                                      request,
                                      vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = ServicePlanUpdateRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.update_service_plan_using_put(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_list_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_list_using_post") create_list_using_post

> Returns information about a specified device or a list of devices in an account.

```python
def create_list_using_post(self,
                               request,
                               vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Device Query |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = DeviceListRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_list_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_deactive_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_deactive_using_post") create_deactive_using_post

> Deactivates service for one or more devices.

```python
def create_deactive_using_post(self,
                                   request,
                                   vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Deactivate state |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CarrierDeactivateRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_deactive_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="update_custom_fields_using_put"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.update_custom_fields_using_put") update_custom_fields_using_put

> Updates one or more custom field values for devices.

```python
def update_custom_fields_using_put(self,
                                       request,
                                       vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Request |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CustomFieldsUpdateRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.update_custom_fields_using_put(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="add_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.add_using_post") add_using_post

> Adds up to 200 new devices, without provisioning lines of service for them.

```python
def add_using_post(self,
                       request,
                       vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Devices to Add |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = AddDevicesRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.add_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_active_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".DevicesController.create_active_using_post") create_active_using_post

> Activates service for one or more devices.

```python
def create_active_using_post(self,
                                 request,
                                 vz_m_2_m_token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Activate state |
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |



#### Example Usage

```python
request = CarrierActivateRequest()
vz_m_2_m_token = 'VZ-M2M-Token'

result = devices_client.create_active_using_post(request, vz_m_2_m_token)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)

### <a name="callbacks_controller"></a>![Class: ](http://apidocs.io/img/class.png ".CallbacksController") CallbacksController

#### Get controller instance

An instance of the ``` CallbacksController ``` class can be accessed from the API Client.

```python
 callbacks_client = client.callbacks
```

#### <a name="delete_unregister_callback_using_delete"></a>![Method: ](http://apidocs.io/img/method.png ".CallbacksController.delete_unregister_callback_using_delete") delete_unregister_callback_using_delete

> Stops the platform from sending callback messages for the specified account and service.

```python
def delete_unregister_callback_using_delete(self,
                                                vz_m_2_m_token,
                                                aname,
                                                sname)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |
| sname |  ``` Required ```  | Service name |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'
sname = 'sname'

result = callbacks_client.delete_unregister_callback_using_delete(vz_m_2_m_token, aname, sname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="create_register_callback_using_post"></a>![Method: ](http://apidocs.io/img/method.png ".CallbacksController.create_register_callback_using_post") create_register_callback_using_post

> Registers a URL where an account will receive RESTFul messages from a platform callback service.

```python
def create_register_callback_using_post(self,
                                            vz_m_2_m_token,
                                            aname,
                                            request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |
| request |  ``` Required ```  | Request |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'
request = RegisterCallbackRequest()

result = callbacks_client.create_register_callback_using_post(vz_m_2_m_token, aname, request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




#### <a name="list_callbacks_using_get"></a>![Method: ](http://apidocs.io/img/method.png ".CallbacksController.list_callbacks_using_get") list_callbacks_using_get

> Returns the name and endpoint URL of all callback listening services registered for a given account.

```python
def list_callbacks_using_get(self,
                                 vz_m_2_m_token,
                                 aname)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| vZM2MToken |  ``` Required ```  | M2M-MC Session Token |
| aname |  ``` Required ```  | Account name |



#### Example Usage

```python
vz_m_2_m_token = 'VZ-M2M-Token'
aname = 'aname'

result = callbacks_client.list_callbacks_using_get(vz_m_2_m_token, aname)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Error Response |




[Back to List of Controllers](#list_of_controllers)



