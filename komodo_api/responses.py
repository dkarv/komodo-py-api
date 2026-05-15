from .types import *
from typing import TypeVar, Callable

Res = TypeVar("Res")


class ReadApi:
    def __init__(self, request: Callable[[str, any, type[Res]], Res]):
        self.request = request

    async def _read(self, request: ReadRequest, clz: type[Res]) -> Res:
        return await self.request("read", request, clz)

    def getVersion(self, params: GetVersion) -> GetVersionResponse:
        return self._read(ReadRequestGetVersion(params=params), GetVersionResponse)

    def getCoreInfo(self, params: GetCoreInfo) -> GetCoreInfoResponse:
        return self._read(ReadRequestGetCoreInfo(params=params), GetCoreInfoResponse)

    def listSecrets(self, params: ListSecrets) -> ListSecretsResponse:
        return self._read(ReadRequestListSecrets(params=params), ListSecretsResponse)

    def listGitProvidersFromConfig(
        self, params: ListGitProvidersFromConfig
    ) -> ListGitProvidersFromConfigResponse:
        return self._read(
            ReadRequestListGitProvidersFromConfig(params=params),
            ListGitProvidersFromConfigResponse,
        )

    def listDockerRegistriesFromConfig(
        self, params: ListDockerRegistriesFromConfig
    ) -> ListDockerRegistriesFromConfigResponse:
        return self._read(
            ReadRequestListDockerRegistriesFromConfig(params=params),
            ListDockerRegistriesFromConfigResponse,
        )

    # ==== USER ====
    def getUsername(self, params: GetUsername) -> GetUsernameResponse:
        return self._read(ReadRequestGetUsername(params=params), GetUsernameResponse)

    def getPermission(self, params: GetPermission) -> GetPermissionResponse:
        return self._read(
            ReadRequestGetPermission(params=params), GetPermissionResponse
        )

    def findUser(self, params: FindUser) -> FindUserResponse:
        return self._read(ReadRequestFindUser(params=params), FindUserResponse)

    def listUsers(self, params: ListUsers) -> ListUsersResponse:
        return self._read(ReadRequestListUsers(params=params), ListUsersResponse)

    def listApiKeys(self, params: ListApiKeys) -> ListApiKeysResponse:
        return self._read(ReadRequestListApiKeys(params=params), ListApiKeysResponse)

    def listApiKeysForServiceUser(
        self, params: ListApiKeysForServiceUser
    ) -> ListApiKeysForServiceUserResponse:
        return self._read(
            ReadRequestListApiKeysForServiceUser(params=params),
            ListApiKeysForServiceUserResponse,
        )

    def listPermissions(self, params: ListPermissions) -> ListPermissionsResponse:
        return self._read(
            ReadRequestListPermissions(params=params), ListPermissionsResponse
        )

    def listUserTargetPermissions(
        self, params: ListUserTargetPermissions
    ) -> ListUserTargetPermissionsResponse:
        return self._read(
            ReadRequestListUserTargetPermissions(params=params),
            ListUserTargetPermissionsResponse,
        )

    # ==== USER GROUP ====
    def getUserGroup(self, params: GetUserGroup) -> GetUserGroupResponse:
        return self._read(ReadRequestGetUserGroup(params=params), GetUserGroupResponse)

    def listUserGroups(self, params: ListUserGroups) -> ListUserGroupsResponse:
        return self._read(
            ReadRequestListUserGroups(params=params), ListUserGroupsResponse
        )

    # ==== PROCEDURE ====
    def getProceduresSummary(
        self, params: GetProceduresSummary
    ) -> GetProceduresSummaryResponse:
        return self._read(
            ReadRequestGetProceduresSummary(params=params), GetProceduresSummaryResponse
        )

    def getProcedure(self, params: GetProcedure) -> GetProcedureResponse:
        return self._read(ReadRequestGetProcedure(params=params), GetProcedureResponse)

    def getProcedureActionState(
        self, params: GetProcedureActionState
    ) -> GetProcedureActionStateResponse:
        return self._read(
            ReadRequestGetProcedureActionState(params=params),
            GetProcedureActionStateResponse,
        )

    def listProcedures(self, params: ListProcedures) -> ListProceduresResponse:
        return self._read(
            ReadRequestListProcedures(params=params), ListProceduresResponse
        )

    def listFullProcedures(
        self, params: ListFullProcedures
    ) -> ListFullProceduresResponse:
        return self._read(
            ReadRequestListFullProcedures(params=params), ListFullProceduresResponse
        )

    # ==== ACTION ====
    def getActionsSummary(self, params: GetActionsSummary) -> GetActionsSummaryResponse:
        return self._read(
            ReadRequestGetActionsSummary(params=params), GetActionsSummaryResponse
        )

    def getAction(self, params: GetAction) -> GetActionResponse:
        return self._read(ReadRequestGetAction(params=params), GetActionResponse)

    def getActionActionState(
        self, params: GetActionActionState
    ) -> GetActionActionStateResponse:
        return self._read(
            ReadRequestGetActionActionState(params=params), GetActionActionStateResponse
        )

    def listActions(self, params: ListActions) -> ListActionsResponse:
        return self._read(ReadRequestListActions(params=params), ListActionsResponse)

    def listFullActions(self, params: ListFullActions) -> ListFullActionsResponse:
        return self._read(
            ReadRequestListFullActions(params=params), ListFullActionsResponse
        )

    # ==== SCHEDULE ====
    def listSchedules(self, params: ListSchedules) -> ListSchedulesResponse:
        return self._read(
            ReadRequestListSchedules(params=params), ListSchedulesResponse
        )

    # ==== SERVER ====
    def getServersSummary(self, params: GetServersSummary) -> GetServersSummaryResponse:
        return self._read(
            ReadRequestGetServersSummary(params=params), GetServersSummaryResponse
        )

    def getServer(self, params: GetServer) -> GetServerResponse:
        return self._read(ReadRequestGetServer(params=params), GetServerResponse)

    def getServerState(self, params: GetServerState) -> GetServerStateResponse:
        return self._read(
            ReadRequestGetServerState(params=params), GetServerStateResponse
        )

#    def getPeripheryVersion(
#        self, params: GetPeripheryVersion
#    ) -> GetPeripheryVersionResponse:
#        return self._read(
#            ReadRequestGetPeripheryVersion(params=params), GetPeripheryVersionResponse
#        )

    def getDockerContainersSummary(
        self, params: GetDockerContainersSummary
    ) -> GetDockerContainersSummaryResponse:
        return self._read(
            ReadRequestGetDockerContainersSummary(params=params),
            GetDockerContainersSummaryResponse,
        )

    def listDockerContainers(
        self, params: ListDockerContainers
    ) -> ListDockerContainersResponse:
        return self._read(
            ReadRequestListDockerContainers(params=params), ListDockerContainersResponse
        )

    def listAllDockerContainers(
        self, params: ListAllDockerContainers
    ) -> ListAllDockerContainersResponse:
        return self._read(
            ReadRequestListAllDockerContainers(params=params),
            ListAllDockerContainersResponse,
        )

    def inspectDockerContainer(
        self, params: InspectDockerContainer
    ) -> InspectDockerContainerResponse:
        return self._read(
            ReadRequestInspectDockerContainer(params=params),
            InspectDockerContainerResponse,
        )

    def getResourceMatchingContainer(
        self, params: GetResourceMatchingContainer
    ) -> GetResourceMatchingContainerResponse:
        return self._read(
            ReadRequestGetResourceMatchingContainer(params=params),
            GetResourceMatchingContainerResponse,
        )

    def getContainerLog(self, params: GetContainerLog) -> GetContainerLogResponse:
        return self._read(
            ReadRequestGetContainerLog(params=params), GetContainerLogResponse
        )

    def searchContainerLog(
        self, params: SearchContainerLog
    ) -> SearchContainerLogResponse:
        return self._read(
            ReadRequestSearchContainerLog(params=params), SearchContainerLogResponse
        )

    def listDockerNetworks(
        self, params: ListDockerNetworks
    ) -> ListDockerNetworksResponse:
        return self._read(
            ReadRequestListDockerNetworks(params=params), ListDockerNetworksResponse
        )

    def inspectDockerNetwork(
        self, params: InspectDockerNetwork
    ) -> InspectDockerNetworkResponse:
        return self._read(
            ReadRequestInspectDockerNetwork(params=params), InspectDockerNetworkResponse
        )

    def listDockerImages(self, params: ListDockerImages) -> ListDockerImagesResponse:
        return self._read(
            ReadRequestListDockerImages(params=params), ListDockerImagesResponse
        )

    def inspectDockerImage(
        self, params: InspectDockerImage
    ) -> InspectDockerImageResponse:
        return self._read(
            ReadRequestInspectDockerImage(params=params), InspectDockerImageResponse
        )

    def listDockerImageHistory(
        self, params: ListDockerImageHistory
    ) -> ListDockerImageHistoryResponse:
        return self._read(
            ReadRequestListDockerImageHistory(params=params),
            ListDockerImageHistoryResponse,
        )

    def listDockerVolumes(self, params: ListDockerVolumes) -> ListDockerVolumesResponse:
        return self._read(
            ReadRequestListDockerVolumes(params=params), ListDockerVolumesResponse
        )

    def inspectDockerVolume(
        self, params: InspectDockerVolume
    ) -> InspectDockerVolumeResponse:
        return self._read(
            ReadRequestInspectDockerVolume(params=params), InspectDockerVolumeResponse
        )

    def listComposeProjects(
        self, params: ListComposeProjects
    ) -> ListComposeProjectsResponse:
        return self._read(
            ReadRequestListComposeProjects(params=params), ListComposeProjectsResponse
        )

    def getServerActionState(
        self, params: GetServerActionState
    ) -> GetServerActionStateResponse:
        return self._read(
            ReadRequestGetServerActionState(params=params), GetServerActionStateResponse
        )

    def getHistoricalServerStats(
        self, params: GetHistoricalServerStats
    ) -> GetHistoricalServerStatsResponse:
        return self._read(
            ReadRequestGetHistoricalServerStats(params=params),
            GetHistoricalServerStatsResponse,
        )

    def listServers(self, params: ListServers) -> ListServersResponse:
        return self._read(ReadRequestListServers(params=params), ListServersResponse)

    def listFullServers(self, params: ListFullServers) -> ListFullServersResponse:
        return self._read(
            ReadRequestListFullServers(params=params), ListFullServersResponse
        )

    def listTerminals(self, params: ListTerminals) -> ListTerminalsResponse:
        return self._read(
            ReadRequestListTerminals(params=params), ListTerminalsResponse
        )

    # ==== STACK ====
    def getStacksSummary(self, params: GetStacksSummary) -> GetStacksSummaryResponse:
        return self._read(
            ReadRequestGetStacksSummary(params=params), GetStacksSummaryResponse
        )

    def getStack(self, params: GetStack) -> GetStackResponse:
        return self._read(ReadRequestGetStack(params=params), GetStackResponse)

    def getStackActionState(
        self, params: GetStackActionState
    ) -> GetStackActionStateResponse:
        return self._read(
            ReadRequestGetStackActionState(params=params), GetStackActionStateResponse
        )

#    def getStackWebhooksEnabled(
#        self, params: GetStackWebhooksEnabled
#    ) -> GetStackWebhooksEnabledResponse:
#        return self._read(
#            ReadRequestGetStackWebhooksEnabled(params=params),
#            GetStackWebhooksEnabledResponse,
#        )

    def getStackLog(self, params: GetStackLog) -> GetStackLogResponse:
        return self._read(ReadRequestGetStackLog(params=params), GetStackLogResponse)

    def searchStackLog(self, params: SearchStackLog) -> SearchStackLogResponse:
        return self._read(
            ReadRequestSearchStackLog(params=params), SearchStackLogResponse
        )

    def inspectStackContainer(
        self, params: InspectStackContainer
    ) -> InspectStackContainerResponse:
        return self._read(
            ReadRequestInspectStackContainer(params=params),
            InspectStackContainerResponse,
        )

    def listStacks(self, params: ListStacks) -> ListStacksResponse:
        return self._read(ReadRequestListStacks(params=params), ListStacksResponse)

    def listFullStacks(self, params: ListFullStacks) -> ListFullStacksResponse:
        return self._read(
            ReadRequestListFullStacks(params=params), ListFullStacksResponse
        )

    def listStackServices(self, params: ListStackServices) -> ListStackServicesResponse:
        return self._read(
            ReadRequestListStackServices(params=params), ListStackServicesResponse
        )

    def listCommonStackExtraArgs(
        self, params: ListCommonStackExtraArgs
    ) -> ListCommonStackExtraArgsResponse:
        return self._read(
            ReadRequestListCommonStackExtraArgs(params=params),
            ListCommonStackExtraArgsResponse,
        )

    def listCommonStackBuildExtraArgs(
        self, params: ListCommonStackBuildExtraArgs
    ) -> ListCommonStackBuildExtraArgsResponse:
        return self._read(
            ReadRequestListCommonStackBuildExtraArgs(params=params),
            ListCommonStackBuildExtraArgsResponse,
        )

    # ==== DEPLOYMENT ====
    def getDeploymentsSummary(
        self, params: GetDeploymentsSummary
    ) -> GetDeploymentsSummaryResponse:
        return self._read(
            ReadRequestGetDeploymentsSummary(params=params),
            GetDeploymentsSummaryResponse,
        )

    def getDeployment(self, params: GetDeployment) -> GetDeploymentResponse:
        return self._read(
            ReadRequestGetDeployment(params=params), GetDeploymentResponse
        )

    def getDeploymentContainer(
        self, params: GetDeploymentContainer
    ) -> GetDeploymentContainerResponse:
        return self._read(
            ReadRequestGetDeploymentContainer(params=params),
            GetDeploymentContainerResponse,
        )

    def getDeploymentActionState(
        self, params: GetDeploymentActionState
    ) -> GetDeploymentActionStateResponse:
        return self._read(
            ReadRequestGetDeploymentActionState(params=params),
            GetDeploymentActionStateResponse,
        )

    def getDeploymentStats(
        self, params: GetDeploymentStats
    ) -> GetDeploymentStatsResponse:
        return self._read(
            ReadRequestGetDeploymentStats(params=params), GetDeploymentStatsResponse
        )

    def getDeploymentLog(self, params: GetDeploymentLog) -> GetDeploymentLogResponse:
        return self._read(
            ReadRequestGetDeploymentLog(params=params), GetDeploymentLogResponse
        )

    def searchDeploymentLog(
        self, params: SearchDeploymentLog
    ) -> SearchDeploymentLogResponse:
        return self._read(
            ReadRequestSearchDeploymentLog(params=params), SearchDeploymentLogResponse
        )

    def inspectDeploymentContainer(
        self, params: InspectDeploymentContainer
    ) -> InspectDeploymentContainerResponse:
        return self._read(
            ReadRequestInspectDeploymentContainer(params=params),
            InspectDeploymentContainerResponse,
        )

    def listDeployments(self, params: ListDeployments) -> ListDeploymentsResponse:
        return self._read(
            ReadRequestListDeployments(params=params), ListDeploymentsResponse
        )

    def listFullDeployments(
        self, params: ListFullDeployments
    ) -> ListFullDeploymentsResponse:
        return self._read(
            ReadRequestListFullDeployments(params=params), ListFullDeploymentsResponse
        )

    def listCommonDeploymentExtraArgs(
        self, params: ListCommonDeploymentExtraArgs
    ) -> ListCommonDeploymentExtraArgsResponse:
        return self._read(
            ReadRequestListCommonDeploymentExtraArgs(params=params),
            ListCommonDeploymentExtraArgsResponse,
        )

    # ==== BUILD ====
    def getBuildsSummary(self, params: GetBuildsSummary) -> GetBuildsSummaryResponse:
        return self._read(
            ReadRequestGetBuildsSummary(params=params), GetBuildsSummaryResponse
        )

    def getBuild(self, params: GetBuild) -> GetBuildResponse:
        return self._read(ReadRequestGetBuild(params=params), GetBuildResponse)

    def getBuildActionState(
        self, params: GetBuildActionState
    ) -> GetBuildActionStateResponse:
        return self._read(
            ReadRequestGetBuildActionState(params=params), GetBuildActionStateResponse
        )

    def getBuildMonthlyStats(
        self, params: GetBuildMonthlyStats
    ) -> GetBuildMonthlyStatsResponse:
        return self._read(
            ReadRequestGetBuildMonthlyStats(params=params), GetBuildMonthlyStatsResponse
        )

#    def getBuildWebhookEnabled(
#        self, params: GetBuildWebhookEnabled
#    ) -> GetBuildWebhookEnabledResponse:
#        return self._read(
#            ReadRequestGetBuildWebhookEnabled(params=params),
#            GetBuildWebhookEnabledResponse,
#        )

    def listBuilds(self, params: ListBuilds) -> ListBuildsResponse:
        return self._read(ReadRequestListBuilds(params=params), ListBuildsResponse)

    def listFullBuilds(self, params: ListFullBuilds) -> ListFullBuildsResponse:
        return self._read(
            ReadRequestListFullBuilds(params=params), ListFullBuildsResponse
        )

    def listBuildVersions(self, params: ListBuildVersions) -> ListBuildVersionsResponse:
        return self._read(
            ReadRequestListBuildVersions(params=params), ListBuildVersionsResponse
        )

    def listCommonBuildExtraArgs(
        self, params: ListCommonBuildExtraArgs
    ) -> ListCommonBuildExtraArgsResponse:
        return self._read(
            ReadRequestListCommonBuildExtraArgs(params=params),
            ListCommonBuildExtraArgsResponse,
        )

    # ==== REPO ====
    def getReposSummary(self, params: GetReposSummary) -> GetReposSummaryResponse:
        return self._read(
            ReadRequestGetReposSummary(params=params), GetReposSummaryResponse
        )

    def getRepo(self, params: GetRepo) -> GetRepoResponse:
        return self._read(ReadRequestGetRepo(params=params), GetRepoResponse)

    def getRepoActionState(
        self, params: GetRepoActionState
    ) -> GetRepoActionStateResponse:
        return self._read(
            ReadRequestGetRepoActionState(params=params), GetRepoActionStateResponse
        )

#    def getRepoWebhooksEnabled(
#        self, params: GetRepoWebhooksEnabled
#    ) -> GetRepoWebhooksEnabledResponse:
#        return self._read(
#            ReadRequestGetRepoWebhooksEnabled(params=params),
#            GetRepoWebhooksEnabledResponse,
#        )

    def listRepos(self, params: ListRepos) -> ListReposResponse:
        return self._read(ReadRequestListRepos(params=params), ListReposResponse)

    def listFullRepos(self, params: ListFullRepos) -> ListFullReposResponse:
        return self._read(
            ReadRequestListFullRepos(params=params), ListFullReposResponse
        )

    # ==== SYNC ====
    def getResourceSyncsSummary(
        self, params: GetResourceSyncsSummary
    ) -> GetResourceSyncsSummaryResponse:
        return self._read(
            ReadRequestGetResourceSyncsSummary(params=params),
            GetResourceSyncsSummaryResponse,
        )

    def getResourceSync(self, params: GetResourceSync) -> GetResourceSyncResponse:
        return self._read(
            ReadRequestGetResourceSync(params=params), GetResourceSyncResponse
        )

    def getResourceSyncActionState(
        self, params: GetResourceSyncActionState
    ) -> GetResourceSyncActionStateResponse:
        return self._read(
            ReadRequestGetResourceSyncActionState(params=params),
            GetResourceSyncActionStateResponse,
        )

#    def getSyncWebhooksEnabled(
#        self, params: GetSyncWebhooksEnabled
#    ) -> GetSyncWebhooksEnabledResponse:
#        return self._read(
#            ReadRequestGetSyncWebhooksEnabled(params=params),
#            GetSyncWebhooksEnabledResponse,
#        )

    def listResourceSyncs(self, params: ListResourceSyncs) -> ListResourceSyncsResponse:
        return self._read(
            ReadRequestListResourceSyncs(params=params), ListResourceSyncsResponse
        )

    def listFullResourceSyncs(
        self, params: ListFullResourceSyncs
    ) -> ListFullResourceSyncsResponse:
        return self._read(
            ReadRequestListFullResourceSyncs(params=params),
            ListFullResourceSyncsResponse,
        )

    # ==== BUILDER ====
    def getBuildersSummary(
        self, params: GetBuildersSummary
    ) -> GetBuildersSummaryResponse:
        return self._read(
            ReadRequestGetBuildersSummary(params=params), GetBuildersSummaryResponse
        )

    def getBuilder(self, params: GetBuilder) -> GetBuilderResponse:
        return self._read(ReadRequestGetBuilder(params=params), GetBuilderResponse)

    def listBuilders(self, params: ListBuilders) -> ListBuildersResponse:
        return self._read(ReadRequestListBuilders(params=params), ListBuildersResponse)

    def listFullBuilders(self, params: ListFullBuilders) -> ListFullBuildersResponse:
        return self._read(
            ReadRequestListFullBuilders(params=params), ListFullBuildersResponse
        )

    # ==== ALERTER ====
    def getAlertersSummary(
        self, params: GetAlertersSummary
    ) -> GetAlertersSummaryResponse:
        return self._read(
            ReadRequestGetAlertersSummary(params=params), GetAlertersSummaryResponse
        )

    def getAlerter(self, params: GetAlerter) -> GetAlerterResponse:
        return self._read(ReadRequestGetAlerter(params=params), GetAlerterResponse)

    def listAlerters(self, params: ListAlerters) -> ListAlertersResponse:
        return self._read(ReadRequestListAlerters(params=params), ListAlertersResponse)

    def listFullAlerters(self, params: ListFullAlerters) -> ListFullAlertersResponse:
        return self._read(
            ReadRequestListFullAlerters(params=params), ListFullAlertersResponse
        )

    # ==== TOML ====
    def exportAllResourcesToToml(
        self, params: ExportAllResourcesToToml
    ) -> ExportAllResourcesToTomlResponse:
        return self._read(
            ReadRequestExportAllResourcesToToml(params=params),
            ExportAllResourcesToTomlResponse,
        )

    def exportResourcesToToml(
        self, params: ExportResourcesToToml
    ) -> ExportResourcesToTomlResponse:
        return self._read(
            ReadRequestExportResourcesToToml(params=params),
            ExportResourcesToTomlResponse,
        )

    # ==== TAG ====
    def getTag(self, params: GetTag) -> GetTagResponse:
        return self._read(ReadRequestGetTag(params=params), GetTagResponse)

    def listTags(self, params: ListTags) -> ListTagsResponse:
        return self._read(ReadRequestListTags(params=params), ListTagsResponse)

    # ==== UPDATE ====
    def getUpdate(self, params: GetUpdate) -> GetUpdateResponse:
        return self._read(ReadRequestGetUpdate(params=params), GetUpdateResponse)

    def listUpdates(self, params: ListUpdates) -> ListUpdatesResponse:
        return self._read(ReadRequestListUpdates(params=params), ListUpdatesResponse)

    # ==== ALERT ====
    def listAlerts(self, params: ListAlerts) -> ListAlertsResponse:
        return self._read(ReadRequestListAlerts(params=params), ListAlertsResponse)

    def getAlert(self, params: GetAlert) -> GetAlertResponse:
        return self._read(ReadRequestGetAlert(params=params), GetAlertResponse)

    # ==== SERVER STATS ====
    def getSystemInformation(
        self, params: GetSystemInformation
    ) -> GetSystemInformationResponse:
        return self._read(
            ReadRequestGetSystemInformation(params=params), GetSystemInformationResponse
        )

    def getSystemStats(self, params: GetSystemStats) -> GetSystemStatsResponse:
        return self._read(
            ReadRequestGetSystemStats(params=params), GetSystemStatsResponse
        )

    def listSystemProcesses(
        self, params: ListSystemProcesses
    ) -> ListSystemProcessesResponse:
        return self._read(
            ReadRequestListSystemProcesses(params=params), ListSystemProcessesResponse
        )

    # ==== VARIABLE ====
    def getVariable(self, params: GetVariable) -> GetVariableResponse:
        return self._read(ReadRequestGetVariable(params=params), GetVariableResponse)

    def listVariables(self, params: ListVariables) -> ListVariablesResponse:
        return self._read(
            ReadRequestListVariables(params=params), ListVariablesResponse
        )

    # ==== PROVIDER ====
    def getGitProviderAccount(
        self, params: GetGitProviderAccount
    ) -> GetGitProviderAccountResponse:
        return self._read(
            ReadRequestGetGitProviderAccount(params=params),
            GetGitProviderAccountResponse,
        )

    def listGitProviderAccounts(
        self, params: ListGitProviderAccounts
    ) -> ListGitProviderAccountsResponse:
        return self._read(
            ReadRequestListGitProviderAccounts(params=params),
            ListGitProviderAccountsResponse,
        )

    def getDockerRegistryAccount(
        self, params: GetDockerRegistryAccount
    ) -> GetDockerRegistryAccountResponse:
        return self._read(
            ReadRequestGetDockerRegistryAccount(params=params),
            GetDockerRegistryAccountResponse,
        )

    def listDockerRegistryAccounts(
        self, params: ListDockerRegistryAccounts
    ) -> ListDockerRegistryAccountsResponse:
        return self._read(
            ReadRequestListDockerRegistryAccounts(params=params),
            ListDockerRegistryAccountsResponse,
        )


class WriteApi:
    def __init__(self, request: Callable[[str, any, type[Res]], Res]):
        self.request = request

    async def _write(self, request: WriteRequest, clz: type[Res]) -> Res:
        return await self.request("write", request, clz)

    # ==== USER ====
    def createLocalUser(self, params: CreateLocalUser) -> CreateLocalUserResponse:
        return self._write(
            WriteRequestCreateLocalUser(params=params), CreateLocalUserResponse
        )

#    def updateUserUsername(
#        self, params: UpdateUserUsername
#    ) -> UpdateUserUsernameResponse:
#        return self._write(
#            WriteRequestUpdateUserUsername(params=params), UpdateUserUsernameResponse
#        )

#    def updateUserPassword(
#        self, params: UpdateUserPassword
#    ) -> UpdateUserPasswordResponse:
#        return self._write(
#            WriteRequestUpdateUserPassword(params=params), UpdateUserPasswordResponse
#        )

    def deleteUser(self, params: DeleteUser) -> DeleteUserResponse:
        return self._write(WriteRequestDeleteUser(params=params), DeleteUserResponse)

    # ==== SERVICE USER ====
    def createServiceUser(self, params: CreateServiceUser) -> CreateServiceUserResponse:
        return self._write(
            WriteRequestCreateServiceUser(params=params), CreateServiceUserResponse
        )

    def updateServiceUserDescription(
        self, params: UpdateServiceUserDescription
    ) -> UpdateServiceUserDescriptionResponse:
        return self._write(
            WriteRequestUpdateServiceUserDescription(params=params),
            UpdateServiceUserDescriptionResponse,
        )

    def createApiKeyForServiceUser(
        self, params: CreateApiKeyForServiceUser
    ) -> CreateApiKeyForServiceUserResponse:
        return self._write(
            WriteRequestCreateApiKeyForServiceUser(params=params),
            CreateApiKeyForServiceUserResponse,
        )

    def deleteApiKeyForServiceUser(
        self, params: DeleteApiKeyForServiceUser
    ) -> DeleteApiKeyForServiceUserResponse:
        return self._write(
            WriteRequestDeleteApiKeyForServiceUser(params=params),
            DeleteApiKeyForServiceUserResponse,
        )

    # ==== USER GROUP ====
    def createUserGroup(self, params: CreateUserGroup) -> UserGroup:
        return self._write(WriteRequestCreateUserGroup(params=params), UserGroup)

    def renameUserGroup(self, params: RenameUserGroup) -> UserGroup:
        return self._write(WriteRequestRenameUserGroup(params=params), UserGroup)

    def deleteUserGroup(self, params: DeleteUserGroup) -> UserGroup:
        return self._write(WriteRequestDeleteUserGroup(params=params), UserGroup)

    def addUserToUserGroup(self, params: AddUserToUserGroup) -> UserGroup:
        return self._write(WriteRequestAddUserToUserGroup(params=params), UserGroup)

    def removeUserFromUserGroup(self, params: RemoveUserFromUserGroup) -> UserGroup:
        return self._write(
            WriteRequestRemoveUserFromUserGroup(params=params), UserGroup
        )

    def setUsersInUserGroup(self, params: SetUsersInUserGroup) -> UserGroup:
        return self._write(WriteRequestSetUsersInUserGroup(params=params), UserGroup)

    def setEveryoneUserGroup(self, params: SetEveryoneUserGroup) -> UserGroup:
        return self._write(WriteRequestSetEveryoneUserGroup(params=params), UserGroup)

    # ==== PERMISSIONS ====
    def updateUserAdmin(self, params: UpdateUserAdmin) -> UpdateUserAdminResponse:
        return self._write(
            WriteRequestUpdateUserAdmin(params=params), UpdateUserAdminResponse
        )

    def updateUserBasePermissions(
        self, params: UpdateUserBasePermissions
    ) -> UpdateUserBasePermissionsResponse:
        return self._write(
            WriteRequestUpdateUserBasePermissions(params=params),
            UpdateUserBasePermissionsResponse,
        )

    def updatePermissionOnResourceType(
        self, params: UpdatePermissionOnResourceType
    ) -> UpdatePermissionOnResourceTypeResponse:
        return self._write(
            WriteRequestUpdatePermissionOnResourceType(params=params),
            UpdatePermissionOnResourceTypeResponse,
        )

    def updatePermissionOnTarget(
        self, params: UpdatePermissionOnTarget
    ) -> UpdatePermissionOnTargetResponse:
        return self._write(
            WriteRequestUpdatePermissionOnTarget(params=params),
            UpdatePermissionOnTargetResponse,
        )

    # ==== DESCRIPTION ====
    def updateResourceMeta(self, params: UpdateResourceMeta) -> UpdateResourceMetaResponse:
        return self._write(
            WriteRequestUpdateResourceMeta(params=params), UpdateResourceMetaResponse
        )

    # ==== SERVER ====
    def createServer(self, params: CreateServer) -> Server:
        return self._write(WriteRequestCreateServer(params=params), Server)

    def copyServer(self, params: CopyServer) -> Server:
        return self._write(WriteRequestCopyServer(params=params), Server)

    def deleteServer(self, params: DeleteServer) -> Server:
        return self._write(WriteRequestDeleteServer(params=params), Server)

    def updateServer(self, params: UpdateServer) -> Server:
        return self._write(WriteRequestUpdateServer(params=params), Server)

    def renameServer(self, params: RenameServer) -> Update:
        return self._write(WriteRequestRenameServer(params=params), Update)

    def createNetwork(self, params: CreateNetwork) -> Update:
        return self._write(WriteRequestCreateNetwork(params=params), Update)

    def createTerminal(self, params: CreateTerminal) -> NoData:
        return self._write(WriteRequestCreateTerminal(params=params), NoData)

    def deleteTerminal(self, params: DeleteTerminal) -> NoData:
        return self._write(WriteRequestDeleteTerminal(params=params), NoData)

    def deleteAllTerminals(self, params: DeleteAllTerminals) -> NoData:
        return self._write(WriteRequestDeleteAllTerminals(params=params), NoData)

    # ==== STACK ====
    def createStack(self, params: CreateStack) -> Stack:
        return self._write(WriteRequestCreateStack(params=params), Stack)

    def copyStack(self, params: CopyStack) -> Stack:
        return self._write(WriteRequestCopyStack(params=params), Stack)

    def deleteStack(self, params: DeleteStack) -> Stack:
        return self._write(WriteRequestDeleteStack(params=params), Stack)

    def updateStack(self, params: UpdateStack) -> Stack:
        return self._write(WriteRequestUpdateStack(params=params), Stack)

    def renameStack(self, params: RenameStack) -> Update:
        return self._write(WriteRequestRenameStack(params=params), Update)

    def writeStackFileContents(self, params: WriteStackFileContents) -> Update:
        return self._write(WriteRequestWriteStackFileContents(params=params), Update)

    def refreshStackCache(self, params: RefreshStackCache) -> NoData:
        return self._write(WriteRequestRefreshStackCache(params=params), NoData)

#    def createStackWebhook(
#        self, params: CreateStackWebhook
#    ) -> CreateStackWebhookResponse:
#        return self._write(
#            WriteRequestCreateStackWebhook(params=params), CreateStackWebhookResponse
#        )

#    def deleteStackWebhook(
#        self, params: DeleteStackWebhook
#    ) -> DeleteStackWebhookResponse:
#        return self._write(
#            WriteRequestDeleteStackWebhook(params=params), DeleteStackWebhookResponse
#        )

    # ==== DEPLOYMENT ====
    def createDeployment(self, params: CreateDeployment) -> Deployment:
        return self._write(WriteRequestCreateDeployment(params=params), Deployment)

    def copyDeployment(self, params: CopyDeployment) -> Deployment:
        return self._write(WriteRequestCopyDeployment(params=params), Deployment)

    def createDeploymentFromContainer(
        self, params: CreateDeploymentFromContainer
    ) -> Deployment:
        return self._write(
            WriteRequestCreateDeploymentFromContainer(params=params), Deployment
        )

    def deleteDeployment(self, params: DeleteDeployment) -> Deployment:
        return self._write(WriteRequestDeleteDeployment(params=params), Deployment)

    def updateDeployment(self, params: UpdateDeployment) -> Deployment:
        return self._write(WriteRequestUpdateDeployment(params=params), Deployment)

    def renameDeployment(self, params: RenameDeployment) -> Update:
        return self._write(WriteRequestRenameDeployment(params=params), Update)

    # ==== BUILD ====
    def createBuild(self, params: CreateBuild) -> Build:
        return self._write(WriteRequestCreateBuild(params=params), Build)

    def copyBuild(self, params: CopyBuild) -> Build:
        return self._write(WriteRequestCopyBuild(params=params), Build)

    def deleteBuild(self, params: DeleteBuild) -> Build:
        return self._write(WriteRequestDeleteBuild(params=params), Build)

    def updateBuild(self, params: UpdateBuild) -> Build:
        return self._write(WriteRequestUpdateBuild(params=params), Build)

    def refreshBuildCache(self, params: RefreshBuildCache) -> NoData:
        return self._write(WriteRequestRefreshBuildCache(params=params), NoData)

#    def createBuildWebhook(
#        self, params: CreateBuildWebhook
#    ) -> CreateBuildWebhookResponse:
#        return self._write(
#            WriteRequestCreateBuildWebhook(params=params), CreateBuildWebhookResponse
#        )

#    def deleteBuildWebhook(
#        self, params: DeleteBuildWebhook
#    ) -> DeleteBuildWebhookResponse:
#        return self._write(
#            WriteRequestDeleteBuildWebhook(params=params), DeleteBuildWebhookResponse
#        )

    # ==== BUILDER ====
    def createBuilder(self, params: CreateBuilder) -> Builder:
        return self._write(WriteRequestCreateBuilder(params=params), Builder)

    def copyBuilder(self, params: CopyBuilder) -> Builder:
        return self._write(WriteRequestCopyBuilder(params=params), Builder)

    def deleteBuilder(self, params: DeleteBuilder) -> Builder:
        return self._write(WriteRequestDeleteBuilder(params=params), Builder)

    def updateBuilder(self, params: UpdateBuilder) -> Builder:
        return self._write(WriteRequestUpdateBuilder(params=params), Builder)

    def renameBuilder(self, params: RenameBuilder) -> Update:
        return self._write(WriteRequestRenameBuilder(params=params), Update)

    # ==== REPO ====
    def createRepo(self, params: CreateRepo) -> Repo:
        return self._write(WriteRequestCreateRepo(params=params), Repo)

    def copyRepo(self, params: CopyRepo) -> Repo:
        return self._write(WriteRequestCopyRepo(params=params), Repo)

    def deleteRepo(self, params: DeleteRepo) -> Repo:
        return self._write(WriteRequestDeleteRepo(params=params), Repo)

    def updateRepo(self, params: UpdateRepo) -> Repo:
        return self._write(WriteRequestUpdateRepo(params=params), Repo)

    def renameRepo(self, params: RenameRepo) -> Update:
        return self._write(WriteRequestRenameRepo(params=params), Update)

    def refreshRepoCache(self, params: RefreshRepoCache) -> NoData:
        return self._write(WriteRequestRefreshRepoCache(params=params), NoData)

#    def createRepoWebhook(self, params: CreateRepoWebhook) -> CreateRepoWebhookResponse:
#        return self._write(
#            WriteRequestCreateRepoWebhook(params=params), CreateRepoWebhookResponse
#        )

#    def deleteRepoWebhook(self, params: DeleteRepoWebhook) -> DeleteRepoWebhookResponse:
#        return self._write(
#            WriteRequestDeleteRepoWebhook(params=params), DeleteRepoWebhookResponse
#        )

    # ==== ALERTER ====
    def createAlerter(self, params: CreateAlerter) -> Alerter:
        return self._write(WriteRequestCreateAlerter(params=params), Alerter)

    def copyAlerter(self, params: CopyAlerter) -> Alerter:
        return self._write(WriteRequestCopyAlerter(params=params), Alerter)

    def deleteAlerter(self, params: DeleteAlerter) -> Alerter:
        return self._write(WriteRequestDeleteAlerter(params=params), Alerter)

    def updateAlerter(self, params: UpdateAlerter) -> Alerter:
        return self._write(WriteRequestUpdateAlerter(params=params), Alerter)

    def renameAlerter(self, params: RenameAlerter) -> Update:
        return self._write(WriteRequestRenameAlerter(params=params), Update)

    # ==== PROCEDURE ====
    def createProcedure(self, params: CreateProcedure) -> Procedure:
        return self._write(WriteRequestCreateProcedure(params=params), Procedure)

    def copyProcedure(self, params: CopyProcedure) -> Procedure:
        return self._write(WriteRequestCopyProcedure(params=params), Procedure)

    def deleteProcedure(self, params: DeleteProcedure) -> Procedure:
        return self._write(WriteRequestDeleteProcedure(params=params), Procedure)

    def updateProcedure(self, params: UpdateProcedure) -> Procedure:
        return self._write(WriteRequestUpdateProcedure(params=params), Procedure)

    def renameProcedure(self, params: RenameProcedure) -> Update:
        return self._write(WriteRequestRenameProcedure(params=params), Update)

    # ==== ACTION ====
    def createAction(self, params: CreateAction) -> Action:
        return self._write(WriteRequestCreateAction(params=params), Action)

    def copyAction(self, params: CopyAction) -> Action:
        return self._write(WriteRequestCopyAction(params=params), Action)

    def deleteAction(self, params: DeleteAction) -> Action:
        return self._write(WriteRequestDeleteAction(params=params), Action)

    def updateAction(self, params: UpdateAction) -> Action:
        return self._write(WriteRequestUpdateAction(params=params), Action)

    def renameAction(self, params: RenameAction) -> Update:
        return self._write(WriteRequestRenameAction(params=params), Update)

    # ==== SYNC ====
    def createResourceSync(self, params: CreateResourceSync) -> ResourceSync:
        return self._write(WriteRequestCreateResourceSync(params=params), ResourceSync)

    def copyResourceSync(self, params: CopyResourceSync) -> ResourceSync:
        return self._write(WriteRequestCopyResourceSync(params=params), ResourceSync)

    def deleteResourceSync(self, params: DeleteResourceSync) -> ResourceSync:
        return self._write(WriteRequestDeleteResourceSync(params=params), ResourceSync)

    def updateResourceSync(self, params: UpdateResourceSync) -> ResourceSync:
        return self._write(WriteRequestUpdateResourceSync(params=params), ResourceSync)

    def renameResourceSync(self, params: RenameResourceSync) -> Update:
        return self._write(WriteRequestRenameResourceSync(params=params), Update)

    def commitSync(self, params: CommitSync) -> Update:
        return self._write(WriteRequestCommitSync(params=params), Update)

    def writeSyncFileContents(self, params: WriteSyncFileContents) -> Update:
        return self._write(WriteRequestWriteSyncFileContents(params=params), Update)

    def refreshResourceSyncPending(
        self, params: RefreshResourceSyncPending
    ) -> ResourceSync:
        return self._write(
            WriteRequestRefreshResourceSyncPending(params=params), ResourceSync
        )

#    def createSyncWebhook(self, params: CreateSyncWebhook) -> CreateSyncWebhookResponse:
#        return self._write(
#            WriteRequestCreateSyncWebhook(params=params), CreateSyncWebhookResponse
#        )

#    def deleteSyncWebhook(self, params: DeleteSyncWebhook) -> DeleteSyncWebhookResponse:
#        return self._write(
#            WriteRequestDeleteSyncWebhook(params=params), DeleteSyncWebhookResponse
#        )

    # ==== TAG ====
    def createTag(self, params: CreateTag) -> Tag:
        return self._write(WriteRequestCreateTag(params=params), Tag)

    def deleteTag(self, params: DeleteTag) -> Tag:
        return self._write(WriteRequestDeleteTag(params=params), Tag)

    def renameTag(self, params: RenameTag) -> Tag:
        return self._write(WriteRequestRenameTag(params=params), Tag)

    def updateTagColor(self, params: UpdateTagColor) -> Tag:
        return self._write(WriteRequestUpdateTagColor(params=params), Tag)

    # ==== VARIABLE ====
    def createVariable(self, params: CreateVariable) -> CreateVariableResponse:
        return self._write(
            WriteRequestCreateVariable(params=params), CreateVariableResponse
        )

    def updateVariableValue(
        self, params: UpdateVariableValue
    ) -> UpdateVariableValueResponse:
        return self._write(
            WriteRequestUpdateVariableValue(params=params), UpdateVariableValueResponse
        )

    def updateVariableDescription(
        self, params: UpdateVariableDescription
    ) -> UpdateVariableDescriptionResponse:
        return self._write(
            WriteRequestUpdateVariableDescription(params=params),
            UpdateVariableDescriptionResponse,
        )

    def updateVariableIsSecret(
        self, params: UpdateVariableIsSecret
    ) -> UpdateVariableIsSecretResponse:
        return self._write(
            WriteRequestUpdateVariableIsSecret(params=params),
            UpdateVariableIsSecretResponse,
        )

    def deleteVariable(self, params: DeleteVariable) -> DeleteVariableResponse:
        return self._write(
            WriteRequestDeleteVariable(params=params), DeleteVariableResponse
        )

    # ==== PROVIDERS ====
    def createGitProviderAccount(
        self, params: CreateGitProviderAccount
    ) -> CreateGitProviderAccountResponse:
        return self._write(
            WriteRequestCreateGitProviderAccount(params=params),
            CreateGitProviderAccountResponse,
        )

    def updateGitProviderAccount(
        self, params: UpdateGitProviderAccount
    ) -> UpdateGitProviderAccountResponse:
        return self._write(
            WriteRequestUpdateGitProviderAccount(params=params),
            UpdateGitProviderAccountResponse,
        )

    def deleteGitProviderAccount(
        self, params: DeleteGitProviderAccount
    ) -> DeleteGitProviderAccountResponse:
        return self._write(
            WriteRequestDeleteGitProviderAccount(params=params),
            DeleteGitProviderAccountResponse,
        )

    def createDockerRegistryAccount(
        self, params: CreateDockerRegistryAccount
    ) -> CreateDockerRegistryAccountResponse:
        return self._write(
            WriteRequestCreateDockerRegistryAccount(params=params),
            CreateDockerRegistryAccountResponse,
        )

    def updateDockerRegistryAccount(
        self, params: UpdateDockerRegistryAccount
    ) -> UpdateDockerRegistryAccountResponse:
        return self._write(
            WriteRequestUpdateDockerRegistryAccount(params=params),
            UpdateDockerRegistryAccountResponse,
        )

    def deleteDockerRegistryAccount(
        self, params: DeleteDockerRegistryAccount
    ) -> DeleteDockerRegistryAccountResponse:
        return self._write(
            WriteRequestDeleteDockerRegistryAccount(params=params),
            DeleteDockerRegistryAccountResponse,
        )


class ExecuteApi:
    def __init__(self, request: Callable[[str, any, type[Res]], Res]):
        self.request = request

    async def _execute(self, request: ExecuteRequest, clz: type[Res]) -> Res:
        return await self.request("execute", request, clz)

    # ==== SERVER ====
    def startContainer(self, params: StartContainer) -> Update:
        return self._execute(ExecuteRequestStartContainer(params=params), Update)

    def restartContainer(self, params: RestartContainer) -> Update:
        return self._execute(ExecuteRequestRestartContainer(params=params), Update)

    def pauseContainer(self, params: PauseContainer) -> Update:
        return self._execute(ExecuteRequestPauseContainer(params=params), Update)

    def unpauseContainer(self, params: UnpauseContainer) -> Update:
        return self._execute(ExecuteRequestUnpauseContainer(params=params), Update)

    def stopContainer(self, params: StopContainer) -> Update:
        return self._execute(ExecuteRequestStopContainer(params=params), Update)

    def destroyContainer(self, params: DestroyContainer) -> Update:
        return self._execute(ExecuteRequestDestroyContainer(params=params), Update)

    def startAllContainers(self, params: StartAllContainers) -> Update:
        return self._execute(ExecuteRequestStartAllContainers(params=params), Update)

    def restartAllContainers(self, params: RestartAllContainers) -> Update:
        return self._execute(ExecuteRequestRestartAllContainers(params=params), Update)

    def pauseAllContainers(self, params: PauseAllContainers) -> Update:
        return self._execute(ExecuteRequestPauseAllContainers(params=params), Update)

    def unpauseAllContainers(self, params: UnpauseAllContainers) -> Update:
        return self._execute(ExecuteRequestUnpauseAllContainers(params=params), Update)

    def stopAllContainers(self, params: StopAllContainers) -> Update:
        return self._execute(ExecuteRequestStopAllContainers(params=params), Update)

    def pruneContainers(self, params: PruneContainers) -> Update:
        return self._execute(ExecuteRequestPruneContainers(params=params), Update)

    def deleteNetwork(self, params: DeleteNetwork) -> Update:
        return self._execute(ExecuteRequestDeleteNetwork(params=params), Update)

    def pruneNetworks(self, params: PruneNetworks) -> Update:
        return self._execute(ExecuteRequestPruneNetworks(params=params), Update)

    def deleteImage(self, params: DeleteImage) -> Update:
        return self._execute(ExecuteRequestDeleteImage(params=params), Update)

    def pruneImages(self, params: PruneImages) -> Update:
        return self._execute(ExecuteRequestPruneImages(params=params), Update)

    def deleteVolume(self, params: DeleteVolume) -> Update:
        return self._execute(ExecuteRequestDeleteVolume(params=params), Update)

    def pruneVolumes(self, params: PruneVolumes) -> Update:
        return self._execute(ExecuteRequestPruneVolumes(params=params), Update)

    def pruneDockerBuilders(self, params: PruneDockerBuilders) -> Update:
        return self._execute(ExecuteRequestPruneDockerBuilders(params=params), Update)

    def pruneBuildx(self, params: PruneBuildx) -> Update:
        return self._execute(ExecuteRequestPruneBuildx(params=params), Update)

    def pruneSystem(self, params: PruneSystem) -> Update:
        return self._execute(ExecuteRequestPruneSystem(params=params), Update)

    # ==== STACK ====
    def deployStack(self, params: DeployStack) -> Update:
        return self._execute(ExecuteRequestDeployStack(params=params), Update)

    def batchDeployStack(self, params: BatchDeployStack) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchDeployStack(params=params), BatchExecutionResponse)

    def deployStackIfChanged(self, params: DeployStackIfChanged) -> Update:
        return self._execute(ExecuteRequestDeployStackIfChanged(params=params), Update)

    def batchDeployStackIfChanged(
        self, params: BatchDeployStackIfChanged
    ) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchDeployStackIfChanged(params=params), BatchExecutionResponse)

    def pullStack(self, params: PullStack) -> Update:
        return self._execute(ExecuteRequestPullStack(params=params), Update)

    def batchPullStack(self, params: BatchPullStack) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchPullStack(params=params), BatchExecutionResponse)

    def startStack(self, params: StartStack) -> Update:
        return self._execute(ExecuteRequestStartStack(params=params), Update)

    def restartStack(self, params: RestartStack) -> Update:
        return self._execute(ExecuteRequestRestartStack(params=params), Update)

    def stopStack(self, params: StopStack) -> Update:
        return self._execute(ExecuteRequestStopStack(params=params), Update)

    def pauseStack(self, params: PauseStack) -> Update:
        return self._execute(ExecuteRequestPauseStack(params=params), Update)

    def unpauseStack(self, params: UnpauseStack) -> Update:
        return self._execute(ExecuteRequestUnpauseStack(params=params), Update)

    def destroyStack(self, params: DestroyStack) -> Update:
        return self._execute(ExecuteRequestDestroyStack(params=params), Update)
    
    def runStackService(self, params: RunStackService) -> Update:
        return self._execute(ExecuteRequestRunStackService(params=params), Update)

    def batchDestroyStack(self, params: BatchDestroyStack) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchDestroyStack(params=params), BatchExecutionResponse)

    # ==== DEPLOYMENT ====
    def deploy(self, params: Deploy) -> Update:
        return self._execute(ExecuteRequestDeploy(params=params), Update)

    def batchDeploy(self, params: BatchDeploy) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchDeploy(params=params), BatchExecutionResponse)

    def pullDeployment(self, params: PullDeployment) -> Update:
        return self._execute(ExecuteRequestPullDeployment(params=params), Update)

    def startDeployment(self, params: StartDeployment) -> Update:
        return self._execute(ExecuteRequestStartDeployment(params=params), Update)

    def restartDeployment(self, params: RestartDeployment) -> Update:
        return self._execute(ExecuteRequestRestartDeployment(params=params), Update)

    def pauseDeployment(self, params: PauseDeployment) -> Update:
        return self._execute(ExecuteRequestPauseDeployment(params=params), Update)

    def unpauseDeployment(self, params: UnpauseDeployment) -> Update:
        return self._execute(ExecuteRequestUnpauseDeployment(params=params), Update)

    def stopDeployment(self, params: StopDeployment) -> Update:
        return self._execute(ExecuteRequestStopDeployment(params=params), Update)

    def destroyDeployment(self, params: DestroyDeployment) -> Update:
        return self._execute(ExecuteRequestDestroyDeployment(params=params), Update)

    def batchDestroyDeployment(
        self, params: BatchDestroyDeployment
    ) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchDestroyDeployment(params=params), BatchExecutionResponse)

    # ==== BUILD ====
    def runBuild(self, params: RunBuild) -> Update:
        return self._execute(ExecuteRequestRunBuild(params=params), Update)

    def batchRunBuild(self, params: BatchRunBuild) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchRunBuild(params=params), BatchExecutionResponse)

    def cancelBuild(self, params: CancelBuild) -> Update:
        return self._execute(ExecuteRequestCancelBuild(params=params), Update)

    # ==== REPO ====
    def cloneRepo(self, params: CloneRepo) -> Update:
        return self._execute(ExecuteRequestCloneRepo(params=params), Update)

    def batchCloneRepo(self, params: BatchCloneRepo) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchCloneRepo(params=params), BatchExecutionResponse)

    def pullRepo(self, params: PullRepo) -> Update:
        return self._execute(ExecuteRequestPullRepo(params=params), Update)

    def batchPullRepo(self, params: BatchPullRepo) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchPullRepo(params=params), BatchExecutionResponse)

    def buildRepo(self, params: BuildRepo) -> Update:
        return self._execute(ExecuteRequestBuildRepo(params=params), Update)

    def batchBuildRepo(self, params: BatchBuildRepo) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchBuildRepo(params=params), BatchExecutionResponse)

    def cancelRepoBuild(self, params: CancelRepoBuild) -> Update:
        return self._execute(ExecuteRequestCancelRepoBuild(params=params), Update)

    # ==== PROCEDURE ====
    def runProcedure(self, params: RunProcedure) -> Update:
        return self._execute(ExecuteRequestRunProcedure(params=params), Update)

    def batchRunProcedure(self, params: BatchRunProcedure) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchRunProcedure(params=params), BatchExecutionResponse)

    # ==== ACTION ====
    def runAction(self, params: RunAction) -> Update:
        return self._execute(ExecuteRequestRunAction(params=params), Update)

    def batchRunAction(self, params: BatchRunAction) -> BatchExecutionResponse:
        return self._execute(ExecuteRequestBatchRunAction(params=params), BatchExecutionResponse)

    # ==== SYNC ====
    def runSync(self, params: RunSync) -> Update:
        return self._execute(ExecuteRequestRunSync(params=params), Update)

    # ==== ALERTER ====
    def testAlerter(self, params: TestAlerter) -> Update:
        return self._execute(ExecuteRequestTestAlerter(params=params), Update)
    
    def sendAlert(self, params: SendAlert) -> Update:
        return self._execute(ExecuteRequestSendAlert(params=params), Update)
    
    # ==== MAINTENANCE ====
    def clearRepoCache(self, params: ClearRepoCache) -> Update:
        return self._execute(ExecuteRequestClearRepoCache(params=params), Update)
    
    def backupCoreDatabase(self, params: BackupCoreDatabase) -> Update:
        return self._execute(ExecuteRequestBackupCoreDatabase(params=params), Update)
    
    def globalAutoUpdate(self, params: GlobalAutoUpdate) -> Update:
        return self._execute(ExecuteRequestGlobalAutoUpdate(params=params), Update)
